from . import menu_actions
from . import screen_bodies


BODIES = {
    "SCRIPTS": screen_bodies.scripts_body,
    "DETAILS": screen_bodies.script_details,
    "SCRIPT_LOGS": screen_bodies.script_logs,
    "RUN_LOGS": screen_bodies.run_logs_body,
    "APP_LOGS": screen_bodies.app_logs_body,
    "ADD": screen_bodies.script_details #to do: create temp obj display
}


MENUS = {
    "MAIN": {
        "items": ["[1] Manage", "[2] Logs", "[3] Exit"],
        "actions": {
            1: menu_actions.manage,
            2: menu_actions.run_logs,
            3: menu_actions.exit
        }
    },
    "MANAGE": {
        "items": ["[1] Select", "[2] Sort", "[3] Add", "[4] Back"],
        "actions": {
            1: menu_actions.select,
            2: menu_actions.sort,
            3: menu_actions.add,
            4: menu_actions.main
        }
    },
    "SELECT": {
        "items": ["Enter Script ID", "[0] Cancel"],
        "actions": {
            1: menu_actions.select,
            2: menu_actions.manage
        }
    },
    "DETAILS": {
        "items": ["[1] Run", "[2] Edit", "[3] Script Logs", "[4] Open", "[5] Back"],
        "actions": {
            1: menu_actions.run,
            2: menu_actions.edit,
            3: menu_actions.script_logs,
            4: menu_actions.open_script,
            5: menu_actions.manage
        }
    },
    "RUN_SUCCESS": {
        "items": ["Script Started"],
        "actions": {
            1: menu_actions.details,
        }
    },
    "RUN_FAIL": {
        "items": ["Script Cannot Run. Please Check Path and SHA-256 Validation."],
        "actions": {
            1: menu_actions.details,
        }
    },
    "EDIT": {
        "items": ["[1] Name", "[2] Desc", "[3] Type", "[4] Rehash", "[5] Archive", "[6] Back"],
        "actions": {
            1: menu_actions.edit_name,
            2: menu_actions.edit_desc,
            3: menu_actions.edit_type,
            4: menu_actions.rehash,
            5: menu_actions.archive,
            6: menu_actions.details
        }
    },
    "EDIT_NAME": {
        "items": ["New Script Name | [0] Cancel"],
        "actions": {
            1: None
        }
    },
    "EDIT_DESC": {
        "items": ["New Script Description | [0] Cancel"],
        "actions": {
            1: None
        }
    },
    "EDIT_TYPE": {
        "items": ["New Script Type: [1] Monitoring | [2] Utility | [3] Misc. | [0] Cancel"],
        "actions": {
            1: None
        }
    },
    "REHASH": {
        "items": ["Rehash Script? (Y/N) | [0] Cancel"],
        "actions": {
            1: None
        }
    },
    "ARCHIVE": {
        "items": ["Archive Script? (Y/N) | [0] Cancel"],
        "actions": {
            1: None
        }
    },
    "SCRIPT_LOGS": {
        "items": ["[1] Back"],
        "actions": {
            1: menu_actions.details
        }
    },
    "SORT": {
        "items": ["[1] ID | [2] Name | [3] Platform | [4] Type | [5] Status | [6] Last Run | [7] Back"],
        "actions": {
            1: None
        }
    },
    "ADD_FILE": {
        "items": ["Enter Script Filename | [0] Cancel"],
        "actions": {
            1: None
        }
    },
    "ADD_NAME": {
        "items": ["Enter Script Name | [0] Cancel"],
        "actions": {
            1: None
        }
    },
    "ADD_TYPE": {
        "items": ["Select Script Type:[1] Monitoring | [2] Utility | [3] Misc. | [0] Cancel"],
        "actions": {
            1: None
        }
    },
    "ADD_DESC": {
        "items": ["Enter Script Description | [0] Cancel"],
        "actions": {
            1: None
        }
    },
    "ADD_CONFIRM": {
        "items": ["Confirm (Y/N) | [0] Cancel"],
        "actions": {
            1: None
        }
    },
    "RUN_LOGS": {
        "items": ["[1] Open TXT", "[2] View App Logs", "[3] Back"],
        "actions": {
            1: menu_actions.open_run_log_file,
            2: menu_actions.app_logs,
            3: menu_actions.main
        }
    },
    "APP_LOGS": {
        "items": ["[1] Open TXT", "[2] View Run Logs", "[3] Back"],
        "actions": {
            1: menu_actions.open_app_log_file,
            2: menu_actions.run_logs,
            3: menu_actions.main
        }
    }    
}