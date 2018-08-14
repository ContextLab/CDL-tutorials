# CDL python package tutorial
This tutorial shows how to create a CDL-approved python package and how to generate documentation using sphinx.

# Table of contents
- [Getting started](#getting-started)
- [Basic structure](#basic-structure-of-a-project)
- [The essentials](the-essentials)
  * [README.md](#readmemd)
  * [LICENSE](#license)
  * [CONTRIBUTING.md](#contributingmd)
  * [setup.py](#setuppy)
  * [requirements.txt](#requirementstxt)
- [Documentation](#documentation)
  * [`sphinx`](#sphinx)

## Getting started
1. Pull latest from CDL-tutorials repo
2. Navigate to the example_package folder and run `pip install -e .`. This will install an editable installation of the package so you can modify it.

## Basic structure of a project
The basic structure for a CDL Python package looks like this:
```
# essentials
README.md                          # documentation about the package
LICENSE                            # license file (typically MIT)
CONTRIBUTING.md                    # file containing instructions for contributing
setup.py                           # python package config file
requirements.txt                   # text file containing software dependencies

# documentation
docs/conf.py                       # file for configuring documentation with sphinx
docs/index.rst                     # file to generate index.html on doc website
docs/api.rst                       # file to specify API on doc website
docs/tutorial/notebook.ipynb       # file to specify API on doc website
docs/tutorial/tools/nb_to_doc.py   # file to specify API on doc website

# tests
tests/test_basic.py                # basic tests for package
tests/test_advanced.py             # more advanced tests

# code
<name of package>/__init__.py      # file indicating that this folder is a module
<name of package>/core.py          # file containing essential code
<name of package>/helpers.py       # file containing helper functions
```
These are the minimum files needed to create a CDL python package. We'll go into more depth on each of these components.

## The essentials
Below is a list of (important) files required for a CDL-approved python package.

### README.md
While often tedious to create, this is one of the most important files in a software project.  It provides a roadmap for users to install, utilize and contribute to your project. Even the best code without proper documentation is effectively useless. A CDL-approved README should contain the following information:

- __Overview__ - A plain english high level overview of what your package does
- __Try it__ - A link to a Binder notebook that allows potential users to quickly try out the package
- __Installation__ - A section detailing how the package can be installed
- __Requirements__ - A full list of software dependencies
- __Citing__ - Information on how to reference the software
- __Contributing__ - A link to a [Code of Conduct](https://www.mozilla.org/en-US/about/governance/policies/participation/), and a link to the CONTRIBUTING.md file
- __Testing__ - Instructions on how to test the package
- __Examples__ - Pictoral and/or code examples of the package in action

For examples of these README sections, please see the [hypertools](https://github.com/ContextLab/hypertools/blob/master/readme.md) README.

### LICENSE
We typically use an open-source MIT for software.  Use [this](https://github.com/ContextLab/hypertools/blob/master/LICENSE) one unless there is a reason for the software not to be open-source.

### CONTRIBUTING.md
This section is critical for a successful open-source project. As the project grows, so will the number of people who'd like to contribute.  Having a guideline on how to contribute will save you (and contributors) a lot of time in the long run. For an example, see [here](https://github.com/ContextLab/hypertools/blob/master/CONTRIBUTING.md).

### setup.py
This file is required to tell python you want to create a python package. Below is a simple example of a setup.py file:
```
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='cdl',
    version='0.1.0',
    description='Sample package for CDL tutorial',
    long_description=readme,
    author='Contextual Dynamics Laboratory',
    author_email='contextualdynamics@gmail.com',
    url='https://www.context-lab.com',
    license=license,
    install_requires = requirements,
    packages=find_packages(exclude=('tests', 'docs'))
)
```
These are the essential fields to set up a python package. There are additional arguments that can be added to this file.  For examples, see [here](https://github.com/ContextLab/CDL-tutorials/blob/package-updates/packages/example_package/setup.py) and [here](https://github.com/kennethreitz/setup.py).

### requirements.txt
This file contains all the software dependencies for your project. Each line should be a different pip installable package.  To specify particular versions, use the syntax: `hypertools==0.5.1`. An example can be seen [here](https://github.com/ContextLab/CDL-tutorials/blob/package-updates/packages/example_package/requirements.txt)

## Documentation
Great documentation is critical to the success of an open-source software project. Every (public) function you write should be accompanied by a docstring.  "Public" means that a user will directly interact with the function.  A docstring is a description of what the function does and includes all possible inputs and outputs. To be consistent, we use the numpydoc format. For details on the numpydoc format, see [here](http://numpydoc.readthedocs.io/en/latest/format.html). Here is a simple example of a function documented in "numpydoc" style:

```
def add(a, b):
  """
  The sum of two numbers.

  Parameters
  ----------
  x : int
      Description of parameter `x`.
  y : int
      Description of parameter `y`

  Returns
  -------
  int
      Description of anonymous integer return value.
  """
  return a + b
```

In the CDL, we use `sphinx`, a package that helps to create awesome documentation. One of the nice things about `sphinx` is that if you document your code in the format above, it can be automatically ported to a `sphinx` documentation website. Therefore, we __strongly recommend__ using this format for code documentation (and documenting before or while you write the code!) as it makes the whole documentation process much, much easier.

## `sphinx`
`sphinx` is a python package that makes building great documentation easier. The basic idea is that it extracts the docstrings, example code, and tutorials in your software project and generates a nice html website from them. This website can be hosted on [ReadtheDocs](https://readthedocs.org/) (more on that later) or any web server (such as github pages). To generate `sphinx` documentation from scratch, (after installing `pip install sphinx`) you can use the [sphinx-quickstart](http://www.sphinx-doc.org/en/master/usage/quickstart.html) command line interface. However, this tutorial includes a template customized for CDL projects that you can use.
