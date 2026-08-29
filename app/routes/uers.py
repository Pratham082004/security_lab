"""User-related routes."""

from flask import Blueprint, jsonify

bp = Blueprint('users', __name__, url_prefix='/users')


@bp.route('/', methods=['GET'])
def list_users():
    """Return a placeholder users response."""
    return jsonify({'users': []})


if __name__ == '__main__':
    print('Users routes loaded.')
