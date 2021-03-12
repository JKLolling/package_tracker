from flask import Flask, render_template
import os
from Routes import index
from flask_migrate import Migrate
from app.models import db

app = Flask(__name__)

app.config.update({
    'SECRET_KEY': os.environ.get("SECRET_KEY"),
    "SQLALCHEMY_TRACK_MODIFICATIONS": False,
    'SQLALCHEMY_DATABASE_URI': os.environ.get("DATABASE_URL")
})

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(index.bp)
