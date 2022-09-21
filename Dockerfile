FROM python:3

ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/app
COPY requirements/local.txt ./
COPY requirements/base.txt ./

RUN pip install -r ./local.txt

