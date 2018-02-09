# Testing



# Getting Started

+ Clone this repo: `git clone https://github.com/ContextLab/CDL-tutorials.git` or pull latest

+ Follow instructions in the Docker tutorial to build the docker image, or
if you have already built the docker image, execute the command:

`docker start CDL && docker attach CDL`

+ Install Pytests [https://docs.pytest.org/en/latest/getting-started.html] and
TravisCI [https://github.com/travis-ci/travis.rb.git]

+ To test, run `pytest` in the folder that contains the functions you want to test

## Pytest tutorial

+ Walk through these scripts in the followin order and and execute these commands in this folder:

+ test_sample.py

+ `$ pytest`

+ test_sysexit.py

+ `$ pytest -q test_sysexit.py`

+ test_class.py

+ `$ pytest -q test_class.py`

## IPytest tutorial

+ Walk through tutorial outlines in Testing.ipynb in the Notebooks folder

## Helpful commands
