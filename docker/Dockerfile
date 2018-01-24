# Dockerfile for CDL docker tutorial.  The line below is the operating system or
# runtime. It is the 'parent image' which you can build on top of in the lines
# below. For example, the parent image can be an operating system like debian
(a Linux distribution) or a runtime like python.

FROM debian:stretch

# This line specifies who maintains the docker file

MAINTAINER Contextual Dynamics Lab <contextualdynamics@gmail.com>

# Here, we will install all debian-related packages. apt-get is a linux package
that is similar to pip for python.  It contains many libraries that are useful
for scientific computing.  First, we will update apt-get to make sure it is up
to date.

RUN apt-get update

# Now we'll install eatmydata, which helps to make the debian install faster.

RUN apt-get install -y eatmydata

# Here, we install some basic packages.  python-dev is a package needed to
support python. python-pip installs pip. procps installs a few more useful
packages like ps, top, kill and others. git is a software version control
program. yasm is a program that translates to and from machine language and
assembly language.

RUN eatmydata apt-get install -y \
    python-dev \
    python-pip \
    procps \
    git \
    yasm \
    vim

# This line just removes some unecessary files to keep the docker container lean.

RUN rm -rf /var/lib/apt/lists/*

# Here, we will layer on some python packages.  First let's upgrade pip

RUN pip install --upgrade pip

# Now, let's install all the libraries we need for the CDL docker image.  Here
are the basics.  What else do we need? Let's add it here.

RUN pip install --upgrade \
setuptools \
requests

# Here, we can add data folders to the docker image.

ADD notebooks /notebooks
ADD data /data
ADD slides /slides

# The working directory is the location that the docker image initializes in
whenever it is started.  We will set it to notebooks.

WORKDIR /notebooks

# Environmental variables are variables that will be available to you in the
terminal.

ENV A=1

# This allows you to expose a port from within the docker to provide a service
or listen on.

EXPOSE 9999
