"""Comment routes."""

from flask import Blueprint, jsonify

bp = Blueprint('comments', __name__, url_prefix='/comments')


@bp.route('/', methods=['GET'])
def list_comments():
    """Return a placeholder comments response."""
    return jsonify({'comments': []})


if __name__ == '__main__':
    print('Comments routes loaded.')
