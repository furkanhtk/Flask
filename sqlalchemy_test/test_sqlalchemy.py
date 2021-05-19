#https://medium.com/swlh/flask-sqlalchemy-basics-60d4f7f122


import sys


from sqlalchemy import Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine


Base = declarative_base()

class Book(Base):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True)
    Frequency = Column(String(250), nullable=False)
    Power = Column(String(250), nullable=False)


# creates a create_engine instance at the bottom of the file

engine = create_engine('sqlite:///parameters_database.db')

Base.metadata.create_all(engine)


