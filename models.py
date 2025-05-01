from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Survey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    street_address = db.Column(db.String(200), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(100), nullable=False)
    zip_code = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    survey_date = db.Column(db.Date, nullable=False)

    liked_most = db.Column(db.String(50), nullable=False)  # e.g., "students"
    interest_source = db.Column(db.String(50), nullable=False)  # e.g., "Internet"
    recommendation = db.Column(db.String(50), nullable=False)  # e.g., "Very Likely"
