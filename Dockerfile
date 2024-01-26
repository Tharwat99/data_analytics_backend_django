FROM python:3.8

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
COPY ./requirements.txt .
RUN pip install -r requirements.txt


RUN mkdir /app
WORKDIR /app
COPY . /app

EXPOSE 8000

CMD python manage.py runserver 0.0.0.0:8000