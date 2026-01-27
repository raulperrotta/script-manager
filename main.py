from script_manager.bootstrap.bootstrap import initialize_app
from script_manager.menus.menu_controller import menu
import sys


def main():
    try:
        # initialize app
        app_data = initialize_app()

        # launch main menu        
        menu(app_data)
        
    # exit if app launch fails
    except Exception as error:
        print(f"ERROR: {error}")
        sys.exit(1)


if __name__ == "__main__":
    main()