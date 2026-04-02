from functools import wraps
from flask import jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt, get_jwt_identity

def role_required(allowed_roles):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            verify_jwt_in_request()

            # ✅ identity (user id)
            user_id = get_jwt_identity()

            # ✅ claims (extra data like role)
            claims = get_jwt()
            role = claims.get("role")

            if role not in allowed_roles:
                return jsonify({"error": "Access denied"}), 403

            return func(*args, **kwargs)
        return wrapper
    return decorator