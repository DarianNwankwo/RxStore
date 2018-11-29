from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, SelectField
from wtforms.validators import ValidationError, DataRequired, EqualTo, Length, Email
from app.models import Patient, Doctor, Pharmacist, Prescription


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    user_type = SelectField(
        "Type",
        description="What type of user are you?", 
        choices=[("patient", "Patient"), ("doctor", "Doctor"), ("pharmacist", "Pharmacist")],
        validators=[DataRequired()]
        )
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Sign In")


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(),
                                           EqualTo('password')])
    submit = SubmitField('Register')


class EditPatientForm(FlaskForm):
    pass


class EditPharmacistForm(FlaskForm):
    pass


class EditDoctorForm(FlaskForm):
    pass


class EditPrescriptionForm(FlaskForm):
    pass