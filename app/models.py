from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db#, login


class Patient(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    doctor_id = db.Column(db.Integer, db.ForeignKey("doctor.id"))
    pharm_id = db.Column(db.Integer, db.ForeignKey("pharmacist.id"))
    first_name = db.Column(db.String(32), index=True)
    middle_name = db.Column(db.String(32), index=True)
    last_name = db.Column(db.String(32), index=True)
    birthdate = db.Column(db.Date)
    gender = db.Column(db.String(1), index=True)
    # primary_physician = db.Column(db.String(96), index=True)
    insurance_number = db.Column(db.String(64))
    allergies = db.relationship("Allergies", backref="patient", lazy="dynamic")
    street_address = db.Column(db.String(96))
    state = db.Column(db.String(2))
    city = db.Column(db.String(96))
    zip_code = db.Column(db.String(12))
    country = db.Column(db.String(96))
    email = db.Column(db.String(120))
    phone_number = db.Column(db.String(14))
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))


    def __repr__(self):
        return '<User {}>'.format(self.username)


    def set_password(self, password):
        self.password_hash = generate_password_hash(password)


    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    


class Prescription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(96), index=True)
    is_name_brand = db.Column(db.Boolean())
    refills_left = db.Column(db.Integer)
    directions = db.Column(db.String(300))
    disbursed = db.Column(db.Integer, default=0)
    dosage_strength = db.Column(db.String(5))
    prescribe_date = db.Column(db.DateTime, default=datetime.utcnow)
    disbursed_date = db.Column(db.DateTime, default=datetime.utcnow)


class Doctor(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patients = db.relationship("Patient", backref="doc", lazy="dynamic")
    first_name = db.Column(db.String(32), index=True, unique=False)
    middle_name = db.Column(db.String(32), index=True, unique=False)
    last_name = db.Column(db.String(32), index=True, unique=False)
    birthdate = db.Column(db.Date)
    gender = db.Column(db.String(1), index=True)
    hospital = db.Column(db.String(96), index=True)
    medical_license = db.Column(db.String(96))
    street_address = db.Column(db.String(96))
    state = db.Column(db.String(2))
    city = db.Column(db.String(96))
    zip_code = db.Column(db.String(12))
    country = db.Column(db.String(96))
    email = db.Column(db.String(120))
    phone_number = db.Column(db.String(14))
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)


    def set_password(self, password):
        self.password_hash = generate_password_hash(password)


    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Pharmacist(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patients = db.relationship("Patient", backref="pharm", lazy="dynamic")
    first_name = db.Column(db.String(32), index=True, unique=False)
    middle_name = db.Column(db.String(32), index=True, unique=False)
    last_name = db.Column(db.String(32), index=True, unique=False)
    birthdate = db.Column(db.Date)
    gender = db.Column(db.String(1), index=True)
    pharmacy = db.Column(db.String(96), index=True)
    medical_license = db.Column(db.String(96))
    street_address = db.Column(db.String(96))
    state = db.Column(db.String(2))
    city = db.Column(db.String(96))
    zip_code = db.Column(db.String(12))
    country = db.Column(db.String(96))
    email = db.Column(db.String(120))
    phone_number = db.Column(db.String(14))
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))


    def __repr__(self):
        return '<User {}>'.format(self.username)


    def set_password(self, password):
        self.password_hash = generate_password_hash(password)


    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Allergies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey("patient.id"))
    name = db.Column(db.String(40), index=True)
    
