from pathlib import Path
from configparser import ConfigParser


def update_sorting(config, sort_style):
    if sort_style == config["settings"]["sort_style"]:
        reverse_sorting(config)
    else:
        update_sort_style(config, sort_style)
  

def update_sort_style(config, sort_style):
    config_path = Path("config.ini")

    config_file = ConfigParser()
    config_file.read(config_path)

    config["settings"]["sort_style"] = sort_style
    config_file["settings"]["sort_style"] = sort_style

    with config_path.open("w") as file:
        config_file.write(file)


def reverse_sorting(config):
    config_path = Path("config.ini")

    config_file = ConfigParser()
    config_file.read(config_path)

    current_order = config["settings"]["sort_reverse"]
  
    if current_order == "True":
        config["settings"]["sort_reverse"] = "False"
        config_file["settings"]["sort_reverse"] = "False"

    else:
        config["settings"]["sort_reverse"] = "True"
        config_file["settings"]["sort_reverse"] = "True"
   
    with config_path.open("w") as file:
        config_file.write(file)