import sqlite3
import shutil
from pathlib import Path
from .log_creation import new_app_log
from .data_builder import get_script_by_id

def edit_script_entry(app_data, script_id, field, value, target):
    script = get_script_by_id(script_id, app_data["scripts"])
    setattr(script, field, value)

    edit_query = f"""
        UPDATE scripts
        SET {field} = ?
        WHERE id = ?
    """

    db_path = app_data["config"]["files"]["app_db"]
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute(
        edit_query,
        (
            value,
            script.id
        )
    )
    con.commit()
    con.close()

    new_app_log(app_data, "EDIT", target, script)


def update_path(app_data, script):
    script_folder = app_data["config"]["folders"]["scripts_dir"]
    APP_ROOT = Path(__file__).parent.parent.parent
    SCRIPTS_DIR = (APP_ROOT / script_folder).resolve()

    current_path = Path(script.path)

    current_folder_name = current_path.parent
    filename = current_path.name

    new_folder_name = script.name

    current_full_path = (SCRIPTS_DIR / current_folder_name).resolve()
    new_full_path = (SCRIPTS_DIR / new_folder_name).resolve()

    current_full_path.rename(new_full_path)

    script.path = Path(script.name) / filename

    edit_query = """
        UPDATE scripts
        SET path = ?
        WHERE id = ?
    """

    db_path = app_data["config"]["files"]["app_db"]
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute(
        edit_query, 
        (
            str(script.path),
            script.id
        )
    )
    con.commit()
    con.close()