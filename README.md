# Script Manager

Local CLI script repository manager focused on scheduling, logging, and SHA256 integrity checks.

## App Architecture

Project structure and responsibility boundaries:

```text
C:.
│   .gitignore
│   config.ini
│   main.py
│   README.md
│   run.bat
│
├───data
│   │   scripts.db
│   │
│   ├───logs
│   │       app_logs.db
│   │       app_logs.txt
│   │       run_logs.db
│   │       run_logs.txt
│   │
│   └───scripts
│
└───script_manager
    │   __init__.py
    │
    ├───bootstrap
    │       bootstrap.py
    │       __init__.py
    │
    ├───logic
    │       config_loader.py
    │       db_loader.py
    │       db_operations.py
    │       directory_checker.py
    │       file_checker.py
    │       open_file.py
    │       runtime_views.py
    │       script_loader.py
    │       user_input.py
    │       __init__.py
    │
    └───menus
            menu_actions.py
            menu_content.py
            menu_controller.py
            menu_render.py
            __init__.py