from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_migrate import Migrate

db = SQLAlchemy()
bcrypt = Bcrypt()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = "secret"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # ✅ THIS IS THE FIX (VERY IMPORTANT)
    CORS(app,
         resources={r"/*": {"origins": "http://localhost:5173"}},
         supports_credentials=True)

    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)

    from app.views import bp
    app.register_blueprint(bp)

    return app