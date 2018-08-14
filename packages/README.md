## Python package tutorial

This tutorial shows how to create a python package, starting from the CDL template, and how to create user friendly documentation for the package with readthedocs.

To get started:
[1] pull latest from CDL-tutorials repo
[2] install the requirements in package/sample_package using `pip install -r requirements.txt`
[3] pip install the package 'pip install -e .' and play around with it
[4] clone the CDL-starter-pack repository
[5] copy the core.py and helpers.py files from sample_package into CDL-starter-pack to begin beuilding package as if from scratch


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
