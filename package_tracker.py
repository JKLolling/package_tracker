from flask import Flask, render_template
import os
from Routes import index
app = Flask(__name__)

app.config.update({
    'SECRET_KEY': os.environ.get("SECRET_KEY"),
    "SQLALCHEMY_TRACK_MODIFICATIONS": False
})

app.register_blueprint(index.bp)
