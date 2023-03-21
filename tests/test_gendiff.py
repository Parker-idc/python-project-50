from gendiff import generate_diff
import pytest
import os

test_cases = [
    ("flat1.json", "flat2.json", "result/flat_stylish.txt", "stylish"),
    ("flat1.yaml", "flat2.yaml", "result/flat_stylish.txt", "stylish"),
    ("recursive1.json", "recursive2.json", "result/recursive_stylish.txt", "stylish"),
    ("recursive1.yaml", "recursive2.yaml", "result/recursive_stylish.txt", "stylish"),
    ("flat1.json", "flat2.json", "result/flat_plain.txt", "plain"),
    ("flat1.yaml", "flat2.yaml", "result/flat_plain.txt", "plain"),
    ("recursive1.json", "recursive2.json", "result/recursive_plain.txt", "plain"),
    ("recursive1.yaml", "recursive2.yaml", "result/recursive_plain.txt", "plain"),
    ("flat1.json", "flat2.json", "result/flat_json.txt", "json"),
    ("flat1.yaml", "flat2.yaml", "result/flat_json.txt", "json"),
    ("recursive1.json", "recursive2.json", "result/recursive_json.txt", "json"),
    ("recursive1.yaml", "recursive2.yaml", "result/recursive_json.txt", "json")
]


def get_fixture_path(filename):
    return os.path.join('tests/fixtures', filename)


@pytest.mark.parametrize("file1, file2, result, formatter", test_cases)
def test_universal_case(file1, file2, result, formatter):
    with open(get_fixture_path(result), 'r') as res:
        result_content = "\n".join(res.read().splitlines())
    assert generate_diff(
        get_fixture_path(file1),
        get_fixture_path(file2),
        formatter) == result_content
