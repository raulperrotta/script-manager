from script_manager.bootstrap.bootstrap import initialize_app
from script_manager.menus.screen_controller import menu
from script_manager.logic.script_exe import end_script_process
import sys


def main():
    try:
        app_data = initialize_app()
    except Exception as error:
        print(f"ERROR: {error}")
        sys.exit(1) 

    try:
        initial_state = {"body": "SCRIPTS", "menu": "MAIN"}
        menu(initial_state, app_data)

    finally:
        for script in app_data["scripts"]:
            if script.process:
                end_script_process(script)
                

if __name__ == "__main__":
    main()