# CDL python package tutorial
This tutorial shows how to create a CDL-approved python package and how to generate documentation using sphinx.

# Table of contents
- [Getting started](#getting-started)
- [Basic structure](#basic-structure)

## Getting started
[](#){name=getting-started}

1. Pull latest from CDL-tutorials repo
2. Navigate to the example_package folder and run `pip install -e .`. This will install an editable installation of the package so you can modify it.

## Basic structure
[](#){name=basic-structure}

The basic structure for a CDL Python package looks like this:
```
README.md                          # documentation about the package
LICENSE                            # license file (typically MIT)
setup.py                           # python package config file
requirements.txt                   # text file containing software dependencies

<name of package>/__init__.py      # file indicating that this folder is a module
<name of package>/core.py          # file containing essential code
<name of package>/helpers.py       # file containing helper functions

docs/conf.py                       # file for configuring documentation with sphinx
docs/index.rst                     # file to generate index.html on doc website
docs/api.rst                       # file to specify API on doc website
docs/tutorial/notebook.ipynb       # file to specify API on doc website
docs/tutorial/tools/nb_to_doc.py   # file to specify API on doc website

tests/test_basic.py                # basic tests for package
tests/test_advanced.py             # more advanced tests
```
These are the minimum files needed to create a CDL python package. \
Below we'll go into more depth on each of these components

##
