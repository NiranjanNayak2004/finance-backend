from flask import Blueprint, jsonify,request

from models.record import Record
from collections import defaultdict
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
@dashboard_bp.route("/dashboard/category")
@role_required(["admin", "analyst"])
def category_summary():
    query = Record.query

    # Optional filters
    if request.args.get("type"):
        query = query.filter_by(type=request.args.get("type"))

    if request.args.get("category"):
        query = query.filter_by(category=request.args.get("category"))

    records = query.all()

    category_totals = {}

    for r in records:
        category_totals[r.category] = category_totals.get(r.category, 0) + r.amount

    return jsonify(category_totals)

@dashboard_bp.route("/dashboard/monthly")
@role_required(["admin", "analyst"])
def monthly_trends():
    records = Record.query.all()

    monthly_data = defaultdict(lambda: {"income": 0, "expense": 0})

    for r in records:
        # Extract YYYY-MM from date string
        month = r.date[:7] if r.date else "unknown"

        if r.type == "income":
            monthly_data[month]["income"] += r.amount
        elif r.type == "expense":
            monthly_data[month]["expense"] += r.amount

    return jsonify(monthly_data)