# Reference: https://medium.com/shot-code/running-django-postgresql-containers-and-persisting-data-with-docker-4dd8e4dd5361
FROM python:3.8

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

# Install postgres client
RUN apt-get update && \
	apt-get install postgresql-client dkms build-essential linux-headers-amd64 \
	gcc libc6-dev -y

RUN pip install -r /requirements.txt

WORKDIR /app

# [Security] Limit the scope of user who run the docker image
RUN useradd -ms /bin/bash devops

USER devops
