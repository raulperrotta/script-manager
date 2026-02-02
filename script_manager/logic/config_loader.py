from script_manager.logic.data_models import CONFIG_FORMAT
from configparser import ConfigParser
from configparser import ExtendedInterpolation
from pathlib import Path
import sys


def load_config():
    config_path = Path("config.ini")

    if not config_path.exists():
        print("ERROR: config.ini Not Found")
        sys.exit(1)
    
    config = ConfigParser(interpolation = ExtendedInterpolation())

    # read the file with parsing and interpolation
    try:
        with config_path.open() as file:
            config.read_file(file)

    except Exception as error:
        print(f"ERROR: {error}")
        sys.exit(1)

    validate_config(config)

    return config


def validate_config(config: ConfigParser):
    # compares config file with expected data model
    for section, options in CONFIG_FORMAT.items():
        if section not in config:
            print(f"ERROR: missing config section [{section}]")
            sys.exit(1)

        for option in options:
            if option not in config[section]:
                print(f"ERROR: missing config option '{option}' in [{section}]")
                sys.exit(1)

    # verifies interpolation resolution
    try:
        for section in config.sections():
            for option in config[section]:
                config.get(section, option)

    except Exception as error:
        print(f"ERROR: {error}")
        sys.exit(1)
