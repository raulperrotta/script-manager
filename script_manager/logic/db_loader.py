import sqlite3
from datetime import datetime
from pathlib import Path
from dataclasses import fields
from script_manager.logic.data_models import Script, RunLog, AppLog
from script_manager.logic.integrity_checker import calculate_sha256


class Loader:
    def __init__(self, db_path):
        self.db_path = Path(db_path)

    # return all rows from a table in the database
    def get_table_data(self, table):
        con = sqlite3.connect(self.db_path)
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute(f"SELECT * FROM {table}")
        rows = cur.fetchall()
        con.close()
        return rows
    
    def convert_row_to_object(self, row, data_model):
        # create data holder
        object_data = {}
    
        for field in fields(data_model):
            field_data = row[field.name] if field.name in row.keys() else None
            # convert data types if needed
            if field.type is datetime and field_data:
                field_data = datetime.fromisoformat(field_data)

            elif field.type is Path and field_data:
                field_data = Path(field_data)

            elif field.type is bool:
                field_data = bool(field_data)
            # store field data in holder
            object_data[field.name] = field_data
        # create object with data
        return data_model(**object_data)

    # create script list from db table
    def load_scripts(self):
        self.scripts = []
        rows = self.get_table_data("scripts")
        self.scripts = [self.convert_row_to_object(row, Script) for row in rows]
        return self.scripts

    # create run log list from db table
    def load_run_logs(self):
        self.run_logs = []
        rows = self.get_table_data("run_logs")
        self.run_logs = [self.convert_row_to_object(row, RunLog) for row in rows]
        return self.run_logs

    # create app log list from db table
    def load_app_logs(self):
        self.app_logs = []
        rows = self.get_table_data("app_logs")
        self.app_logs = [self.convert_row_to_object(row, AppLog) for row in rows]
        return self.app_logs
    

def set_script_status(script_list, script_folder):
    APP_ROOT = Path(__file__).parent.parent.parent
    SCRIPTS_DIR = (APP_ROOT / script_folder).resolve()

    for script in script_list:
        # checks for script file location
        complete_file_path = (SCRIPTS_DIR / script.path).resolve()

        if not Path(complete_file_path).exists():
            script.status = "Path Not Found"
        # checks for file integrity
        elif script.sha256 != calculate_sha256(complete_file_path):
            script.status = "Modified"    
        # path found & SHA256 check passed
        else:            
            script.status = "Ready"
    return script_list


# orchestrator
def database_loader(db_path, scripts_dir):
    loader = Loader(db_path)
    script_list = loader.load_scripts()
    script_list = set_script_status(script_list, scripts_dir)
    run_log_list = loader.load_run_logs()
    app_log_list = loader.load_app_logs()
    return script_list, run_log_list, app_log_list