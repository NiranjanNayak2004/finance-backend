from flask import Blueprint, app, request, jsonify
from models.record import Record
from models.user import User
from extensions import db
from middleware.role_middleware import role_required

user_bp = Blueprint("user", __name__)

@user_bp.route("/users", methods=["POST"])
@role_required(["admin"])
def create_user():
    data = request.json

    if not data.get("name") or not data.get("email") or not data.get("role"):
        return jsonify({"error": "All fields are required"}), 400

    user = User(
        name=data["name"],
        email=data["email"],
        role=data["role"]
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User created"})


@user_bp.route("/users", methods=["GET"])
@role_required(["admin", "analyst", "viewer"])
def get_users():
    users = User.query.all()

    return jsonify([
        {
            "id": u.id,
            "name": u.name,
            "email": u.email,
            "role": u.role,
            "is_active": u.is_active
        } for u in users
    ])
