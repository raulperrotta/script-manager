from script_manager.logic.data_models import SCHEMA
from script_manager.bootstrap.db_checker import check_db
from pathlib import Path
import sys


def validate_files(config):
    for file, file_path in config['files'].items():
        path = Path(file_path)

        if path.suffix == '.db':
            # pass database path and schema validate correctness
            if "app_db" in file:
                check_db(path, SCHEMA)
            else:
                print(f"ERROR: no schema defined for {file}")
                sys.exit(1)

        # creates the .txt file if it does not exist
        elif path.suffix == '.txt':
            if not path.exists():
                path.touch()

        # exits if file extension is not .db or .txt
        else:
            print(f"ERROR: unsupported file type {path}")
            sys.exit(1)