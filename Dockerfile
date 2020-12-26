FROM python:3.8.6-alpine

LABEL Maintainer="akshaych.dev@gmail.com"

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1


COPY ./requirements.txt /requirements.txt

RUN set -ex \
  && mkdir /app \
  && pip install --upgrade pip \
  && apk add --update --no-cache postgresql-libs jpeg-dev \
  && apk add --update --no-cache --virtual .tmp-build-deps \
  gcc musl-dev postgresql-dev zlib zlib-dev linux-headers \
  && pip install --no-cache-dir -r /requirements.txt \
  && apk --purge del .tmp-build-deps

WORKDIR /app
COPY ./app /app

RUN mkdir -p /vol/web/media \
  && mkdir -p /vol/web/static \
  && adduser -D user \
  && chown -R user:user /vol/ \
  && chown -R user:user /app \
  && chmod -R 755 /vol/web

USER user

CMD gunicorn app.wsgi:application --bind 0.0.0.0:$PORT