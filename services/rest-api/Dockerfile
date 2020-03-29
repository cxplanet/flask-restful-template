# pull official deb base, no alpine here
FROM python:3.8.1-slim-buster
WORKDIR /usr/src/app

# prevent writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
# do not buffer stdout and stderr
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update && apt-get install -y netcat

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

COPY . /usr/src/app/