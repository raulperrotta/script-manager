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
└───script_manager
    │   __init__.py
    │
    ├───bootstrap
    │       bootstrap.py
    │       config_loader.py
    │       db_checker.py
    │       directory_checker.py
    │       file_checker.py
    │       __init__.py
    │
    ├───logic
    │       data_builder.py
    │       data_models.py
    │       db_loader.py
    │       integrity_checker.py
    │       log_creation.py
    │       open_file.py
    │       script_editing.py
    │       script_entry_creation.py
    │       script_exe.py
    │       set_sort_style.py
    │       user_input.py
    │       __init__.py
    │
    └───menus
            menu_actions.py
            screen_bodies.py
            screen_content.py
            screen_controller.py
            screen_render.py
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
* [os](https://docs.python.org/3/library/os.html)
* [shutil](https://docs.python.org/3/library/shutil.html)


### External Libraries

 No third party libraries are used in this project.