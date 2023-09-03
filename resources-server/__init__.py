import os
import sys
from flask import Flask
import logging
from config import APP_SECRET_KEY, LOGS_FILE


def create_app():
    # Init the Flask application
    app = Flask(__name__)
    app.secret_key = APP_SECRET_KEY

    # Set up the endpoints with a Blueprint
    from server.routes import bp
    app.register_blueprint(bp)

    # Set up the logging
    os.umask(0)
    os.makedirs(os.path.dirname(LOGS_FILE), exist_ok=True, mode=0o755)
    logging.basicConfig(level=logging.INFO,
                        handlers=[logging.FileHandler(filename=LOGS_FILE),
                                  logging.StreamHandler(stream=sys.stdout)],
                        format=('%(levelname)-7s %(asctime)s %(module)-11s%(funcName)-13s'
                                '%(message)s'),
                        datefmt='%H:%M:%S')

    return app
