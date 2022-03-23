# Flask User Management

[![Build Status](https://travis-ci.org/mjhea0/flask-basic-registration.svg?branch=master)](https://travis-ci.org/mjhea0/flask-basic-registration)

Starter app for managing users - login/logout and registration.

## QuickStart

Use a python virtual environment:

```sh
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
```

Note: to deactivate (leave the virtual env) type this cmd:
```sh
deactivate
```

### Set Environment Variables

```sh
$ export APP_SETTINGS="project.config.DevelopmentConfig"
```

or

```sh
$ export APP_SETTINGS="project.config.ProductionConfig"
```

### Update Settings in Production

1. `SECRET_KEY`
1. `SQLALCHEMY_DATABASE_URI`

### Create DB

```sh
$ python manage.py create_db
$ python manage.py db init
$ python manage.py db migrate
$ python manage.py create_admin
```

### Run

```sh
$ python manage.py runserver
```

### Testing

Without coverage:

```sh
$ python manage.py test
```

With coverage:

```sh
$ python manage.py cov
```
