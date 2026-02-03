import datetime
import sqlite3
from pathlib import Path
from .data_models import AppLog


def new_app_log(app_data, log_type, log_code, script=None):

    new_app_log = AppLog(
        date=datetime.now(),
        type=log_type,
        code=log_code,
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
