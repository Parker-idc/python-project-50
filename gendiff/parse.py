import json
import yaml
import os


def get_data(file_path):
    if not os.path.isfile(file_path):
        raise ValueError(f"{file_path} - wrong file")
    _, format_name = os.path.splitext(os.path.normpath(file_path))
    with open(file_path, 'r') as file:
        return parse(file, format_name)


def parse(file_data, format_name):
    if format_name == ".json":
        return json.load(file_data)
    if format_name == ".yaml" or ".yml":
        return yaml.safe_load(file_data)
    raise ValueError(f"{format_name} - wrong format")
