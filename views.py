from datetime import datetime
from flask import *
from database import Database
from parameter import Parameter
#from flask import render_template,current_app,abort


def home_page():
    today = datetime.today()
    day_name = today.strftime("%A")
    return render_template("home.html", day=today)


def Measurement_page():
    today = datetime.today()
    day_name = today.strftime("%A")
    return render_template("Measurement.html", day=today)


def parameters_page():
    db = current_app.config["db"]
    if request.method == "GET":
        parameters = db.get_parameters()
        return render_template("parameters.html", parameters=sorted(parameters))
    else:
        form_parameter_keys = request.form.getlist("parameter_keys")
        for form_parameter_key in form_parameter_keys:
            db.delete_parameter(int(form_parameter_key))
        return redirect(url_for("parameters_page"))


def parameter_page(parameter_key):
    db = current_app.config["db"]
    parameter = db.get_parameter(parameter_key)
    if parameter is None:
        abort(404)
    return render_template("parameter.html", parameter=parameter)


def parameter_add_page():
    if request.method == "GET":
        return render_template(
            "parameter_edit.html",
        )
    else:
        form_frequency = request.form["frequency"]
        form_power = request.form["power"]
        parameter = Parameter(form_frequency, int(form_power) if form_power else None)
        db = current_app.config["db"]
        parameter_key = db.add_parameter(parameter)
        return redirect(url_for("parameter_page", parameter_key=parameter_key))
