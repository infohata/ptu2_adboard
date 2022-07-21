# syntax=docker/dockerfile:1
FROM python:slim-buster
WORKDIR /app
COPY ./adboard .
COPY ./requirements.txt .
RUN apt update && apt upgrade
RUN pip install -r requirements.txt
# RUN python manage.py collectstatic --noinput
# RUN python manage.py migrate
# #CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# CMD ["gunicorn", "-w", "3", "-b", "0.0.0.0:8000", "adboard.wsgi"]
