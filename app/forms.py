from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, EqualTo, Length
from app.models import Patient, Doctor, Pharmacist, Prescription


class LoginForm(FlaskForm):
    pass


class RegistrationForm(FlaskForm):
    pass


class EditPatientForm(FlaskForm):
    pass


class EditPharmacistForm(FlaskForm):
    pass


class EditDoctorForm(FlaskForm):
    pass


class EditPrescriptionForm(FlaskForm):
    pass