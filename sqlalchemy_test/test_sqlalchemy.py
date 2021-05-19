#https://medium.com/swlh/flask-sqlalchemy-basics-60d4f7f122


import sys


from sqlalchemy import Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine


Base = declarative_base()



engine = create_engine('sqlite:///parameters_database.db')

Base.metadata.create_all(engine)

