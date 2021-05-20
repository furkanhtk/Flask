from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from test_sqlalchemy import Parameters, Base




def get_parameters(session):
    parameters_list = session.query(Parameters).all()
    for parameter in parameters_list:

        print("id:{} F:{} P:{}".format(parameter.id, parameter.Frequency, parameter.Power))

    return parameters_list



def add_parameter(session, freq, pwr):
    parameter_to_add = Parameters(Frequency=freq, Power=pwr)
    session.add(parameter_to_add)
    session.commit()
    # session.query(Parameters).first()


def update_parameter(session, id_number, freq, pwr):
    edited_parameter = session.query(Parameters).filter_by(id=id_number).one()
    edited_parameter.Frequency = freq
    edited_parameter.Power = pwr
    session.add(edited_parameter)
    session.commit()

def delete_parameter(session,parameter_key):
    parameter_to_delete = session.query(Parameters).filter_by(Frequency='1 GHz').one()
    session.delete(parameter_to_delete)
    session.commit()


if __name__ == "__main__":
    engine = create_engine('sqlite:///parameters_database.db')
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    get_parameters(session)

    update_parameter(session,5,)