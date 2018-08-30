# CDL python package tutorial
This tutorial shows how to create a CDL-approved python package, organize the code, write examples, tutorials, documentation and tests.

# Table of contents
- [Getting started](#getting-started)
- [Basic structure](#basic-structure-of-a-project)
- [The essentials](#the-essentials)
  * [README.md](#readmemd)
  * [LICENSE](#license)
  * [CONTRIBUTING.md](#contributingmd)
  * [setup.py](#setuppy)
  * [requirements.txt](#requirementstxt)
- [Code](#code)  
  * [Package organization](#package-organization)
  * [`__init__.py`](#__init__py)
- [Examples](#examples)
- [Documentation](#documentation)
  * [`sphinx`](#sphinx)
  * [`conf.py`](#confpy)
  * [`index.rst`](#indexrst)
  * [`api.rst`](#apirst)
  * [Examples](#examples)
  * [Tutorials](#tutorials)
  * [`tutorials.rst`](#tutorialsrst)
  * [Build the documentation](#build-the-documentation)
- [Tests](#tests)
  * [`py.test`](#pytest)
  * [Travis CI](#travisci)
- [Releases](#releases)
- [Pushing to pip](#pip)

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
.travis.yml                        # config file to set up travis (automated testing)
MANIFEST.in                        # tells pip what folders to include in package

# code
<name of package>/__init__.py      # file indicating that this folder is a module
<name of package>/core.py          # file containing essential code
<name of package>/helpers.py       # file containing helper functions

# code examples
examples/                          # folder of python scripts containing example uses of your software
examples/plot_add_lists.py         # file illustrating some functionality of the package
examples/README.txt                # can be empty, but required for sphinx to create example gallery

# documentation
docs/conf.py                       # file for configuring documentation with sphinx
docs/index.rst                     # file to generate index.html on doc website
docs/api.rst                       # file to specify API table of contents
docs/Makefile                      # helps to generate the sphinx docs
docs/doc_requirements.txt          # file containing requirements to build documentation
docs/tutorials.rst                 # file to specify tutorials table of content
docs/tutorial/notebook.ipynb       # jupyter notebook with example tutorial
docs/tutorial/tools/nb_to_doc.py   # tool to convert from .ipynb to .rst
docs/tutorial/Makefile             # file to convert notebooks to .rst

# tests
tests/test_core.py                # basic tests for package
tests/test_helpers.py             # more advanced tests
```
These are the minimum files needed to create a CDL python package. We'll go into more depth on each of these components.

## The essentials
Below is a list of files required for a CDL-approved python package.

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
This file contains all the software dependencies for your project. Each line should be a different pip installable package.  To specify particular versions, use the syntax: `hypertools==0.5.1`. An example can be seen [here](https://github.com/ContextLab/CDL-tutorials/blob/package-updates/packages/example_package/requirements.txt).

## Code
The code for your software project should go in a folder named with the name of the project.  In this example, the folder is `cdl` and it contains 3 files: `__init__.py`, `core.py` and `helpers.py`.  While package organization can vary dramatically as function of the project scope/complexity, there are some general organizational principles that will make it easier to maintain. There is also some fundamental structure you must follow in order for Python to recognize the code a package. The general structure of a very simple package should look something like this:

```
cdl
└── __init__.py : initializes the package
└── core.py : main code
└── helpers.py : helper code
```

For packages with more complex functionality, the organization might look something like this:

```
cdl
└── __init__.py : initializes the package
└── folder1 : contains code for some functionality
    ├── __init__.py : initializes the folder1 module
    └── folder1_core.py : main code for folder1 functionality
    └── folder1_helpers.py : helper code for folder1 functionality
└── folder2 : contains code for some other functionality
    ├── __init__.py : initializes the folder2 module
    └── folder2_core.py : main code for folder2 functionality
    └── folder2_helpers.py : helper code for folder2 functionality
```

### Package organization
As the project grows in complexity, organization becomes essential. CDL-approved packages generally follow a "modular" structure.  That is, functions that are similar in objective are grouped together. For example in the folders above, `folder1` might contain all code related to plotting whereas `folder2` code contain all code related to data analysis. Another principle we follow is to write everything once and reuse. You might be wondering, "What if I need the same functionality in two difference scripts"? The answer is to write the function once and then import it wherever you need it.  For example, if you needed some functionality from `folder1_helpers.py` in `folder1_core.py`, at the top of your `folder1_core.py` script you would write:

```
from .folder1_helpers import <name-of-function>
```

To import code from another folder, at the top of your `folder1_core.py` file:

```
from ..folder2.folder2_core import <name-of-function>
```

For a full treatment of good coding principles, see [Jeremy's tutorial](https://github.com/ContextLab/CDL-tutorials/blob/master/coding/slides/coding_tips.pdf) and for more on packages see [here](https://docs.python.org/3/tutorial/modules.html#packages) and [here](http://mikegrouchy.com/blog/2012/05/be-pythonic-__init__py.html).

### `__init__.py`
This is a special file that tells Python to recognize a folder as part of your package. For every code folder in your package, you must include an `__init__.py` file if you want it included in the package.  It can be empty, or it can contain "initialization" code for the particular code module.

## Examples
This folder contains basic examples of your package in action.  Keep these simple and self contained.  Users should be able to run all of the examples after installing your package.  The examples can be referred to directly, but will also be compiled and assembled into a gallery of examples on the documentation website (see [here](https://hypertools.readthedocs.io/en/latest/auto_examples/index.html) for example). In order for `sphinx` to recognize these, there are a few formatting requirements.  First, scripts that render an image must be named `plot_XX.py` where XX can be anything. Secondly, all scripts must have a header like this:

```
# -*- coding: utf-8 -*-
"""
=============================
A basic example
=============================

Add some more text here.
"""

# Code source: Andrew Heusser
# License: MIT
```

The text at the top (between the lines) will be read as the title of the example, and the text below the lines should be a high-level description of what is being illustrated with the example.  Finally, it's useful to include the code source and well as the license (although not strictly required). See [here](https://github.com/ContextLab/hypertools/blob/master/examples/plot_basic.py) for a full example.

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
3. Replace line 18 with the location of the function/class within the package (e.g. `cdl.hmm`).
4. Copy and paste line 12-18 for all functions/classes you want to document

If you set up your docstrings correctly, that should be all you have to do.  When `sphinx` builds the website, these references will automatically be populated with your docstrings.  Note that this manual approach is easy enough for small projects but could be unsustainable for larger packages.  For larger packages, you'll want to learn how to use [sphinx-apidoc](http://www.sphinx-doc.org/en/master/man/sphinx-apidoc.html). For an example of an `api.rst` file, see [here](https://github.com/ContextLab/hypertools/blob/master/docs/api.rst).

### Tutorials
While tedious, this is a crucial part of your documentation.  It provides a way for users to learn about the package how you intended it to be used.  In practice, writing these notebooks are also very useful for finding software bugs and testing whether your API makes sense in the "wild". These tutorials can be written as a jupyter notebook (located in `docs/tutorial`) and then converted to `.rst` format with a script that I shamelessly stole from `seaborn` (located here: `docs/tutorial/tools/nb_to_doc.py`). For an example notebook see [here](https://github.com/ContextLab/hypertools/blob/master/docs/tutorials/plot.ipynb). After writing the tutorial from `docs/tutorial`, edit the `docs/tutorial/Makefile` to refer to each of you tutorial notebooks ([example](https://github.com/ContextLab/hypertools/blob/master/docs/tutorials/Makefile)). The, in the terminal run: `make notebooks`.  If this is successful, the output should be a `.rst` file with the same name as your notebook (and no error messages in the console). These `.rst` files will comprise the tutorials section of your documentation website. __NOTE:__ This must be run prior to generating the documentation.

### `tutorials.rst`
This file is used to specify the table of contents for your tutorials.  It is located in `docs/tutorial.rst`. Edit it for you own use by:
1. change line 5 to whatever title you'd like
2. change line 8 to be the title of the tutorial
3. change line 14 to be the location of the jupyter notebook containing the tutorial
4. copy lines 8-14 for as many tutorials as you have

### Build the documentation
If you've made it this far, you now have all the elements to build the documentation. Inside of the `docs` folder, simply run: `make html`.  If this runs successfully, it should generate a folder inside of `docs` called `_build`.  Navigate into this folder and double click `index.html`. At this point, you should have a full documentation website.  Click through the links to make sure they all work, and the examples and tutorials rendered properly.

### ReadtheDocs
If you've made it this far, syncing up to ReadtheDocs should be relatively painless:

1. go to the ReadtheDocs [login](https://readthedocs.org/accounts/login/) page and enter your credentials (they will be on the CDL 1password site).
2. log in and select "Import a project". Find your project and add it. __NOTE__: it will only show up here if it is under the CDL github list and is __public__.
3. Give the project a name and click next.  
4. Navigate to "Advanced Settings" and check "Install your project inside a virtualenv using setup.py install"
5. Under `Requirements file`, add the text: `docs/doc_requirements.txt`
6. Navigate to the bottom and hit save

You can check to see if everything worked by clicking "Builds".  If the one on top says "Passed", the website compiled correctly on ReadtheDocs.  If it says "Failed", click the build and it will give you some output useful for debugging. If this all works, then you are good to go!  Any time you change the code/documentation (e.g. pushing to github), the website will rebuild and any new changes will be updated on the website automatically.

## Tests
Great tests are a crucial part of reliable software.  There are many benefits to writing great tests. First, tests assure that your functions are working as you expect them to. Second, they allow for a battery of checks each time you make a change. It's difficult to anticipate the downstream consequences of changing a particular function. Tests allow you to catch bugs as you develop instead of after the fact.  Third, they can be automated.  Using a service like TravisCI, it's possible to run tests each time you (or a new contributor to the project) submits a pull request.  In large projects, PRs are not even considered until they pass the tests.  This enforces a certain level of quality and overall, makes the code better. For example tests, check out the `tests/test_core.py` file

### `pytest`
`pytest` is the CDL-approved package for writing tests.  First, install the package (`pip install pytest`).  Then, create a folder in your package called `tests`. Finally, write the tests!  For example tests, check out the scripts in the `tests` folder. Once the tests are written, simply call `pytest` in terminal inside your package repo. If any of the tests do not pass, `pytest` will tell you the tests failed and show you where. Here's a very basic example:

```
def test_add_two_numbers():
  a = 1
  b = 2
  assert add(a, b)==3
```

This test is written to see whether the `add` function is working properly.  The key part of this is the `assert` statement, which can be used to check for expected behavior. If `add(a, b)==3` is `False`, then this will trigger pytest to tell you that 1 of your tests has failed and give you details on why.


A few tips for writing good tests:
- __Make sure your are tests fast__. A good test will check the logic of a function as quickly and simply as possible. This will save time during development If you have a complicated function, it may be necessary to write a more complicated test.  Start simple and add only what you need to confirm that the function is working as expected.
- __Name your tests intuitively__. This will speed up debugging.  If your function is called `add` and you are checking whether the code accurately adds two numbers, name the test `test_add_two_numbers`. If it fails when you run the tests, you'll immediately know what went wrong. __NOTE__: You must lead your function names with `test_` or they will not run.
- __Separate your tests into multiple files__.  For simple packages this is not necessary, but as your code grows in complexity, maintaining multiple test scripts is a good way to organize things.  This also allows you to test specific modules of the code, which can save time.
-__Write tests as you code__. Each time you write a function, you should also write a test function. Otherwise, you will be faced with a massive task of writing all your tests at once.  The quality of the tests will inevitably be worse, and it will take longer because you will have to remind yourself of what each function does. Some folks will even write the tests before they write the function, which forces you to think about the API before diving into the guts of the code.

For more information on writing tests, see [here](https://docs.python-guide.org/writing/tests/#py-test).

### TravisCI
TravisCI is a service that automatically runs your test each time you push your code to Github.  In addition, you can test your software on multiple versions of your programming language (e.g. python 2 and 3) and send the results as a webhook (e.g. to slack). To set up travis, you will need to add a `.travis.yml` file to your repo. Here's what's inside:

```
language: python                                      # the programming language
sudo: false                                           # turn off sudo
python:                                               # versions of python to test
- '2.7'
- '3.5'
- '3.6'
install:                                              # install instructions
- wget http://repo.continuum.io/miniconda/Miniconda-latest-Linux-x86_64.sh -O miniconda.sh
- bash miniconda.sh -b -p $HOME/miniconda
- export PATH="$HOME/miniconda/bin:$PATH"
- hash -r
- conda config --set always_yes yes --set changeps1 no
- conda update -q conda
- conda info -a
- conda create -q -n testenv python=$TRAVIS_PYTHON_VERSION pip pytest
- source activate testenv
- python setup.py install
script: py.test                                       # how to run the tests
```
There are many more optional specifications which you can read about [https://docs.travis-ci.com/user/getting-started/]. You can also tell travis to send its results to slack upon completion.  Instructions for that are [here](https://docs.travis-ci.com/user/notifications/)

To setup the Travis service, go to their [website](https://travis-ci.com/), and sign in with your github credentials.  Your public repos will show up, and you can turn on the service for them.
