# syntax=docker/dockerfile:1
FROM python:slim-buster
WORKDIR /app
COPY ./adboard .
COPY ./requirements.txt .
RUN apt update && apt upgrade
RUN pip install -r requirements.txt
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
