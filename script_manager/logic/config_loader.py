from script_manager.logic.data_models import CONFIG_FORMAT
from configparser import ConfigParser
from configparser import ExtendedInterpolation
from pathlib import Path
import sys


def load_config():
    # set config path
    config_path = Path("config.ini")

    # exits if config file is not found
    if not config_path.exists():
        print("ERROR: config.ini Not Found")
        sys.exit(1)
    
    # sets parsing and interpolation
    config = ConfigParser(interpolation = ExtendedInterpolation())

    # read the file
    try:
        with config_path.open() as file:
            config.read_file(file)

    # exit if file reading fails
    except Exception as error:
        print(f"ERROR: {error}")
        sys.exit(1)

    # config.ini format validation
    validate_config(config)

    return config


def validate_config(config: ConfigParser):
    #checks if sections and options match intended format
    for section, options in CONFIG_FORMAT.items():
        if section not in config:
            print(f"ERROR: missing config section [{section}]")
            sys.exit(1)

        for option in options:
            if option not in config[section]:
                print(f"ERROR: missing config option '{option}' in [{section}]")
                sys.exit(1)

    # validates interpolation resolution
    try:
        for section in config.sections():
            for option in config[section]:
                config.get(section, option)
    except Exception as error:
        print(f"ERROR: {error}")
        sys.exit(1)
