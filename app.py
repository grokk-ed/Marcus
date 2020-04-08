import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)
migrate = Migrate(app, db)
from models import User  # noqa: E402, F401


@app.route('/')
def hello():
    print(os.environ['APP_SETTINGS'])
    return "Hello World!"


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)


if __name__ == '__main__':
    app.run()
