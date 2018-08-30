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
