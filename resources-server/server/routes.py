import jwt
import logging
from flask import Blueprint, jsonify, request, g
bp = Blueprint('resource', __name__)


@bp.before_request
def decode_auth_token():
    """
    Validates the auth token before every request
    :raises ExpiredSignatureError: If token is expired
    :raises InvalidTokenError: If token is invalid
    :raises Exception: For every other error
    """
    try:
        # Extract the authorization token from the header
        auth_header = request.headers.get('Authorization')
        if auth_header:
            auth_token = auth_header.split(" ")[1]
        else:
            return jsonify({'Error': 'No token found. Please login and provide a valid token'}), 404
        if auth_token:
            public_key = open('jwt-key.pub').read()
            payload = jwt.decode(auth_token, public_key, algorithms=['RS256'])
            # Save user info in g, an object that can store data during an application context
            g.user_info = payload
    except jwt.ExpiredSignatureError:
        return jsonify({'Error': 'Signature expired. Please login again.'}), 403
    except jwt.InvalidTokenError:
        return jsonify({'Error': 'Invalid token. Please login.'}), 403
    except Exception as e:
        logging.exception(e)
        return jsonify({'Error': 'Something went wrong. Please try again later'}), 500


@bp.route('/user', methods=["GET"])
def get_user():
    """
    Dummy function to show how an API could return resources
    :return: The decoded jwt user info
    :rtype: json
    """
    return jsonify({'result': g.user_info})
