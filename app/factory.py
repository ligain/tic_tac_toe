import os

from flask import Flask

def create_app(config: str = None):
    app = Flask(__name__)

    if not config:
        config = os.getenv('APP_SETTINGS')

    app.config.from_object(config)

    from models import db
    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app