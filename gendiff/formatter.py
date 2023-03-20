from gendiff.formats.json import format_to_json
from gendiff.formats.stylish import format_to_stylish
from gendiff.formats.plain import format_to_plain


def to_format(format_name, data):
    if format_name == 'json':
        return format_to_json(data)
    if format_name == 'plain':
        return format_to_plain(data)
    if format_name == 'stylish':
        return format_to_stylish(data)
