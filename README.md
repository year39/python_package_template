---
id: python-package-template
title: Python Package Template
tags: [python]
created: 12/23/2020
updated: 02/04/2023
excerpt: This is a simple Python package/project template with unit tests and setuptools.
readTime: 5 minutes
---

# Project structure

For more details, follow this excellent [guide](https://packaging.python.org/en/latest/tutorials/packaging-projects/).

```
.
├── hello_python: package name
│   ├── subpackage: an example of a sub-package
│   │   ├── __init__.py: declare package directory
│   │   └── math.py: sub-package source file
│   ├── config: an example of a config directory, verify it gets packaged
│   │   └── system_config.yaml: a useless config file for demo purpose
│   ├── __init__.py: declare package directory
│   ├── read_config.py: package source file
├── LICENSE.txt: license file
├── pyproject.toml: contains build system requirements
├── README.md: Read me file
├── requirements.txt: install requirements
├── setup.cfg: Setuptools configuration file
└── tests: unit test directory
    ├── __init__.py: declare a package
    └── test_simple.py: unit test
```

# Install requirements

```sh
pip install -r requirements.txt
```

# Unit tests

```
pytest

#Output:

============================= test session starts ==============================
platform linux -- Python 3.10.8, pytest-7.1.2, pluggy-1.0.0
rootdir: /python_package_template
plugins: cov-4.0.0
collected 1 item

tests/test_simple.py .                                                   [100%]

============================== 1 passed in 0.01s ===============================
```

# Build

```sh
python -m build

# output:

...
adding 'hello_python/__init__.py'
adding 'hello_python/read_config.py'
adding 'hello_python/subpackage/__init__.py'
adding 'hello_python/subpackage/math.py'
adding 'hello_python/config/system_config.yaml'
adding 'hello_python-1.0.0.dist-info/LICENSE.txt'
adding 'hello_python-1.0.0.dist-info/METADATA'
adding 'hello_python-1.0.0.dist-info/WHEEL'
adding 'hello_python-1.0.0.dist-info/entry_points.txt'
adding 'hello_python-1.0.0.dist-info/top_level.txt'
adding 'hello_python-1.0.0.dist-info/RECORD'
removing build/bdist.linux-x86_64/wheel
Successfully built hello_python-1.0.0.tar.gz and hello_python-1.0.0-py3-none-any.whl

```

# .whl package

`.whl` is the standard Python packaging and it's essentially an archive contains
the package files and metadata.

After a successful build, the packaging is now inside `dist/` directory.

```sh
ls dist/
hello_python-1.0.0-py3-none-any.whl  hello_python-1.0.0.tar.gz
```

The `.whl` is the Python package distribution, and the `.tar.gz` is the source
code distribution.

# Install the package

Install the package from the package source code:

```sh
python -m pip install .
```

Or, install the `.whl` package:

```sh
pip install <package-name>.whl
```

Output:

```sh
Installing build dependencies ... done
Getting requirements to build wheel ... done
Preparing metadata (pyproject.toml) ... done
Requirement already satisfied: pyyaml in /miniconda3/lib/python3.10/site-packages (from hello-python==1.0.0) (6.0)
Requirement already satisfied: urllib3>=1.2 in /miniconda3/lib/python3.10/site-packages (from hello-python==1.0.0) (1.26.8)
Building wheels for collected packages: hello-python
  Building wheel for hello-python (pyproject.toml) ... done
  Created wheel for hello-python: filename=hello_python-1.0.0-py3-none-any.whl size=6630 sha256=e05c8ef68a30155d0abd460298c7aa048e791665f7ad415aed5a93ef9ce3422c
  Stored in directory: /tmp/pip-ephem-wheel-cache-mk7guazo/wheels/a8/54/30/59f8f2c784a00deb52cc2d376d20fe75663b99a46643193de7
Successfully built hello-python
Installing collected packages: hello-python
Successfully installed hello-python-1.0.0
```

# Verify the contents of the installed package

To verify resources are available after installing the package, run `python`
command to enter the `REPL` and import and inspect the package:

```python
Python 3.9.7 (default, Sep 16 2021, 13:09:58)
[GCC 7.5.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import hello_python
>>> import importlib.resources
>>> list(importlib.resources.contents('hello_python'))
['subpackage', 'config', '__init__.py', '__pycache__', 'read_config.py']
>>>
>>> from hello_python.read_config import print_config
>>> print_config()
controller:
  address: 192.168.1.10
  sim: true
network:
  data_uri:
  - http://127.0.0.1:3000/
>>> from hello_python.subpackage.math import add_two
>>> add_two(1, 5)
6
>>>
```

You can see all the package related files exist including the
`config/system_config.yaml` file and `subpackage` directory.
