# CDL python package tutorial
This tutorial shows how to create a CDL-approved python package and how to generate documentation using sphinx.

# Table of contents
- [Getting started](#getting-started)
- [Basic structure](#basic-structure-of-a-project)
  * [README](#readme)
  * [License](#license)

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

### README
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

### License
We typically use an open-source MIT for software.  Use [this](https://github.com/ContextLab/hypertools/blob/master/LICENSE) one unless there is a reason for the software not to be open-source.

### Contributing
This section is critical for a successful open-source project. As the project grows, so will the number of people who'd like to contribute.  Having a guideline on how to contribute will save you (and contributors) a lot of time in the long run. For an example, see [here](https://github.com/ContextLab/hypertools/blob/master/CONTRIBUTING.md).
