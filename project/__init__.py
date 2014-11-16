# project/__init__.py


#################
#### imports ####
#################

import os

from flask import Flask
from flask.ext.login import LoginManager
from flask.ext.bcrypt import Bcrypt
from flask.ext.sqlalchemy import SQLAlchemy
from flask_mail import Mail


################
#### config ####
################

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
login_manager = LoginManager()
login_manager.init_app(app)
bcrypt = Bcrypt(app)
mail = Mail(app)
db = SQLAlchemy(app)

from project.main.views import main_blueprint
from project.user.views import user_blueprint

# register our blueprints
app.register_blueprint(main_blueprint)
app.register_blueprint(user_blueprint)

# flask-login
from models import User

login_manager.login_view = "user.login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == int(user_id)).first()
