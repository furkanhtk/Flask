from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database_parameters.sqlite3'

db = SQLAlchemy(app)


class Parameters(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    date_data = db.Column(db.DateTime())
    input_frequency_data = db.Column(db.String())
    input_power_data = db.Column(db.String())
    measured_raw_power_data = db.Column(db.String())
    angle_data = db.Column(db.String())
    calculated_power_data = db.Column(db.String())


def __init__(self, date_data, input_frequency_data, input_power_data, measured_raw_power_data, angle_data,
             calculated_power_data):
    self.date_data = date_data
    self.input_frequency_data = input_frequency_data
    self.input_power_data = input_power_data
    self.measured_raw_power_data = measured_raw_power_data
    self.angle_data = angle_data
    self.calculated_power_data = calculated_power_data


@app.route('/')
def parameters_page():
    return render_template('parameters_page.html', Parameters=Parameters.query.all())


@app.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['date_data'] or not request.form['input_frequency_data'] or not request.form['input_power_data']:
            flash('Please enter all the fields', 'error')
        else:
            parameter = Parameters(request.form['date_data'], request.form['input_frequency_data'],
                                   request.form['input_power_data'], request.form['measured_raw_power_data'],
                                   request.form['angle_data'], request.form['calculated_power_data'])

            db.session.add(parameter)
            db.session.commit()
            flash('Record was successfully added')
            return redirect(url_for('parameters_page'))
    return render_template('new_parameter.html')


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
