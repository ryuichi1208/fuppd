FROM python:3.7.4-alpine3.10
LABEL maintainer="ryuichi1208 (ryucrosskey@gmail.com)"

WORKDIR /app
EXPOSE 5000
COPY . /app

ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

RUN apk add --no-cache \
    git openssl ffmpeg \
    opus libffi-dev gcc \
    curl musl-dev
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT ["uwsgi", "--ini", "settings/app.ini"]
