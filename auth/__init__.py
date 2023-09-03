import os
import sys
import logging
import server.models
from flask import Flask
from extras import db
from config import config


def create_app(config_name):
    # Init the Flask application
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # Init the database
    db.init_app(app)

    with app.app_context():
        db.create_all()

    # Set up the endpoints with a Blueprint
    from server.routes import bp
    app.register_blueprint(bp)

    os.umask(0)
    os.makedirs(os.path.dirname(app.config['LOGS_FILE']), exist_ok=True, mode=0o755)
    logging.basicConfig(level=logging.INFO,
                        handlers=[logging.FileHandler(filename=app.config['LOGS_FILE']),
                                  logging.StreamHandler(stream=sys.stdout)],
                        format=('%(levelname)-7s %(asctime)s %(module)-11s%(funcName)-13s'
                                '%(message)s'),
                        datefmt='%H:%M:%S')

    return app
