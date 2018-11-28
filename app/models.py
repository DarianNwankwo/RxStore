from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import app, db#, login


class Person(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(32), index=True, unique=False)
    middle_name = db.Column(db.String(32), index=True, unique=False)
    last_name = db.Column(db.String(32), index=True, unique=False)
    birthdate = db.Column(db.Date)
    gender = db.Column(db.String(1), index=True)



class Patient(Person):
    pass
    


class Prescription(db.Model):
    id = db.Column(db.Integer, primary_key=True)


class Doctor(Person):
    pass


class Pharmacist(Person):
    pass



# class Contact(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     patient_id = db.Column(db.Integer, db.ForeignKey("patient.id"))
#     street_address
#     state
#     city = db.Column(db.String(74), index=True, unique=True)
#     zip_code = db.Column(db.String(10), index=True)
#     country = db.Column(db.String(74), index=True)
#     email = db.Column(db.String(120), index=True, unique=True)
#     phone_number
