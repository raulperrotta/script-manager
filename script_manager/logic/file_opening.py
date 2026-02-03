import subprocess
import sys
from pathlib import Path


def open_file(path, script_list=None, script=None):
    APP_ROOT = Path(__file__).parent.parent.parent

    if script:
        scripts_dir = (APP_ROOT / path).resolve()
        complete_path = (scripts_dir / script.path).resolve()

        if sys.platform.startswith("win"):
            subprocess.run(["notepad", str(complete_path)])
        elif sys.platform == "darwin":
            subprocess.run(["open", str(complete_path)])
        else:
            subprocess.run(["xdg-open", str(complete_path)])

    else:
        complete_path = (APP_ROOT / path).resolve()

        if sys.platform.startswith("win"):
            subprocess.Popen(["notepad", str(complete_path)])
        elif sys.platform == "darwin":
            subprocess.Popen(["open", str(complete_path)])
        else:
            subprocess.Popen(["xdg-open", str(complete_path)])

