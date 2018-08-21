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
- [Code](#code)
  * [`__init__.py`](#__init__py)
  * [Package organization](#packageorganization)
- [Examples](#examples)
- [Documentation](#documentation)
  * [`sphinx`](#sphinx)
  * [`conf.py`](#confpy)
  * [`index.rst`](#indexrst)
  * [`api.rst`](#apirst)
  * [Code examples](#codeexamples)
  * [Tutorials](#tutorials)
  * [Building the documentation](#buildingthedocumentation)
- [Tests](#tests)
  * [`py.test`](#pytest)
  * [Travis CI](#travisci)

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

# code
<name of package>/__init__.py      # file indicating that this folder is a module
<name of package>/core.py          # file containing essential code
<name of package>/helpers.py       # file containing helper functions

# code examples
examples/                          # folder of python scripts containing example uses of your software

# documentation
docs/conf.py                       # file for configuring documentation with sphinx
docs/index.rst                     # file to generate index.html on doc website
docs/api.rst                       # file to specify API on doc website
docs/tutorial/notebook.ipynb       # file to specify API on doc website
docs/tutorial/tools/nb_to_doc.py   # file to specify API on doc website

# tests
tests/test_basic.py                # basic tests for package
tests/test_advanced.py             # more advanced tests
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

In the CDL, we use `sphinx`, a package that helps to create awesome documentation. One of the nice things about `sphinx` is that if you document your code in the format above, it can be (mostly) automatically ported to a `sphinx` documentation website. Therefore, we __strongly recommend__ using this format for code documentation (and documenting before or while you write the code!) as it makes the whole documentation process much, much easier.

## `sphinx`
`sphinx` is a python package that makes building great documentation easier. The basic idea is that it extracts the docstrings, example code, and tutorials in your software project and generates a nice html website from them. This website can be hosted on [ReadtheDocs](https://readthedocs.org/) (more on that later) or any web server (such as github pages). To generate `sphinx` documentation from scratch, (after installing `pip install sphinx`) you can use the [sphinx-quickstart](http://www.sphinx-doc.org/en/master/usage/quickstart.html) command line interface. However, this tutorial includes a template customized for CDL projects that you can use. The main components of a CDL-approved sphinx page include:

+ A homepage - introduces the software
+ An API page - documentation of how to use it
+ An examples page - stand alone examples of the software functionality
+ A tutorial page - detailed walkthrough of how to use the software

Below are instructions on how to set up this page

### `conf.py`
This is the primary configuration file for a `sphinx` website. It is located in `docs/conf.py`.  This file can be generated from scratch using `sphinx-quickstart`, but for most cases you can simply copy this file and replace the relevant fields. This file is heavily commented, so take a look for details. To customize this file for your project, follow these instructions:

1. replace line 60 with the name of your project
2. replace lines 69 and 71 with the version of your software. If it's a new project start with `0.1.0`. We follow a release guideline called [semantic versioning](https://semver.org/). The basic idea is that releases with only minor bug fixes, patches, typo fixes etc. will advance the rightmost number (`0.1.0 -> 0.1.1`). Major changes like API changes and feature additions advance the middle number (`0.1.0 -> 0.2.0`).  When you are confident that there are no major bugs and importantly the API is __fixed__ and stable, then it is time for a major release (`0.1.0 -> 1.0.0`). Note: It is __bad form__ to change the API after a major release.  Thus, any changes to the API would require anoter major release (`1.0.0 -> 2.0.0`), so __do not__ do this prematurely.  For some context, at the time of writing this `seaborn` is about 5 years old and just recently released version `0.9.0` (i.e. it hasn't yet hit a major release). For all releases `<1.0.0` it is totally fine to change the API (but be kind to your users, nobody likes a moving target).
3. replace line 119 and 129 with the link to the software (e.g. https://github.com/ContextLab/hypertools)
4. replace `cdl` in lines 139, 166, 187-88 with the name of your software (e.g. hypertools)

### `index.rst`
This [reStructuredText](http://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html) file is the home page for your website. At the very least, you should provide a high-level description of what your software is intended to do. For an example, see [here](https://github.com/ContextLab/hypertools/blob/master/docs/index.rst).

### `api.rst`
This file serves as a template for your API documentation.  It's possible to set this up automatically with sphinx (`sphinx-apidoc`), but it can also be done by hand (which is how I typically do it). To set up your API:

1. change line 5 to the name of your package
2. rename line 12 to the name of the function/class you want to document (this is just the label).
3. Replace line 18 with the location of the function/class within the package (e.g. `cdl.chatter`).
4. Copy and paste line 12-18 for all functions/classes you want to document

If you set up your docstrings correctly, that should be all you have to do.  When `sphinx` builds the website, these references will automatically be populated with your docstrings.  Note that this manual approach is easy enough for small projects but could be unsustainable for larger packages.  For larger packages, you'll want to learn how to use [sphinx-apidoc](http://www.sphinx-doc.org/en/master/man/sphinx-apidoc.html). For an example of an `api.rst` file, see [here](https://github.com/ContextLab/hypertools/blob/master/docs/api.rst).

### Tutorials
While tedious, this is a crucial part of your documentation.  It provides a way for users to learn about the package how you intended it to be used.  In practice, writing these notebooks are also very useful for finding software bugs and testing whether your API makes sense in the "wild". These tutorials can be written as a jupyter notebook (located in `docs/tutorial`) and then converted to `.rst` format with a script that I shamelessly stole from `seaborn` (located here: `docs/tutorial/tools/nb_to_doc.py`). For an example notebook see [here](https://github.com/ContextLab/hypertools/blob/master/docs/tutorials/plot.ipynb). After writing the tutorial from `docs/tutorial` in the terminal run: `make notebooks`.  If this is successful, the output should be a `.rst` file with the same name as your notebook (and no error messages in the console). __NOTE:__ This must be run prior to generating the documentation.
