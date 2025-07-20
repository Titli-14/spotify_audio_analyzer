from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "supersecretkey")

    from .routes import routes as main  # ✅ import correctly
    app.register_blueprint(main)

    return app

