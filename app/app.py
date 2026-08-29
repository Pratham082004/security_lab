"""Application entry point."""

from flask import Flask

app = Flask(__name__)


@app.route('/health')
def hello_world():
    return 'Healthy!'





def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
