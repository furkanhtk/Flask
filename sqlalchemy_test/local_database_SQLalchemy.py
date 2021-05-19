from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Let's import our Book and Base classes from our database_setup.py file

from test_sqlalchemy import Parameters, Base


# bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
engine = create_engine('sqlite:///parameters_database.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object.
session = DBSession()


# Create

parameterOne = Parameters(Frequency="1 GHz", Power="-10 dbm",)
session.add(parameterOne)
session.commit()

# Read

session.query(Parameters).all()
session.query(Parameters).first()

# Update
editedParameter = session.query(Parameters).filter_by(id=1).one()



editedParameter.Power = "99 dbm"
session.add(editedParameter)
session.commit()





# Delete

ParameterToDelete = session.query(Parameters).filter_by(Frequency='1 GHz').one()
session.delete(ParameterToDelete)
session.commit()