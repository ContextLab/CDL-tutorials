# Python package tutorial
This tutorial shows how to create a CDL-approved python package and how to generate documentation using sphinx.

## To get started
1. Pull latest from CDL-tutorials repo
2. Navigate to the sample_package folder and run `pip install -e .`. This will install an editable installation of the package so you can modify it.

## Basic structure
The very basic structure for a CDL Python package looks like this:
```
README.md                # documentation about the package
LICENSE                  # license file (typically MIT)
setup.py                 # python package config file
requirements.txt         # text file containing software dependencies
sample/__init__.py       # file indicating that this folder is a module
sample/core.py           # file containing essential code
sample/helpers.py        # file containing helper functions
docs/conf.py             # file for configuring documentation with sphinx
docs/index.rst           # file to generate index.html on doc website
docs/api.rst             # file to specify API on doc website
tests/test_basic.py      # basic tests for package
tests/test_advanced.py   # more advanced tests
```


## Table of contents

- [requirements](https://github.com/ContextLab/Tutorials/blob/master/Tutorial%20Template/requirements.txt): List of dependencies for this tutorial, able to be automatically installed via `pip`.
- [data](https://github.com/ContextLab/Tutorials/tree/master/Tutorial%20Template/Data)
   - [example data creation](https://github.com/ContextLab/Tutorials/blob/master/Tutorial%20Template/Data/Example_Data_Creation.ipynb): Notebook containing an example of how to create and save data
  - [chirp.npy](https://github.com/ContextLab/Tutorials/blob/master/Tutorial%20Template/Data/chirp.npy): .npy file of the example dataset  
  - [downloading data example](https://github.com/ContextLab/CDL-tutorials/blob/master/tutorial_template/data/downloading_data_example.ipynb)- example of how to download data from on line and source it in the text, data from [here](http://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris)
  - [iris.npy](https://github.com/ContextLab/CDL-tutorials/blob/master/tutorial_template/data/iris.npy): saved file of data created and analyzed in "Downloading data example"
- [notebooks](https://github.com/ContextLab/Tutorials/tree/master/Tutorial%20Template/Notebooks): Folder containing Jupyter Notebooks
  - [demo](https://github.com/ContextLab/Tutorials/blob/master/Tutorial%20Template/Notebooks/Demo.ipynb): Analyzing the sample data
- [slides](https://github.com/ContextLab/Tutorials/tree/master/Tutorial%20Template/Slides)
  - [slides.txt](https://github.com/ContextLab/Tutorials/blob/master/Tutorial%20Template/Slides/Source.tex): Txt format for the slide show- copy and paste into Overleaf as a template to make your own show
  - [slides.pdf](https://github.com/ContextLab/Tutorials/blob/master/Tutorial%20Template/Slides/template%20slideshow.pdf): Pdf presentation of the tutorial
  - [figs](https://github.com/ContextLab/Tutorials/tree/master/Tutorial%20Template/Slides/figs): Folder containing figures for the slideshow
    - [make figure](https://github.com/ContextLab/Tutorials/blob/master/Tutorial%20Template/Slides/figs/make_figure.ipynb): Code to make the figure in the slideshow
    - [sin](https://github.com/ContextLab/Tutorials/blob/master/Tutorial%20Template/Slides/figs/sin.pdf): PDF version of slide show figure
