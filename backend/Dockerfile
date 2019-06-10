# Docker file for a slim Ubuntu-based Python3 image

FROM ubuntu:latest
MAINTAINER Ian Zamorano "ian.zamorano7@gmail.com"

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip \
  && apt-get -y install python-setuptools \
  && apt-get -y install cron

# Set the working directory to /www
RUN mkdir /www
WORKDIR /www

# Set and install requirements
COPY requirements.txt /www/requirements.txt
RUN pip install -r requirements.txt

# Crontab task
COPY crontab /etc/cron.d/populate-task
RUN chmod 0644 /etc/cron.d/populate-task
RUN service cron start


