import os

from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object(os.getenv('APP_SETTINGS'))

    from models import db
    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app