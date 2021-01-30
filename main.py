import flask
from config import get_service_info

app = flask.Flask(__name__)


if __name__ == '__main__':
    host, port = get_service_info()
    app.run(host=host, port=port)
