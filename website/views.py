from flask.wrappers import Response
from sqlalchemy.sql.functions import user
from website.auth import login
from flask import Blueprint, render_template, request, flash, url_for, redirect, jsonify
from flask_login.utils import login_required, current_user
from .models import User
from . import db


views = Blueprint("views", __name__)


@views.route("/")
@views.route("/home")
@login_required
def home():
    if current_user.username == "AnnePapa":
        return render_template("HomeAnnePapa.html", user=current_user)
    elif current_user.username == "OmaOpa":
        return render_template("HomeOmaOpa.html", user=current_user)
    elif current_user.username == "AnneAnneDede":
        return render_template("HomeAnneAnneDede.html", user=current_user)
    elif current_user.username == "TanteMalaikaOnkelPascal":
        return render_template("HomeTanteMalaikaOnkelPascal.html", user=current_user)
    elif current_user.username == "HüseyinDayiTanteSilvia":
        return render_template("HomeHuseyinDayiTanteSilvia.html", user=current_user)
    else:
        flash("Sorry dieser Username hat kein Home")
        return render_template("info.html")

@views.route("/info")
def info():
    return render_template("info.html", user=current_user)