from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


# Crear una extension
db = SQLAlchemy()

def create_app():

    app = Flask(__name__)

    # Configuracion del proyecto
    app.config.from_mapping(
        DEBUG = False,
        SECRET_KEY = 'dev123',
        SQLALCHEMY_DATABASE_URI = 'sqlite:///todolist.db'
    )

    db.init_app(app)

    # Registrar Blueprint todo
    from . import todo
    app.register_blueprint(todo.bp)

    # Registrar Blueprint auth
    from . import auth
    app.register_blueprint(auth.bp)

    @app.route('/')
    def index():
        return render_template('index.html')
    
    with app.app_context():
        db.create_all()
    
    return app