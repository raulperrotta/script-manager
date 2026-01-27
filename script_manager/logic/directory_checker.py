from pathlib import Path
import sys


def validate_directories(config):
    # loads folder path into variable
    for option in config["folders"]:
        dir_path = config.get("folders", option)
        path = Path(dir_path)

        # create directory if missing
        if not path.exists():
            path.mkdir(parents=True, exist_ok=True)

        # exits if path is not a folder
        if not path.is_dir():
             print(f"ERROR: {path} not a directory")
             sys.exit(1)