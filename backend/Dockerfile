# Use an official Python runtime as a parent image
FROM python:3

MAINTAINER Ian Zamorano "ian.zamorano7@gmail.com"

ENV PYTHONUNBUFFERED 1

# Set the working directory to /www
RUN mkdir /www
COPY requirements.txt /www/requirements.txt

WORKDIR /www

RUN pip install -r requirements.txt
