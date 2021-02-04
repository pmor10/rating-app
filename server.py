"""Server for movie ratings app."""

from flask import Flask

app = Flask(__name__)


# Replace this with routes and view functions!


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8888)
