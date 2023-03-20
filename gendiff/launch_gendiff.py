from gendiff.parse import get_data
from gendiff.diff_tree import get_diff_tree
from gendiff.formatter import to_format


def generate_diff(file_path1, file_path2, formatter='stylish'):
    first_file = get_data(file_path1)
    second_file = get_data(file_path2)
    diff = get_diff_tree(first_file, second_file)
    result = to_format(formatter, diff)
    return result
