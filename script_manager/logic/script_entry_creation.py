import sqlite3
import shutil
from datetime import datetime
from pathlib import Path

from .data_models import Script
from .log_creation import new_app_log
from . import integrity_checker
from . import user_input
from ..menus import screen_render


def create_new_script(state, app_data, BODIES, MENUS, NEW_SCRIPT_ID):        
        confirmation, new_script = temp_script_creation(state, app_data, BODIES, MENUS, NEW_SCRIPT_ID)

        if not confirmation:
            return
        
        set_script_path(new_script, app_data)
        set_script_platform(new_script)
        set_script_hash(new_script, app_data)
        new_script.status = "Ready"
        new_script.archived = False
        update_db_script_table(new_script, app_data)
        new_app_log(app_data, "NEW", "ENTRY", new_script)


def temp_script_creation(state, app_data, BODIES, MENUS, NEW_SCRIPT_ID):
    temp_script = Script(
        id=NEW_SCRIPT_ID,
        name=None,
        type=None,
        platform=None,
        last_run=None,
        sha256=None,
        desc=None,
        date_added=datetime.now(),
        date_modified=datetime.now(),
        path="None",
        run_count=0,
        archived=False,
)
    app_data["scripts"].append(temp_script)

    while True:
        creation_steps = [
            ("ADD_FILE", user_input.file_input, "path"),
            ("ADD_NAME", user_input.name_input, "name"),
            ("ADD_TYPE", user_input.type_input, "type"),
            ("ADD_DESC", user_input.desc_input, "desc"),
            ("ADD_CONFIRM", user_input.creation_confirm_input, "none")
        ]

        for menu, input, attr in creation_steps:
            state.update({"body": "ADD", "menu": menu})
            screen_render.refresh_screen(state, app_data, BODIES, MENUS)
            
            value = input(state, app_data, BODIES, MENUS)
            if value == "0":
                temp_script_deletion(app_data, NEW_SCRIPT_ID)
                return False, None
            
            if attr != "none":
                setattr(temp_script, attr, value)

        return True, temp_script
        

def temp_script_deletion(app_data, NEW_SCRIPT_ID):
    for script in app_data["scripts"]:
        if script.id == NEW_SCRIPT_ID:
            app_data["scripts"].remove(script)
            break


def set_script_path(new_script, app_data):
    # expected script directory for input validation
    script_folder = app_data["config"]["folders"]["scripts_dir"]
    APP_ROOT = Path(__file__).parent.parent.parent
    SCRIPTS_DIR = (APP_ROOT / script_folder).resolve()
    
    # complete path to the file currently in scripts dir
    current_path = (SCRIPTS_DIR / new_script.path).resolve()
    filename = new_script.path
    
    # new directory for the script, named after the script
    new_dir = SCRIPTS_DIR / new_script.name
    new_dir.mkdir(exist_ok=True)  # make dir if it doesn't exist
    
    # new path for the file inside the new directory
    new_file_path = new_dir / filename
    
    # move the file
    shutil.move(str(current_path), str(new_file_path))
    
    # update the path in the script object relative to scripts dir
    new_script.path = Path(new_script.name) / filename


def set_script_platform(new_script):
    extension = new_script.path.suffix.lower()

    EXTENSIONS = {
        ".py": "Python",
        ".sh": "Bash",
        ".ps1": "Powershell",
    }

    new_script.platform = EXTENSIONS.get(extension, "Other")


def set_script_hash(new_script, app_data):
    script_folder = app_data["config"]["folders"]["scripts_dir"]
    APP_ROOT = Path(__file__).parent.parent.parent
    SCRIPTS_DIR = (APP_ROOT / script_folder).resolve()
    complete_file_path = (SCRIPTS_DIR / new_script.path).resolve()

    hash_value = integrity_checker.calculate_sha256(complete_file_path)
    new_script.sha256 = hash_value


def update_db_script_table(new_script, app_data):
    creation_query = """
    INSERT INTO scripts (
        name, type, platform, last_run, sha256, desc,
        date_added, date_modified, path, run_count, archived
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """

    db_path = app_data["config"]["files"]["app_db"]
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute(
        creation_query,
        (
            new_script.name,
            new_script.type,
            new_script.platform,
            new_script.last_run.isoformat() if new_script.last_run else None,
            new_script.sha256,
            new_script.desc,
            new_script.date_added.isoformat(),
            new_script.date_modified.isoformat(),
            str(new_script.path),
            new_script.run_count,
            int(new_script.archived)
        )
    )
    con.commit()
    con.close()