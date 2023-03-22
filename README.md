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
[![calculate diff in flat files(JSON)](https://asciinema.org/a/IMZrWvtiryoJmE07iRxnTNOK8.svg)](https://asciinema.org/a/IMZrWvtiryoJmE07iRxnTNOK8)

#### Calculate diff in flat files(YAML)
[![calculate diff in flat files(YAML)](https://asciinema.org/a/Q35QP9kjFkvwFjiqU6zidPBeB.svg)](https://asciinema.org/a/Q35QP9kjFkvwFjiqU6zidPBeB)

#### Calculate diff in recursive files(JSON)
[![calculate diff in recursive files(JSON)](https://asciinema.org/a/oow2zLVCiHMaiWH35qvE7zuD1.svg)](https://asciinema.org/a/oow2zLVCiHMaiWH35qvE7zuD1)

#### Calculate diff in recursive files(YAML)
[![calculate diff in recursive files(YAML)](https://asciinema.org/a/3Dxjqzko4qlAr3dHtj5nQgMxd.svg)](https://asciinema.org/a/3Dxjqzko4qlAr3dHtj5nQgMxd)




### Examples with Plain format:


#### Calculate diff in flat files(JSON)
[![calculate diff in flat files(JSON)](https://asciinema.org/a/yxk2xbZ2l1Is2MwOMQCIFWWlk.svg)](https://asciinema.org/a/yxk2xbZ2l1Is2MwOMQCIFWWlk)

#### Calculate diff in flat files(YAML)
[![calculate diff in flat files(YAML)](https://asciinema.org/a/jQ9WxLuIE9y15Emta4YMx1xde.svg)](https://asciinema.org/a/jQ9WxLuIE9y15Emta4YMx1xde)

#### Calculate diff in recursive files(JSON)
[![calculate diff in recursive files(JSON)](https://asciinema.org/a/MwkafKpzCqn2V7cuYWU3d6cLp.svg)](https://asciinema.org/a/MwkafKpzCqn2V7cuYWU3d6cLp)

#### Calculate diff in recursive files(YAML)
[![calculate diff in recursive files(YAML)](https://asciinema.org/a/UIQlnsgl4PzKN40CMODzpc4Aa.svg)](https://asciinema.org/a/UIQlnsgl4PzKN40CMODzpc4Aa)


### Examples with Json format:


#### Calculate diff in flat files(JSON)
[![calculate diff in flat files(JSON)](https://asciinema.org/a/qjQwgBbrSpICx8T80l4NJF8Zm.svg)](https://asciinema.org/a/qjQwgBbrSpICx8T80l4NJF8Zm)

#### Calculate diff in flat files(YAML)
[![calculate diff in flat files(YAML)](https://asciinema.org/a/zKSJ3kurF1yxwUMvm8qqWx2OB.svg)](https://asciinema.org/a/zKSJ3kurF1yxwUMvm8qqWx2OB)

#### Calculate diff in recursive files(JSON)
[![calculate diff in recursive files(JSON)](https://asciinema.org/a/KhMahOLOLYKl8N936UJS2HFxT.svg)](https://asciinema.org/a/KhMahOLOLYKl8N936UJS2HFxT)

#### Calculate diff in recursive files(YAML)
[![calculate diff in recursive files(YAML)](https://asciinema.org/a/Cs4CuT9WejhLobfEqkFnrCY6j.svg)](https://asciinema.org/a/Cs4CuT9WejhLobfEqkFnrCY6j)



