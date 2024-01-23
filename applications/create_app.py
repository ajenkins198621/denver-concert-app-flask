# create_app.py

import os
from flask import Flask
from sqlalchemy import inspect, Table
from db.db import db
from dotenv import load_dotenv

load_dotenv()


def create_app(config_name='default', template_dir='applications/web/templates', static_dir='applications/web/static'):
    '''
    Creates the app
    '''

    app = Flask(__name__, template_folder=os.path.abspath(
        template_dir), static_folder=os.path.abspath(static_dir))

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
        db.metadata.reflect(db.engine)
        if 'concert_raw' not in db.metadata.tables:
            # Create only the 'concert_raw' table
            Table('concert_raw', db.metadata, autoload_with=db.engine)
            db.create_all()
