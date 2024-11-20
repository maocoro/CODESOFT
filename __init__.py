from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy ()

def create_app():

    app = Flask (__name__)

    app.config.from_object('config.Config')
    db.init_app(app)

    from flask_ckeditor import CKEditor
    ckeditor = CKEditor (app)

    from codesft import home
    app.register_blueprint(home.bp)

    from codesft import code
    app.register_blueprint(code.bp)

    from codesft import auth
    app.register_blueprint(auth.bp)

    from .models import User, Computer, Transacciones, Alertas

    with app.app_context():
        db.create_all()

    return app