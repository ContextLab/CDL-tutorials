# CDL python package tutorial
This tutorial shows how to create a CDL-approved python package and how to generate documentation using sphinx.

# Table of contents
- [Getting started](#getting-started)
- [Basic structure](#basic-structure-of-a-project)
  * [The README](#the-readme)

## Getting started
1. Pull latest from CDL-tutorials repo
2. Navigate to the example_package folder and run `pip install -e .`. This will install an editable installation of the package so you can modify it.

## Basic structure of a project
The basic structure for a CDL Python package looks like this:
```
README.md                          # documentation about the package
LICENSE                            # license file (typically MIT)
CONTRIBUTING.md                    # file containing instructions for contributing
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

### The README
While often tedious to create, this is one of the most important files in a software project.  It provides a roadmap for users to install, utilize and contribute to your project. Even the best code without proper documentation is effectively useless. A CDL-approved README should contain the following information:

- Overview - A plain english high level overview of what your package does
- Try it - A link to a Binder notebook that allows potential users to quickly try out the package
- Installation - A section detailing how the package can be installed
- Requirements - A full list of software dependencies
- Citing - Information on how to reference the software
- Contributing - A link to a [Code of Conduct](https://www.mozilla.org/en-US/about/governance/policies/participation/), and a link to the CONTRIBUTING.md file
- Testing - Instructions on how to test the package
- Examples - Pictoral and/or code examples of the package in action
