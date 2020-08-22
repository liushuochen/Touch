import flask
from util.net import get_start_info

app = flask.Flask(__name__)


if __name__ == '__main__':
    host, port = get_start_info()
    app.run(host=host, port=port)
