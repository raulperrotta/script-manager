from .screen_render import render_screen
from script_manager.logic.user_input import menu_input
from .screen_content import MENUS, BODIES


def menu(state, app_data):
    while True:
        body = BODIES[state["body"]](state, app_data)
        menu = MENUS[state["menu"]]

        render_screen(app_data["scripts"], body, menu["items"])

        selection = menu_input(state, app_data, BODIES, MENUS)
        action = menu["actions"].get(selection)
        action(state, app_data, BODIES, MENUS)