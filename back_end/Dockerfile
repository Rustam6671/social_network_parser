FROM python:3.8.6-alpine3.12

RUN mkdir -p /home/www
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV APP_HOME=/home/www
RUN addgroup -S www && adduser -S www -G www
WORKDIR /home/www

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev bash

RUN /usr/local/bin/python -m pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
WORKDIR /home/www/russo_proj

#RUN chown -R www:www $APP_HOME

#USER www
