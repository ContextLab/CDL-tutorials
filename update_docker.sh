#!/bin/bash

git pull
docker build -t cdl .
docker -rm CDL
docker run -it -p 9999:9999 --name CDL -v ~/Desktop:/mnt cdl
