"""Database configuration and helper functions."""


def get_database_url() -> str:
    """Return the application database URL."""
    return 'sqlite:///app.db'


def init_db():
    """Initialize the database connection."""
    return None


if __name__ == '__main__':
    print('Database module loaded.')
