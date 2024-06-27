from flask_jwt_extended import JWTManager
from flask import Blueprint

jwt = JWTManager()

auth_bp = Blueprint('auth', __name__)
