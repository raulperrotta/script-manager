import sqlite3
import socket
import uuid
from datetime import datetime
from pathlib import Path
from .data_models import AppLog
from .data_models import RunLog


def new_app_log(app_data, log_type, log_code, script=None):
    if not app_data["app_logs"]:
        new_id = 1
    else:
        log_count = len(app_data["app_logs"])
        last_log = app_data["app_logs"][log_count - 1]
        new_id = last_log.id + 1
        
    new_app_log = AppLog(
        id = new_id,
        date = datetime.now(),
        type = log_type,
        code = log_code,
        script_id=script.id if script else None,
        script_name=script.name if script else None
    )

    app_data["app_logs"].append(new_app_log)

    creation_query = """
    INSERT INTO app_logs (date, type, code, script_id, script_name)
    VALUES (?, ?, ?, ?, ?)
    """

    db_path = app_data["config"]["files"]["app_db"]
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute(
        creation_query,
        (
            new_app_log.date.isoformat(),
            new_app_log.type,
            new_app_log.code,
            new_app_log.script_id,
            new_app_log.script_name
        )
    )
    con.commit()
    con.close()

    app_logs_txt_path = Path(app_data["config"]["files"]["app_logs_txt"])
    with app_logs_txt_path.open("a", encoding="utf-8") as file:
        file.write(f'{new_app_log.date.strftime("%Y-%m-%d %H:%M")} | {new_app_log.type} | {new_app_log.code} | {new_app_log.script_id} | {new_app_log.script_name}\n')


def new_run_log(app_data, script):
    if not app_data["run_logs"]:
        new_id = 1
    else:
        log_count = len(app_data["run_logs"])
        last_log = app_data["run_logs"][log_count - 1]
        new_id = last_log.id + 1

    new_run_log = RunLog(
        id = new_id,
        script_id = script.id,
        script_name = script.name,
        run_date = datetime.now(),
        host_name = socket.gethostname(),
        host_id = f"{uuid.getnode():012x}"
    )

    app_data["run_logs"].append(new_run_log)

    creation_query = """
    INSERT INTO run_logs (script_id, script_name, run_date, host_name, host_id)
    VALUES (?, ?, ?, ?, ?)
    """

    db_path = app_data["config"]["files"]["app_db"]
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute(
        creation_query,
        (
            new_run_log.script_id,
            new_run_log.script_name,
            new_run_log.run_date.isoformat(),
            new_run_log.host_name,
            new_run_log.host_id
        )
    )
    con.commit()
    con.close()

    run_logs_txt_path = Path(app_data["config"]["files"]["run_logs_txt"])
    with run_logs_txt_path.open("a", encoding="utf-8") as file:
        file.write(f'{new_run_log.run_date.strftime("%Y-%m-%d %H:%M:%S")} | {new_run_log.script_id} | {new_run_log.script_name} | {new_run_log.host_name} | {new_run_log.host_id}\n')