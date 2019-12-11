import os
from flask import Flask
from flask_cors import CORS
from config.routes import init_routes
from database.database import db
from database.database import ma


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile(os.path.abspath('app.cfg'))
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + \
        os.path.join(basedir, "db.sqlite")

    # Database initialize with app
    db.init_app(app)
    ma.init_app(app)
    with app.app_context():
        # db.drop_all()
        db.create_all()

    return app


if __name__ == "__main__":
    app = create_app()
    CORS(app, supports_credentials=True)
    init_routes(app)
    app.run(port=5001, debug=True, host='0.0.0.0', use_reloader=True)
