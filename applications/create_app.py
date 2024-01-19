# create_app.py

import os
from flask import Flask
from sqlalchemy import inspect
from db.db import db
from dotenv import load_dotenv

load_dotenv()


def create_app(config_name='default'):
    '''
    Creates the app
    '''
    app = Flask(__name__)

    if config_name == 'testing':
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['SQLITE_DATABASE_URI']

    db.init_app(app)
    initialize_database(app)

    return app


def initialize_database(app):
    '''
    Setup the db
    '''
    with app.app_context():
        inspector = inspect(db.engine)
        tables_exist = inspector.get_table_names()
        if not tables_exist:
            db.create_all()
