from dataclasses import dataclass, field
from pathlib import Path
from datetime import datetime


# config file format
CONFIG_FORMAT = {
    "app": [
        "app_name",
    ],
    "settings": [
        "sort_style",
    ],
    "folders": [
        "data_dir",
        "scripts_dir",
        "logs_dir",
    ],
    "files": [
        "app_db",
        "run_logs_txt",
        "app_logs_txt",
    ],
}

# expected schema for database
SCHEMA = {
    "scripts": {
        "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
        "name": "TEXT",
        "type": "TEXT",
        "last_run": "TEXT",
        "sha256": "TEXT",
        "desc": "TEXT",
        "date_added": "TEXT",
        "date_modified": "TEXT",
        "path": "TEXT",
        "run_count": "INTEGER",
        "archived": "INTEGER"  
    },
    "run_logs": {
        "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
        "script_id": "INTEGER",
        "script_name": "TEXT",
        "run_date": "TEXT",
        "host_name": "TEXT",
        "host_id": "TEXT"
    },
    "app_logs": {
        "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
        "date": "TEXT",
        "type": "TEXT",
        "code": "TEXT",
        "script_id": "INTEGER",
        "script_name": "TEXT",
        "old_data": "TEXT",
        "new_data": "TEXT" 
    }
}

# script object model
@dataclass
class Script:
    id: int
    name: str
    type: str
    last_run: datetime
    sha256: str
    desc: str
    date_added: datetime
    date_modified: datetime
    path: Path
    run_count: int
    archived: bool

    # runtime only
    status: str = field(default=None, repr=False)

# run log object model
@dataclass
class RunLog:
    id: int
    script_id: int
    script_name: str
    run_date: datetime
    host_name: str
    host_id: str

# app log object model
@dataclass
class AppLog:
    id: int
    date: datetime
    type: str
    code: str 
    script_id: int = field(default=None, repr=False)
    script_name: str = field(default=None, repr=False)
    old_data: str = field(default=None, repr=False)
    new_data: str = field(default=None, repr=False)
