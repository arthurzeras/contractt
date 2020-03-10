FROM python:3.8

ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
RUN pip install pipenv

RUN mkdir /code
WORKDIR /code

ADD Pipfile Pipfile.lock /code/
RUN pipenv install --system --deploy

ADD . /code/
