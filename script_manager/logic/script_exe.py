import subprocess
import sys
from pathlib import Path
from .log_creation import new_run_log


def run_script(app_data, script):
    APP_ROOT = Path(__file__).parent.parent.parent
    SCRIPTS_DIR = (APP_ROOT / app_data["config"]["folders"]["scripts_dir"]).resolve()
    script_path = (SCRIPTS_DIR / script.path).resolve()

    file_extension = script_path.suffix.lower()

    if sys.platform.startswith("win"):
        if file_extension == ".py":
            args = [sys.executable, str(script_path)]

        elif file_extension == ".ps1":
            args = [
                "powershell",
                "-ExecutionPolicy", "Bypass",
                "-File", str(script_path)
            ]

        else:
            args = [str(script_path)]

    else:
        if file_extension == ".py":
            args = [sys.executable, str(script_path)]
        else:
            script_path.chmod(script_path.stat().st_mode | 0o111)
            args = [str(script_path)]

    process = subprocess.Popen(
        args,
        cwd=script_path.parent,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        stdin=subprocess.DEVNULL
    )

    script.process = process
    script.status = "Running"
    new_run_log(app_data, script)


def check_script_process(script_list):
    for script in script_list:
        if script.process is None:
            continue

        if script.process.poll() is not None:
            script.process = None
            script.status = "Ready"


def end_script_process(script):
    if not script.process:
        return
    
    if script.process.poll() is not None:
        script.process = None
        script.status = "Ready"
        return

    script.process.terminate()

    try:
        script.process.wait(timeout=5)
    except subprocess.TimeoutExpired:
        script.process.kill()
        script.process.wait()

    script.process = None
    script.status = "Ready"