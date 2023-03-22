# Generate difference

### Hexlet tests, linter status, code climate and test coverage :
[![Actions Status](https://github.com/Parker-idc/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/Parker-idc/python-project-50/actions)
<a href="https://codeclimate.com/github/Parker-idc/python-project-50/maintainability"><img src="https://api.codeclimate.com/v1/badges/bb1fb88528b23e27eae1/maintainability" /></a>
[![Test Coverage](https://api.codeclimate.com/v1/badges/bb1fb88528b23e27eae1/test_coverage)](https://codeclimate.com/github/Parker-idc/python-project-50/test_coverage)
[![Actions Status](https://github.com/Parker-idc/python-project-50/workflows/flake8/badge.svg)](https://github.com/Parker-idc/python-project-50/actions)
[![Actions Status](https://github.com/Parker-idc/python-project-50/workflows/pytest/badge.svg)](https://github.com/Parker-idc/python-project-50/actions)
___

### Description :

This is an educational project. 
It includes a command line utility that allows you to compare two .json or .yaml files and find data differences between them. In addition, the user can choose one of three output formats (stylish, plain, json) for differences.
___

### Installation :

1. Clone project.
```
git clone https://github.com/Parker-idc/python-project-50.git
```
```
pip install --user git+https://github.com/Parker-idc/python-project-50.git
```
2.  This project using Poetry, install it for next steps.
3.  Go to ur local directory with project and use `make build` command for creating the package.
4.  For installation use `python3 -m pip install --user dist/*.whl` command, or `make package-install`
___

### Commands :

`gendiff -f [format] file1 file2` command to get a difference between **file1** and **file2**
Select one of specific formats (**stylish**, **plain**, **json**) to get a corresponding output type.

`gendiff -h` command help.
___

### Examples with Stylish format:



#### Calculate diff in flat files(JSON)
[![calculate diff in flat files(JSON)](https://asciinema.org/a/9ePsOIDnpTzv5kzNZGuR0Ahhl.svg)](https://asciinema.org/a/9ePsOIDnpTzv5kzNZGuR0Ahhl)

#### Calculate diff in flat files(YAML)
[![calculate diff in flat files(YAML)](https://asciinema.org/a/QAqb65VqIGbt3F7VjMYzpbLFx.svg)](https://asciinema.org/a/QAqb65VqIGbt3F7VjMYzpbLFx)

