FROM python:3.8-slim-buster

LABEL Maintainer="akshaych.dev@gmail.com"

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

# User created for running application only
RUN adduser -D user
USER user