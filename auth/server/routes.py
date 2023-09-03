import logging
from flask import Blueprint, jsonify, request
from extras import db
from server.models import User
bp = Blueprint('auth', __name__)


@bp.route('/register', methods=["POST"])
def register():
    """
    Registers a new user and returns a new token
    :return: A jwt token
    :rtype: json
    :raises Exception: For every error
    """
    # Get the post data
    data = request.get_json()
    # Check if user exists
    username = data.get('username')
    user = User.query.filter_by(username=username).first()
    if user:
        return jsonify({'Error': 'User already exists. Please choose a different username.'}), 409
    try:
        user = User(username=data.get('username'), password=data.get('password'))
        # Insert the user
        db.session.add(user)
        db.session.commit()
        # Generate the jwt token
        auth_token = user.encode_auth_token(user.id)
        return jsonify({'auth_token': auth_token}), 201
    except Exception as e:
        logging.exception(e)
        return jsonify({'Error': 'Something went wrong. Please try again later.'}), 500


@bp.route('/login', methods=["POST"])
def login():
    """
    Returns a new token
    :return: A jwt token
    :rtype: json
    :raises Exception: For every error
    """
    # Get the post data
    data = request.get_json()
    # Check if user exists
    try:
        user = User.query.filter_by(username=data.get('username')).first()
        if user and user.check_password_hash(data.get('password')):
            # Return token
            auth_token = user.encode_auth_token(user.id)
            return jsonify({'auth_token': auth_token}), 200
        else:
            return jsonify({'Error': 'Wrong username or password. Please try again.'}), 404
    except Exception as e:
        logging.exception(e)
        return jsonify({'Error': 'Something went wrong. Please try again later.'}), 500
