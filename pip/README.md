
# Pushing to pip

# Register with PyPi:

First you need to either register or log in to [PyPi](https://pypi.org/) and [test PyPi](https://test.pypi.org/):

Using a text editor, open up a `~/.pypirc ` file and add the code found in the pypirc.txt file:


# Install Twine
`pip install twine`

# Tar your project
In your project directory run:
`python setup.py sdist`
This should create a `.tar.gz` package of your source files within a new subfolder calles dist/.

# Draft a new release
You'll also need to add this tarball under the release notes.
Make sure to document all changes that occurred between releases.

# Create a test upload:
`twine upload -r test dist/PACKAGENAME-VERSION.tar.gz`

# Create a test install:
Create a virtual environment:

`virtualenv MY_VIRTUALENV`

` cd MY_VIRTUALENV`

`source bin/activate`

`pip install -i https://testpypi.python.org/pypi PACKAGENAME`

And make sure your package is installed.

# Upload for REALS
`twine upload dist/PACKAGENAME-VERSION.tar.gz`

And check that you can install it:
`pip install PACKAGENAME`


If you get stuck, [this](https://tom-christie.github.io/articles/pypi/) is a great link.

Fin
