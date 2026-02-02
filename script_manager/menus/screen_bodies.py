from ..logic import data_builder
from . import screen_render

# body swiches
def scripts_body(state, app_data):
    body_data = data_builder.build_script_body_items(app_data["scripts"], app_data["config"])
    return lambda: screen_render.render_scripts_table(body_data)


def script_details(state, app_data):
    body_data = data_builder.get_script_by_id(state["selected_script"], app_data["scripts"])
    return lambda: screen_render.render_script_details(body_data)


def script_logs(state, app_data):
    body_data = data_builder.get_logs_by_script_id(app_data["scripts"], state["selected_script"], app_data["run_logs"])
    return lambda: screen_render.render_run_logs_table(body_data)


def run_logs_body(state, app_data):
    body_data = data_builder.build_run_logs_body_items(app_data["scripts"], app_data["run_logs"])
    return lambda: screen_render.render_run_logs_table(body_data)


def app_logs_body(state, app_data):
    body_data = data_builder.build_app_logs_body_items(app_data["scripts"], app_data["app_logs"])
    return lambda: screen_render.render_app_logs_table(body_data)