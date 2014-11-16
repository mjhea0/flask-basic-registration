# Flask User Management

[![Build Status](https://travis-ci.org/mjhea0/flask-basic-registration.svg?branch=master)](https://travis-ci.org/mjhea0/flask-basic-registration)

Starter app for managing users - login/logout and registration.

### Set Environment Variables

```sh
$ export APP_SETTINGS="config.DevelopmentConfig
$ export DATABASE_URL="postgresql://localhost/users"
$ export APP_MAIL_USERNAME="blah"
$ export APP_MAIL_PASSWORD="blah"
```

### Quickstart

```sh
$ python manage.py create_db
$ python manage.py db init
$ python manage.py db migrate
$ python manage.py create_admin
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

### Todo

1. forgot password
1. change/update password and email
1. more unit and integration tests
1. travis
1. deployment options
