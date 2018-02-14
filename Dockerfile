
FROM debian:latest

MAINTAINER Contextual Dynamics Lab <contextualdynamics@gmail.com>

RUN apt-get update && apt-get install -y eatmydata
RUN eatmydata apt-get install -y wget bzip2 ca-certificates \
    git \
    swig \
    mpich \
    pkg-config \
    gcc \
    wget \
    curl \
    vim \
    nano

RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \
    wget --quiet https://repo.continuum.io/archive/Anaconda3-4.4.0-Linux-x86_64.sh -O ~/anaconda.sh && \
    /bin/bash ~/anaconda.sh -b -p /opt/conda && \
    rm ~/anaconda.sh
ENV PATH /opt/conda/bin:$PATH

RUN pip install --upgrade pip
RUN pip install --upgrade \
numpy \
scipy \
pandas \
scikit-learn \
seaborn \
hypertools \
matplotlib

ADD pandas /PANDAS
ADD coding /coding
ADD docker /docker
ADD testing /testing
Add tutorial_template /tutorial_template

# ENV GOOGLE_APPLICATION_CREDENTIALS=/data/credentials.json

EXPOSE 9999
