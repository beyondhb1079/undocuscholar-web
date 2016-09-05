import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create the application
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)

app.debug = True
app.config.from_envvar('API_SETTINGS', silent=True)