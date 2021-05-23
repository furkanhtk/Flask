from database import Parameters, Base
from sqlalchemy import create_engine

engine = create_engine('sqlite:///parameters_database.db')

Base.metadata.create_all(engine)