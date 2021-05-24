from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Parameters, Base
import datetime
import models



engine = create_engine('sqlite:///parameters_database.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
models.add_parameter(session,"99","99")
