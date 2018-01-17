This template folder is designed to be a guide for making the tutorials in this repository. The Contextual Dynamics Lab does ask that the guidelines outlined below appear in the tutorials added to this repo and other pages/files/tools are always welcome as well.

A complete tutorial:
  - contains a README with:
      - what the tutorial is for, potential use cases, and how the tutorial is organized
      - a list of the notebooks and datasets included in the tutorial with clickable links
      - describes how to install the necessary dependencies for running the tutorials
  - is self-contained:
      - meaning that the module itself is sharable and doesn't reference other modules in the repo
      - with the exception of referencing to other tutorials as potential prerequisites or next steps in a learning guide (i.e. "to do the Pandas tutorial, you should first do the Python tutorial" (with a clickable link to the python tutorial))
          - please link these in the README or as you are referencing them 

# Template Tutorial README 

This tutorial is designed to be a starting point for other tutorials in this repo. It is recommended that you clone this tutorial and then use it as a launching point for your tutorial. There are three main components of the tutorial Notebooks, Data, and Slides. In the Data folder are two files. One creating data which saves as a .npy to the which is also stored in the folder. The Notebook folder contains an example Jupyter notebook that analyzes data from the Data folder. Finally the Slides folder contains an example slide show that walks through this tutorial and the source.tex to make your own presentation.


To be able to run through the notebooks in the tutorial first install the requirements using `pip install -r requirements.txt` After installing the requirements read through the slides, and then go through the notebook. 

After completing this tutorial, you should be able to move on to any other tutorial in the repo and also have the skill set needed to make your own tutorial. 

## Table of contents

- [Requirements](https://github.com/ContextLab/Tutorials/blob/master/Tutorial%20Template/requirements.txt)- List of dependencies for this tutorial, able to be automatically installed via `pip`.
- [Data](https://github.com/ContextLab/Tutorials/tree/master/Tutorial%20Template/Data)- The data we are analyzing in this tutorial comes from [here](https://pandas.pydata.org/pandas-docs/stable/index.html)
  - [Example data creation](https://github.com/ContextLab/Tutorials/blob/master/Tutorial%20Template/Data/Example_Data_Creation.ipynb)- Notebook containing an example of how to create and save data
  - [Saved data file](https://github.com/ContextLab/Tutorials/blob/master/Tutorial%20Template/Data/chirp.npy)- Npy file of the example dataset  
- [Notebooks](https://github.com/ContextLab/Tutorials/tree/master/Tutorial%20Template/Notebooks)- Folder containing Jupyter Notebooks
  - [Demo](https://github.com/ContextLab/Tutorials/blob/master/Tutorial%20Template/Notebooks/Demo.ipynb)- Analyzing the sample data
- [Slides](https://github.com/ContextLab/Tutorials/tree/master/Tutorial%20Template/Slides)
  - [Slides.txt](https://github.com/ContextLab/Tutorials/blob/master/Tutorial%20Template/Slides/Source.tex)- Txt format for the slide show- copy and paste into Overleaf as a template to make your own show 
  - [Slides.pdf](https://github.com/ContextLab/Tutorials/blob/master/Tutorial%20Template/Slides/template%20slideshow.pdf)-Pdf presentation of the tutorial
  - [figs](https://github.com/ContextLab/Tutorials/tree/master/Tutorial%20Template/Slides/figs)- Folder containing figures for the slideshow 
    - [Make figure](https://github.com/ContextLab/Tutorials/blob/master/Tutorial%20Template/Slides/figs/make_figure.ipynb)- Code to make the figure in the slideshow
    - [Sin](https://github.com/ContextLab/Tutorials/blob/master/Tutorial%20Template/Slides/figs/sin.pdf)- PDF version of slide show figure 
