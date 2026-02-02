from ..menus import screen_render


def menu_input(state, app_data, BODIES, MENUS):
    # get the current menu size for input validation
    MENU_COUNT = len(MENUS[state["menu"]]["items"])

    while True:
        try:
            value = int(input(f"Select an option (1-{MENU_COUNT}): ").strip())
            if 1 <= value <= MENU_COUNT:
                return value
            else:
                screen_render.refresh_screen(state, app_data, BODIES, MENUS)
                print(f"Invalid input, enter a number between 1 and {MENU_COUNT}.")
        except ValueError:
            screen_render.refresh_screen(state, app_data, BODIES, MENUS)
            print(f"Invalid input, enter a number between 1 and {MENU_COUNT}.")   


def script_select_input(state, app_data, BODIES, MENUS):
    # get the total script count for input validation
    SCCRIPT_COUNT = len(app_data["scripts"])

    while True:
        try:
            value = int(input("Script ID: ").strip())
            if 0 <= value <= SCCRIPT_COUNT:
                return value
            else:
                screen_render.refresh_screen(state, app_data, BODIES, MENUS)
                print(f"Enter a number between 0 and {SCCRIPT_COUNT}")
        except ValueError:
            screen_render.refresh_screen(state, app_data, BODIES, MENUS)
            print(f"Enter a number between 0 and {SCCRIPT_COUNT}")


def file_input(state, app_data, BODIES, MENUS):
    # limit fiename size for input validation
    MAX_FILE_LEN = 18

    while True:
        value = input("Enter Filename: ").strip()
        if len(value) == 0:
            screen_render.refresh_screen(state, app_data, BODIES, MENUS)
            print("Name cannot be empty.")
        elif len(value) > MAX_FILE_LEN:
            screen_render.refresh_screen(state, app_data, BODIES, MENUS)
            print(f"Name must be {MAX_FILE_LEN} characters or fewer.")
        else:
            return value


def name_input(state, app_data, BODIES, MENUS):
    # limit name size for input validation
    MAX_NAME_LEN = 18

    while True:
        value = input("Enter Script Name: ").strip()
        if len(value) == 0:
            screen_render.refresh_screen(state, app_data, BODIES, MENUS)
            print("Name cannot be empty.")
        elif len(value) > MAX_NAME_LEN:
            screen_render.refresh_screen(state, app_data, BODIES, MENUS)
            print(f"Name must be {MAX_NAME_LEN} characters or fewer.")
        else:
            return value


def type_input(state, app_data, BODIES, MENUS):
    # dictionary for user to choose with int input
    SCRIPT_TYPES = {
        1: "Monitoring",
        2: "Utility",
        3: "Misc"
    }

    while True:
        try:
            selection = int(input("Select Script Type: ").strip())
            # 0 is used to cancel action
            if selection == 0:
                return "0"
            elif selection in SCRIPT_TYPES:
                return SCRIPT_TYPES[selection]
            else:
                screen_render.refresh_screen(state, app_data, BODIES, MENUS)
                print(f"Input must be a number between 0 and {len(SCRIPT_TYPES)}")
        except ValueError:
            screen_render.refresh_screen(state, app_data, BODIES, MENUS)
            print(f"Input must be a number between 0 and {len(SCRIPT_TYPES)}")


def desc_input(state, app_data, BODIES, MENUS):
    # limit description size for input validation
    MAX_DESC_LEN = 86

    while True:
        value = input("Enter Script Description: ").strip()
        if len(value) == 0:
            screen_render.refresh_screen(state, app_data, BODIES, MENUS)
            print("Name cannot be empty.")
        elif len(value) > MAX_DESC_LEN:
            screen_render.refresh_screen(state, app_data, BODIES, MENUS)
            print(f"Name must be {MAX_DESC_LEN} characters or fewer.")
        else:
            return value


def creation_confirm_input(state, app_data, BODIES, MENUS):
    while True:
        value = input("Create Script Entry?: ").strip().upper()
        if value in ("Y", "YES"):
            return True
        if value in ("N", "NO", "0"):
            return False
        screen_render.refresh_screen(state, app_data, BODIES, MENUS)
        print("Please Confirm or Cancel.")


def rehash_confirm_input(state, app_data, BODIES, MENUS):
    while True:
        value = input("Rehash Script?: ").strip().upper()
        if value in ("Y", "YES"):
            return True
        if value in ("N", "NO", "0"):
            return False
        screen_render.refresh_screen(state, app_data, BODIES, MENUS)
        print("Please Confirm or Cancel.")


def archive_confirm_input(state, app_data, BODIES, MENUS):
    while True:
        value = input("Archive Script?: ").strip().upper()
        if value in ("Y", "YES"):
            return True
        if value in ("N", "NO", "0"):
            return False
        screen_render.refresh_screen(state, app_data, BODIES, MENUS)
        print("Please Confirm or Cancel.")


def sort_input(state, app_data, BODIES, MENUS):
    # dictionary for user to choose with int input
    SORT_STYLE = {
        1: "id",
        2: "name",
        3: "platform",
        4: "type",
        5: "status",
        6: "last_run"
    }

    while True:
        try:
            selection = int(input("Select Sort Style: ").strip())
            # used to back from sort menu
            if selection == (len(SORT_STYLE) + 1):
                return "back"
            elif selection in SORT_STYLE:
                return SORT_STYLE[selection]
            else:
                screen_render.refresh_screen(state, app_data, BODIES, MENUS)
                print(f"Invalid input, enter a number between 1 and {len(SORT_STYLE) + 1}.")
        except ValueError:
            screen_render.refresh_screen(state, app_data, BODIES, MENUS)
            print(f"Invalid input, enter a number between 1 and {len(SORT_STYLE) + 1}.")





