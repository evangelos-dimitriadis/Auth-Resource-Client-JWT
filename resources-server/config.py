import os

CURRENT_PATH = os.getcwd()

LOGS_FILE = os.path.join(CURRENT_PATH, 'log')
APP_SECRET_KEY = os.getenv('APP_SECRET_KEY') or 'so_secret'
