from ..logic import user_input
from ..logic import set_sort_style
from ..logic import script_entry_creation
from . import screen_render
import sys


def main(state, app_data, BODIES, MENUS):
    state.update({"body": "SCRIPTS", "menu": "MAIN"})


def manage(state, app_data, BODIES, MENUS):
    state.update({"body": "SCRIPTS", "menu": "MANAGE"})


def select(state, app_data, BODIES, MENUS):
    state.update({"body": "SCRIPTS", "menu": "SELECT"})
    screen_render.refresh_screen(state, app_data, BODIES, MENUS)
    state["selected_script"] = user_input.script_select_input(state, app_data, BODIES, MENUS)
    if state["selected_script"] == 0:
        state.update({"body": "SCRIPTS", "menu": "MANAGE"})
    else:
        state.update({"body": "DETAILS", "menu": "DETAILS"})


def details(state, app_data, BODIES, MENUS):
    state.update({"body": "DETAILS", "menu": "DETAILS"})


def run(state, app_data, BODIES, MENUS):
    state.update({"body": "DETAILS", "menu": "DETAILS"})


def edit(state, app_data, BODIES, MENUS):
    state.update({"body": "DETAILS", "menu": "EDIT"})


def edit_name(state, app_data, BODIES, MENUS):  
    state.update({"body": "ADD", "menu": "EDIT_NAME"})
    screen_render.refresh_screen(state, app_data, BODIES, MENUS)
    new_script_name = user_input.file_input(state, app_data, BODIES, MENUS)
    if new_script_name != "0":
        # edit name script function
        pass
    state.update({"body": "DETAILS", "menu": "EDIT"})


def edit_desc(state, app_data, BODIES, MENUS):
    state.update({"body": "ADD", "menu": "EDIT_DESC"})
    screen_render.refresh_screen(state, app_data, BODIES, MENUS)
    new_script_desc = user_input.desc_input(state, app_data, BODIES, MENUS)
    if new_script_desc != "0":
        # edit desc script function
        pass
    state.update({"body": "DETAILS", "menu": "EDIT"})


def edit_type(state, app_data, BODIES, MENUS):
    state.update({"body": "ADD", "menu": "EDIT_TYPE"})
    screen_render.refresh_screen(state, app_data, BODIES, MENUS)
    new_script_type = user_input.type_input(state, app_data, BODIES, MENUS)
    if new_script_type != "0":
        # edit type script function
        pass
    state.update({"body": "DETAILS", "menu": "EDIT"})


def rehash(state, app_data, BODIES, MENUS):
    state.update({"body": "ADD", "menu": "REHASH"})
    screen_render.refresh_screen(state, app_data, BODIES, MENUS)
    rehash_choice = user_input.rehash_confirm_input(state, app_data, BODIES, MENUS)
    if rehash_choice == True:
        # rehash script function
        pass
    state.update({"body": "DETAILS", "menu": "EDIT"})


def archive(state, app_data, BODIES, MENUS):
    state.update({"body": "ADD", "menu": "ARCHIVE"})
    screen_render.refresh_screen(state, app_data, BODIES, MENUS)
    archive_choice = user_input.archive_confirm_input(state, app_data, BODIES, MENUS)
    if archive_choice == True:
        # archive script function
        pass
    state.update({"body": "DETAILS", "menu": "EDIT"})


def script_logs(state, app_data, BODIES, MENUS):
    state.update({"body": "SCRIPT_LOGS", "menu": "SCRIPT_LOGS"})


def open_script(state, app_data, BODIES, MENUS):
    state.update({"body": "DETAILS", "menu": "DETAILS"})


def sort(state, app_data, BODIES, MENUS):
    while True:
        state.update({"body": "SCRIPTS", "menu": "SORT"})
        screen_render.refresh_screen(state, app_data, BODIES, MENUS)
        sort_choice = user_input.sort_input(state, app_data, BODIES, MENUS)
        if sort_choice == "back":
            break
        set_sort_style.update_sorting(app_data["config"], sort_choice)
    state.update({"body": "SCRIPTS", "menu": "MANAGE"})


def add(state, app_data, BODIES, MENUS):
    
    script_count = len(app_data["scripts"])

    if script_count != 0:
        latest_script = app_data["scripts"][script_count - 1]
        NEW_SCRIPT_ID = latest_script.id + 1
    else:
        NEW_SCRIPT_ID = 1

    state["selected_script"] = NEW_SCRIPT_ID

    script_entry_creation.create_new_script(state, app_data, BODIES, MENUS, NEW_SCRIPT_ID)

    state.update({"body": "SCRIPTS", "menu": "MANAGE"})


def run_logs(state, app_data, BODIES, MENUS):
    state.update({"body": "RUN_LOGS", "menu": "RUN_LOGS"})


def open_run_log_file(state, app_data, BODIES, MENUS):
    state.update({"body": "RUN_LOGS", "menu": "RUN_LOGS"})


def app_logs(state, app_data, BODIES, MENUS):
    state.update({"body": "APP_LOGS", "menu": "APP_LOGS"})


def open_app_log_file(state, app_data, BODIES, MENUS):
    state.update({"body": "APP_LOGS", "menu": "APP_LOGS"})


def exit(state, app_data, BODIES, MENUS):
    sys.exit(1)