from script_manager.logic.config_loader import load_config
from script_manager.logic.directory_checker import validate_directories
from script_manager.logic.file_checker import validate_files
from script_manager.logic.db_loader import database_loader


def initialize_app():
    # load config
    config = load_config()

    # create / validate directories
    validate_directories(config)

    # create / validate files
    validate_files(config)

    # load database into memory
    script_list, run_log_list, app_log_list = database_loader(config["files"]["app_db"])

    # return app data main app
    return {
        "config": config,
        "scripts": script_list,
        "run_logs": run_log_list,
        "app_logs": app_log_list
    }
