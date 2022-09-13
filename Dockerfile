FROM python:3.8.6-alpine

WORKDIR /django_test

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN pip install --upgrade pip
COPY ./django_project/ /django_test/
COPY ./requirements.txt /django_test/
RUN pip install -r requirements.txt

