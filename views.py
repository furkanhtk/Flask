from datetime import datetime
from flask import *
import models
from database import Base,Parameters

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import time
########################
import plotly.express as px
import numpy as np
import plotly
import random


def home_page():
    today = datetime.today()
    day_name = today.strftime("%A")
    return render_template("home.html", day=today)


def Measurement_page():
    raw_data = np.genfromtxt("dipole_pattern.csv", delimiter=',')
    theta = np.arange(0, 361, 1)
    today = datetime.today()
    fig = px.line_polar(r=raw_data, theta=theta, start_angle=0)
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template("Measurement.html", day=today,graphJSON=graphJSON)


    # today = datetime.today()
    # day_name = today.strftime("%A")
    # return render_template("Measurement.html", day=today)



def parameters_page():
    engine = create_engine('sqlite:///parameters_database.db', connect_args={"check_same_thread": False})
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    if request.method == "GET":
        parameters_list = models.get_parameters(session)
        return render_template("parameters.html", parameters=parameters_list)
    elif request.form.get('Add') == 'Add':
        if request.form.get('mode1') == '1':
            form_mode = 1
        elif request.form.get('mode2') == '2':
            form_mode = 2
        elif request.form.get('mode3') == '3':
            form_mode = 3
        form_frequency = request.form["frequency"]
        form_power = request.form["power"]
        form_g_ref = request.form["g_ref"]
        form_distance = request.form["distance"]
        form_antenna_type = request.form["antenna_type"]
        models.add_parameter(session,form_frequency,form_power,form_g_ref,form_distance,form_antenna_type,form_mode)
        return redirect(url_for("parameters_page"))
    elif request.form.get('Delete') == 'Delete':
        form_parameter_ids = request.form.getlist("parameter_ids")
        for form_parameter_id in form_parameter_ids:
            models.delete_parameter(session, form_parameter_id)
        return redirect(url_for("parameters_page"))
    else:
        return redirect(url_for("parameters_page"))


def parameter_page(parameter_id):
    engine = create_engine('sqlite:///parameters_database.db', connect_args={"check_same_thread": False})
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    parameter = models.get_parameter(session, parameter_id)
    if parameter is None:
        abort(404)
    return render_template("parameter.html", parameter=parameter)


def test():
    return render_template('test.html')


def data():
    # Data Format
    # [TIME, Temperature, Humidity]

    Temperature = random.random() * 100
    Humidity = random.random() * 55

    data = [time.time() * 1000, Temperature, Humidity]

    response = make_response(json.dumps(data))

    response.content_type = 'application/json'

    return response
