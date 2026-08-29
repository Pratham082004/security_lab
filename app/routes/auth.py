"""Authentication routes."""

from flask import Blueprint, jsonify

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/login', methods=['POST'])
def login():
    """Return a placeholder login response."""
    return jsonify({'message': 'Login endpoint not implemented yet.'}), 501


if __name__ == '__main__':
    print('Auth routes loaded.')
