from datetime import datetime
from flask import render_template, url_for, request, flash, redirect, url_for, g
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app, db, nodes
from app.forms import LoginForm, RegistrationForm, EditPatientForm, EditPharmacistForm, EditDoctorForm, EditPrescriptionForm
from app.models import Patient, Doctor, Pharmacist, Prescription

print(f"App Object: {app}")
chord_node = None
####################################################################################
# Configuration
####################################################################################
@app.before_request
def before_request():
    global chord_node
    chord_node = nodes[ get_port() ]

####################################################################################
# Routes for anding page, registration, and login
####################################################################################
@app.route("/")
@app.route("/index")
# @login_required
def index():
    print(chord_node.port)
    return render_template("index.html", title="Home")


@app.route("/login", methods=["GET", "POST"])
def login():
    # print(f"Port value: {app.chord_node.port}")
    print(f"Port value: {request.host}")
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = LoginForm()
    if form.validate_on_submit():
        user = get_user(form)
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password")
            return redirect(url_for("login"))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get("next")
        if not next_page or url_parse(next_page).netloc != "":
            return redirect(next_page)
    return render_template("login.html", title="Login", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = get_user(form)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Congratulations, you are now a registered user!")
        return redirect(url_for("login"))
    return render_template("register.html", title="Register", form=form)


####################################################################################
# Routes for patient
####################################################################################
@app.route("/profile")
def profile():
    return render_template("profile.html", title="Profile of <User>")


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


####################################################################################
# Utility functions. (TODO): Move to separate file
####################################################################################
def get_user(form):
    type_ = form.user_type.data
    if type_ == "patient":
        user = Patient.query.filter_by(username=form.username.data).first()
    if type_ == "doctor":
        user = Doctor.query.filter_by(username=form.username.data).first()
    if type_ == "pharmacist":
        user = Pharmacist.query.filter_by(username=form.username.data).first()
    return user


def get_port():
    """Returns the current application's port number."""
    return request.host.split(":")[1]

