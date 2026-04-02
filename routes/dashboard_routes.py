from flask import Blueprint, jsonify
from models.record import Record
from middleware.role_middleware import role_required

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/dashboard/summary")
@role_required(["admin", "analyst"])
def summary():
    records = Record.query.all()

    income = sum(r.amount for r in records if r.type == "income")
    expense = sum(r.amount for r in records if r.type == "expense")

    return jsonify({
        "total_income": income,
        "total_expense": expense,
        "net_balance": income - expense
    })