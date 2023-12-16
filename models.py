"""Models Interface

Contains models with wrap the database tables in SQLAlchmy ORM"""
import re, os
from sqlalchemy import create_engine
from sqlalchemy import (Column, Integer, String, ForeignKey, Float, DateTime, Text, Table, MetaData)
#from sqlalchemy.dialects.postgresql import UUID
#from sqlalchemy.orm import relation, relationship
from sqlalchemy.sql.sqltypes import Date
from sqlalchemy.orm import (relationship, Mapped, mapped_column, declarative_base)
from dataclasses import dataclass
from datetime import datetime

Base = declarative_base(metadata=MetaData(schema='public'))

@dataclass
class Factors(Base):
    """The factor table
    
    """
    __tablename__ = 'factors'
    reps :  Mapped[int] = mapped_column(primary_key=True)
    factor : Mapped[float] = mapped_column(nullable=False)

    def __repr__(self):
        return(f"Factor(id: {self.reps}, factor: {self.factor})")

@dataclass
class Exercises(Base):
    """The exercises table
    
    """
    __tablename__ = 'exercises'

    #id=Column(Integer, primary_key=True)
    id : Mapped[int] = mapped_column(primary_key=True)
    #exercise_name=Column(String(50), nullable=False)
    exercise_name  : Mapped[str] = mapped_column(nullable=False)
    #description=Column(Text, nullable=True)
    description : Mapped[str] = mapped_column(nullable=True)
    #exrx_name=Column(String(60, nullable=True))
    exrx_name : Mapped[str] = mapped_column(nullable=True) 

    def __repr__(self):
        return(f"Exercise(id: {self.id}, name: {self.exercise_name}, description: {self.description}, EXRX Name: {self.exrx_name}")

@dataclass
class Sets(Base):
    """The sets class represents the activities during a weight training session.  It should be used when the training
       consistes of a repatative routine of cadence and weights.

    :param Base: _description_
    :type Base: _type_
    """
    
    __tablename__ = 'sets'
    id : Mapped[int] = mapped_column(primary_key=True)
    date : Mapped[datetime] = mapped_column(nullable=False)
    exercise_id : Mapped[int] = mapped_column(ForeignKey(Exercises.id))
    cadence : Mapped[str] = mapped_column(nullable=False)
    weights : Mapped[str] = mapped_column(nullable=True)
    weight_unit : Mapped[str] = mapped_column(nullable=True)
    notes : Mapped[str] = mapped_column(nullable=True)

if __name__ == '__main__':
    try:
        uri = os.environ['PG_AZURE_URI']
        engine = create_engine(uri)
    except Exception as e:
        print('Failed to connect to database.')
        print('{0}'.format(e))

    Base.metadata.create_all(engine)
