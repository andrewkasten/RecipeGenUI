FROM python:3.12-slim

RUN mkdir /backend
WORKDIR /backend

ADD requirements.txt /backend/

RUN pip install -r requirements.txt

COPY . /backend/

CMD gunicorn --bind 0.0.0.0:8000 --workers 3 config.wsgi:application
