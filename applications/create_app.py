# create_app.py

import os
from flask import Flask
from sqlalchemy import inspect
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
        inspector = inspect(db.engine)
        tables_exist = inspector.get_table_names()
        if not tables_exist:
            db.create_all()
