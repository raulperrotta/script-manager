def build_script_body_items(scripts, config):
    # get filtered script list
    script_list = [
        {
            "id": script.id,
            "name": script.name,
            "platform": script.platform,
            "type": script.type,
            "status": script.status,
            "last_run": (script.last_run.strftime("%Y-%m-%d %H:%M") if script.last_run else "-")
        }
        for script in scripts
        if not script.archived
    ]

   # get stort style and order and apply to list 
    sort_style = config["settings"]["sort_style"]
    sort_order = config["settings"]["sort_reverse"]

    sorted_scripts = sorted(
        script_list,
        key=lambda x: x[sort_style] or "",
        reverse=(sort_order == "True")
    )

    return sorted_scripts


def get_script_by_id(script_id, script_list):
    for script in script_list:
        if script.id == script_id:
            return script


def get_logs_by_script_id(scripts, script_id, run_logs):
    # limit number of logs to number of active scripts
    limit = len([script for script in scripts if not script.archived])

    # get filtered log list
    script_logs = [
        {
            "run_date": log.run_date.strftime("%Y-%m-%d %H:%M"),
            "script_id": log.script_id,
            "script_name": log.script_name,
            "host_name": log.host_name,
            "host_id": log.host_id,
        }
        for log in run_logs
        if log.script_id == script_id
    ]

    # sort by run date
    sorted_logs = sorted(
        script_logs,
        key=lambda log: log["run_date"],
        reverse=True
    )

    return sorted_logs[:limit]


def build_app_logs_body_items(scripts, app_logs):
    # limit number of logs to number of active scripts
    limit = len([script for script in scripts if not script.archived])

    # get app log list
    app_logs = [
        {
            "date": log.date.strftime("%Y-%m-%d %H:%M"),
            "type": log.type,
            "code": log.code,
            "script_id": log.script_id,
            "script_name": log.script_name,
            "old_data": log.old_data,
            "new_data": log.new_data,
        }
        for log in app_logs
    ]
    
    # sort by log date
    sorted_logs = sorted(
        app_logs,
        key=lambda log: log["date"],
        reverse=True
    )

    return sorted_logs[:limit]


def build_run_logs_body_items(scripts, run_logs):
    # limit number of logs to number of active scripts
    limit = len([script for script in scripts if not script.archived])

    # get run log list
    run_logs = [
        {
            "run_date": log.run_date.strftime("%Y-%m-%d %H:%M"),
            "script_id": log.script_id,
            "script_name": log.script_name,
            "host_name": log.host_name,
            "host_id": log.host_id,
        }
        for log in run_logs
    ]
    
    # sort by run date
    sorted_logs = sorted(
        run_logs,
        key=lambda log: log["run_date"],
        reverse=True
    )

    return sorted_logs[:limit]