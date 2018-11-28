from datetime import datetime
from flask import render_template, url_for, request, flash, redirect, url_for
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, RegistrationForm, EditPatientForm, EditPharmacistForm, EditDoctorForm, EditPrescriptionForm
from app.models import Patient, Doctor, Pharmacist, Prescription


####################################################################################
# Routes for anding page, registration, and login
####################################################################################
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", title="Home")


@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html", title="Login")


@app.route("/register", methods=["GET", "POST"])
def register():
    return render_template("register.html", title="Register")


####################################################################################
# Routes for patient
####################################################################################
@app.route("/patient", methods=["GET", "POST"])
def patient():
    """Display all patients for the current representative. Receives POST request for new users."""
    return render_template("patient/index.html", title="Patient")


@app.route("/patient/<patient_id>", methods=["GET", "POST", "DELETE"])
def patient_info(patient_id):
    """Show info about one specific user. Receives POST request for updating/editing/deleting a particular user."""
    return render_template("patient/show.html", title="Patient <Name>")


@app.route("/patient/<patient_id>/edit")
def edit_patient():
    """Show the form to edit a patient's profile and POST to /patient/<patient_id>"""
    return render_template("patient/edit.html", title="Edit Profile")


@app.route("/patient/new")
def new_patient():
    """Renders a form for new patients and redirects to /patient"""
    return render_template("patient/new.html", title="New Patient")


####################################################################################
# Routes for representative
####################################################################################
@app.route("/representative", methods=["GET", "POST"])
def representative():
    return render_template("representative/index.html", title="Representative")


@app.route("/representative/<rep_id>", methods=["GET", "POST"])
def representative_info(rep_id):
    return render_template("representative/show.html", title="Rep <Name>")


@app.route("/representative/<rep_id>/edit")
def edit_representative(rep_id):
    return render_template("representative/edit.html", title="Edit Profile")


@app.route("/representative/new")
def new_representative():
    return render_template("representative/new.html")