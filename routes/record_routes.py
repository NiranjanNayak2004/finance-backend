from flask import Blueprint, request, jsonify
from models.record import Record
from extensions import db
from middleware.role_middleware import role_required

record_bp = Blueprint("record", __name__)

@record_bp.route("/records", methods=["POST"])
@role_required(["admin"])
def create_record():
    data = request.json

    if not data.get("amount") or not data.get("type") or not data.get("category"):
        return jsonify({"error": "Required fields missing"}), 400

    if data["type"] not in ["income", "expense"]:
        return jsonify({"error": "Invalid type"}), 400

    record = Record(
    amount=data["amount"],
    type=data["type"],
    category=data["category"],
    date=data.get("date"),
    notes=data.get("notes")
)

    db.session.add(record)
    db.session.commit()

    return jsonify({"message": "Record created"})


@record_bp.route("/records", methods=["GET"])
@role_required(["admin", "analyst", "viewer"])
def get_records():
    query = Record.query

    if request.args.get("type"):
        query = query.filter_by(type=request.args.get("type"))

    if request.args.get("category"):
        query = query.filter_by(category=request.args.get("category"))

    records = query.all()

    return jsonify([
    {
        "id": r.id,
        "amount": r.amount,
        "type": r.type,
        "category": r.category,
        "date": r.date,
        "notes": r.notes
    } for r in records
])
@record_bp.route("/records/<int:id>", methods=["GET"])
@role_required(["admin", "analyst", "viewer"])
def get_record_by_id(id):
    record = Record.query.get(id)

    if not record:
        return jsonify({"error": "Record not found"}), 404

    return jsonify({
        "id": record.id,
        "amount": record.amount,
        "type": record.type,
        "category": record.category,
        "date": record.date,
        "notes": record.notes
    })
@record_bp.route("/records/<int:id>", methods=["PUT"])
@role_required(["admin"])
def update_record(id):
    record = Record.query.get(id)

    if not record:
        return jsonify({"error": "Record not found"}), 404

    data = request.json

    record.amount = data.get("amount", record.amount)
    record.type = data.get("type", record.type)
    record.category = data.get("category", record.category)
    record.date = data.get("date", record.date)
    record.notes = data.get("notes", record.notes)

    db.session.commit()

    return jsonify({"message": "Record updated"})
@record_bp.route("/records/<int:id>", methods=["DELETE"])
@role_required(["admin"])
def delete_record(id):
    record = Record.query.get(id)

    if not record:
        return jsonify({"error": "Record not found"}), 404

    db.session.delete(record)
    db.session.commit()

    return jsonify({"message": "Record deleted"}).route("/records/<int:id>", methods=["DELETE"])
@role_required(["admin"])
def delete_record(id):
    record = Record.query.get(id)

    if not record:
        return jsonify({"error": "Record not found"}), 404

    db.session.delete(record)
    db.session.commit()

    return jsonify({"message": "Record deleted"})