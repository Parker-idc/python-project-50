import json
import yaml
import os


def get_data(file):
    with open(file, 'r') as f:
        return parse(f, get_format_name(file))


def get_format_name(file_path):
    if not os.path.isfile(file_path):
        raise ValueError(f"{file_path} - not a file")
    _, format_name = os.path.splitext(os.path.normpath(file_path))
    return format_name


def parse(file_data, format_name):
    if format_name == ".json":
        return json.load(file_data)
    if format_name == ".yaml" or ".yml":
        return yaml.safe_load(file_data)
    raise ValueError(f"{format_name} - wrong format")
