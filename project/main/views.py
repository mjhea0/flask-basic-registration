# project/main/views.py

#################
#### imports ####
#################

from flask import render_template, Blueprint
from flask.ext.login import login_required


################
#### config ####
################

main_blueprint = Blueprint(
    'main', __name__,
    template_folder='templates'
)


################
#### routes ####
################

@main_blueprint.route('/')
@login_required
def home():
    return render_template('index.html')
