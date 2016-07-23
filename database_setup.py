import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):

    __tablename__ = 'user'

    id = Column(Integer, primary_key = True)
    email = Column(String(80), nullable = False)
    name = Column(String(80), nullable = False)
    score = Column(Integer)

engine = create_engine('sqlite:///user.db')
Base.metadata.create_all(engine)
