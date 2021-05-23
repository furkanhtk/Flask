from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Parameters, Base
import datetime



def get_parameters(session):
    parameters_list = session.query(Parameters).all()
    return parameters_list



def add_parameter(session, freq, pwr,g_ref,distance,antenna_type,mode):
    parameter_to_add = Parameters(input_frequency=freq, input_Power=pwr, date=datetime.datetime.now().strftime("%Y-%m-%d-%X"), g_ref=g_ref, distance=distance, antenna_type=antenna_type, mode=mode)
    session.add(parameter_to_add)
    session.commit()
    # session.query(Parameters).first()


def update_parameter(session, id_number, freq, pwr):
    edited_parameter = session.query(Parameters).filter_by(id=id_number).one()
    edited_parameter.input_frequency = freq
    edited_parameter.input_Power = pwr
    session.add(edited_parameter)
    session.commit()

def delete_parameter(session, parameter_id):
    parameter_to_delete = session.query(Parameters).filter_by(id=parameter_id).one()
    session.delete(parameter_to_delete)
    session.commit()


def get_parameter(session, parameter_id):
    parameter_ = session.query(Parameters).filter_by(id=parameter_id).one()
    return parameter_

if __name__ == "__main__":
    engine = create_engine('sqlite:///parameters_database.db')
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    add_parameter(session,"14","14")
    parameters_list = get_parameters(session)
    for parameter in parameters_list:
        print("id:{} F:{} P:{} D:{}".format(parameter.id, parameter.input_frequency, parameter.input_Power, parameter.date))
