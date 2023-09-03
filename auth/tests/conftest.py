import pytest
from app import create_app
from extras import db


@pytest.fixture()
def app():
    app = create_app('testing')

    yield app

    # Clean up
    with app.app_context():
        db.drop_all()


@pytest.fixture()
def client(app):
    return app.test_client()
