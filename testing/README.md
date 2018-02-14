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

+ Test scripts found in the Tests folder

+ Correspond to the examples in slides

## IPytest tutorial

+ Walk through the same examples in Testing.ipynb found in the Notebooks folder

## Helpful commands

+ find helpful pytest fixtures:
`pytest --fixtures`