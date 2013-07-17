flask-basic-registration
========================

Basic user registration package for Flask. Use this as a boilerplate for your app.

- Flask==0.10.1
- Flask-SQLAlchemy==0.16
- Flask-WTF==0.8.4
- Jinja2==2.7
- MarkupSafe==0.18
- SQLAlchemy==0.8.2
- WTForms==1.0.4
- Werkzeug==0.9.1
- itsdangerous==0.22
- wsgiref==0.1.2
 
## Setup

1. clone the repo
2. setup/activate a virtualenv
3. install the requirements
4. update the rdms (sqlite, mysql, postgres)
5. create the database (*db_create.py*)

## Todo

1. create better documentation
2. add unit tests
3. add email verification
4. probably a few more things

## Screenshot

![djang-stripe](http://content.screencast.com/users/Mike_Extentech/folders/Jing/media/f250eb0a-3500-47e0-a555-ed0f2f8ddefc/00000209.png)

## Project structure

    ├── app
    │   ├── __init__.py
    │   ├── forms.py
    │   ├── models.py
    │   ├── templates
    │   │   ├── 404.html
    │   │   ├── 500.html
    │   │   ├── base.html
    │   │   ├── login.html
    │   │   ├── members.html
    │   │   └── register.html
    │   └── views.py
    ├── config.py
    ├── db_create.py
    ├── error.log
    ├── requirements.txt
    └── run.py
