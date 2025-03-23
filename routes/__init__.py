# routes/__init__.py

from flask import Blueprint

# 各Blueprintをインポート
from .auth import auth_bp
from .test import test_bp

def register_blueprints(app):
    app.register_blueprint(auth_bp)
    app.register_blueprint(test_bp)
