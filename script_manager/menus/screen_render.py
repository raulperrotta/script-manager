import os
from script_manager.logic.config_loader import load_config


WIDTH = 100


def clear_console():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def render_screen(scripts, body, menu_items):
    clear_console()
    header_render()
    info_render(scripts)
    body_render(body)   
    menu_render(menu_items)


def header_render():
    config = load_config()
    app_name = config["app"]["app_name"]

    print("=" * WIDTH)
    print(app_name.center(WIDTH))
    print("=" * WIDTH)


def info_render(scripts):
    trusted, modified, running = 0, 0, 0

    for script in scripts:
        if not script.archived:
            if script.status == "Ready":
                trusted += 1
            elif script.status == "Running":
                trusted += 1
                running += 1
            else:
                modified += 1

    processes = f"Trusted Scripts: {trusted} | Modified: {modified} | Running: {running}"

    print(processes.center(WIDTH))
    print("-" * WIDTH)


def body_render(body):
    body()
    print("-" * WIDTH)


def menu_render(menu_items):
    print("-" * WIDTH)
    menu_line = " | ".join(menu_items)
    print(menu_line.center(WIDTH))
    print("-" * WIDTH)


# menu redrawing
def refresh_screen(state, app_data, BODIES, MENUS):
    body = BODIES[state["body"]](state, app_data)
    menu = MENUS[state["menu"]]
    render_screen(app_data["scripts"], body, menu["items"])


def render_scripts_table(scripts):
    if not scripts:
        print("No scripts to display.")
        return

    headers = {
        "ID": 4,
        "Name": 20,
        "Platform": 12,
        "Type": 12,
        "Status": 16,
        "Last Run": 20
    }

    header_columns = []
    for header_name, header_width in headers.items():
        header_columns.append(header_name.ljust(header_width))
    print( " | ".join(header_columns))
    print("-" * WIDTH )

    for script in scripts:
        script_entry = [
            str(script.get("id", "-")).ljust(headers["ID"]),
            str(script.get("name", "-")).ljust(headers["Name"]),
            str(script.get("platform", "-")).ljust(headers["Platform"]),
            str(script.get("type", "-")).ljust(headers["Type"]),
            str(script.get("status", "-")).ljust(headers["Status"]),
            str(script.get("last_run", "-")).ljust(headers["Last Run"])
        ]
        print(" | ".join(script_entry))


def render_script_details(script):
    label_width=12

    display_model = [
        ("ID", "id"),
        ("Name", "name"),
        ("Type", "type"),
        ("Status", "status"),
        ("Last Run", "last_run"),
        ("Path", "path"),
        ("Run Count", "run_count"),
        ("Description", "desc"),
    ]

    for field_name, object_reference in display_model:
        field_data = getattr(script, object_reference, "-")
        print(f"{field_name.ljust(label_width)}: {field_data}")


def render_run_logs_table(run_logs):
    if not run_logs:
        print("No logs to display.")
        return

    headers = {
        "Run Date": 20,
        "Script ID": 10,
        "Script Name": 20,
        "Host Name": 20,
        "Host ID": 20
    }

    header_columns = []
    for header_name, header_width in headers.items():
        header_columns.append(header_name.ljust(header_width))
    print( " | ".join(header_columns))
    print("-" * WIDTH )

    for log in run_logs:
        log_entry = [
            str(log.get("run_date", "-")).ljust(headers["Run Date"]),
            str(log.get("script_id", "-")).ljust(headers["Script ID"]),
            str(log.get("script_name", "-")).ljust(headers["Script Name"]),
            str(log.get("host_name", "-")).ljust(headers["Host Name"]),
            str(log.get("host_id", "-")).ljust(headers["Host ID"])
        ]
        print(" | ".join(log_entry))


def render_app_logs_table(app_logs):
    if not app_logs:
        print("No App Logs to display.")
        return

    headers = {
        "Date": 20,
        "Type": 10,
        "Code": 20,
        "Script ID": 20,
        "Script Name": 20
    }

    header_columns = []
    for header_name, header_width in headers.items():
        header_columns.append(header_name.ljust(header_width)) 
    print( " | ".join(header_columns))
    print("-" * WIDTH )

    for log in app_logs:
        log_entry = [
            str(log.get("date", "-")).ljust(headers["Date"]),
            str(log.get("type", "-")).ljust(headers["Type"]),
            str(log.get("code", "-")).ljust(headers["Code"]),
            str(log.get("script_id", "-")).ljust(headers["Script ID"]),
            str(log.get("script_name", "-")).ljust(headers["Script Name"])
        ]
        print(" | ".join(log_entry))

