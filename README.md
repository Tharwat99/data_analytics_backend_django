# Data analytics backend Django
Simple Data Analytics Platform that allows users to visualize and analyze data


## Clone Project
The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/Tharwat99/data_analytics_backend_django.git
$ cd data_analytics_backend_django
```

## Normal Setup
Create a virtual environment to install dependencies in and activate it:

```sh
$ python -m venv env
$ cd env/Scripts
$ activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Then makemigrations and migrate models to db:
```sh
(env)$ python manage.py makemigrations 
(env)$ python manage.py migrate
```

Once `pip` has finished downloading the dependencies:

## Tests

To run the tests:
```sh
(env)$ python manage.py test
```
## Runserver

```sh
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.

## Docker Setup

```sh
$ docker-compose  up --build
```
Then makemigrations and migrate models to db:

```sh
(env)$ docker-compose run app sh -c "python manage.py makemigrations" 
(env)$ docker-compose run app sh -c "python manage.py migrate"
```
## Tests
To run the tests:
```sh
(env)$ docker-compose run app sh -c "python manage.py test"
```

