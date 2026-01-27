# Script Manager

Local CLI script repository manager focused on scheduling, logging, and SHA-256 integrity checks.

## Project Architecture

Structure and responsibility boundaries:

```
Root:
│   .gitignore
│   config.ini
│   main.py
│   README.md
│   run.bat
│
├───data
│   │   script_manager.db
│   │
│   ├───logs
│   │       app_logs.txt
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
    │       data_models.py
    │       db_loader.py
    │       db_operations.py
    │       directory_checker.py
    │       edit_script.py
    │       file_checker.py
    │       integrity_checker.py
    │       open_file.py
    │       run_script.py
    │       runtime_views.py
    │       user_input.py
    │       __init__.py
    │
    └───menus
            menu_actions.py
            menu_content.py
            menu_controller.py
            menu_render.py
            __init__.py
```
 Note: Data folder and files are generated during first launch.

## Libraries Used

### Standard Libraries

* [sys](https://docs.python.org/3/library/sys.html)
* [pathlib](https://docs.python.org/3/library/pathlib.html)
* [sqlite3](https://docs.python.org/3/library/sqlite3.html)
* [datetime](https://docs.python.org/3/library/datetime.html)
* [dataclasses](https://docs.python.org/3/library/dataclasses.html)
* [hashlib](https://docs.python.org/3/library/hashlib.html)

### External Libraries

 No third party libraries are used in this project.