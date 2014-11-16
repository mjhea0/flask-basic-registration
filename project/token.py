# project/token.py

from itsdangerous import URLSafeTimedSerializer

from project import app


ts = URLSafeTimedSerializer(app.config["SECRET_KEY"])
