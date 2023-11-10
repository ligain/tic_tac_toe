FROM python:3.11

ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY . /app

RUN pip3 install --upgrade pip -r requirements.txt

EXPOSE 5000