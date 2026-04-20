import logging

def create_app():
    app = Flask(__name__)

    if not app.debug:
        logging.basicConfig(level=logging.INFO)

    return app
