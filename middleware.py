from flask import request, jsonify
from flask_jwt_extended import verify_jwt_in_request


# JWT Token Validation Middleware
def jwt_middleware():
    if request.path.startswith('/item'):
        try:
            verify_jwt_in_request()
        except Exception:
            return jsonify(message="Invalid JWT Header"), 401


# Input Validation Decorator
def validate_json(*expected_args):
    def decorator(f):
        def wrapper(*args, **kwargs):
            for arg in expected_args:
                if arg not in request.json:
                    return jsonify(message=f"Missing {arg} in request"), 400
            return f(*args, **kwargs)
        return wrapper
    return decorator
