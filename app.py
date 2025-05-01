from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS
from models import db, Survey

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = SQLALCHEMY_TRACK_MODIFICATIONS

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/survey", methods=["POST"])
def create_survey():
    data = request.get_json()
    survey = Survey(
        first_name=data["first_name"],
        last_name=data["last_name"],
        street_address=data["street_address"],
        city=data["city"],
        state=data["state"],
        zip_code=data["zip_code"],
        phone=data["phone"],
        email=data["email"],
        survey_date=datetime.strptime(data["survey_date"], "%Y-%m-%d"),
        liked_most=data["liked_most"],
        interest_source=data["interest_source"],
        recommendation=data["recommendation"]
    )
    db.session.add(survey)
    db.session.commit()
    return jsonify({"message": "Survey submitted successfully"}), 201

@app.route("/surveys", methods=["GET"])
def get_surveys():
    surveys = Survey.query.all()
    return jsonify([{
        "id": s.id,
        "first_name": s.first_name,
        "last_name": s.last_name,
        "street_address": s.street_address,
        "city": s.city,
        "state": s.state,
        "zip_code": s.zip_code,
        "phone": s.phone,
        "email": s.email,
        "survey_date": s.survey_date.strftime("%Y-%m-%d"),
        "liked_most": s.liked_most,
        "interest_source": s.interest_source,
        "recommendation": s.recommendation
    } for s in surveys])

@app.route("/surveys/<int:survey_id>", methods=["GET"])
def get_survey_by_id(survey_id):
    survey = Survey.query.get_or_404(survey_id)
    return jsonify({
        "id": survey.id,
        "first_name": survey.first_name,
        "last_name": survey.last_name,
        "street_address": survey.street_address,
        "city": survey.city,
        "state": survey.state,
        "zip_code": survey.zip_code,
        "phone": survey.phone,
        "email": survey.email,
        "survey_date": survey.survey_date.strftime("%Y-%m-%d"),
        "liked_most": survey.liked_most,
        "interest_source": survey.interest_source,
        "recommendation": survey.recommendation
    })



@app.route("/survey/<int:survey_id>", methods=["PUT"])
def update_survey(survey_id):
    data = request.get_json()
    survey = Survey.query.get_or_404(survey_id)
    for key in data:
        setattr(survey, key, data[key])
    db.session.commit()
    return jsonify({"message": "Survey updated"})

@app.route("/survey/<int:survey_id>", methods=["DELETE"])
def delete_survey(survey_id):
    survey = Survey.query.get_or_404(survey_id)
    db.session.delete(survey)
    db.session.commit()
    return jsonify({"message": "Survey deleted"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
