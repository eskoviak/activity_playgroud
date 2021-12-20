"""Models Interface

Contains models with wrap the database tables in SQLAlchmy ORM"""
import re, os
from sqlalchemy import create_engine
from sqlalchemy.sql.elements import True_
from sqlalchemy.sql.expression import null, nullslast
from sqlalchemy.sql.operators import as_
from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime, Text, Table
#from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relation, relationship
from sqlalchemy.sql.sqltypes import Date
from sqlalchemy.ext.declarative import declarative_base
from dataclasses import dataclass

Base = declarative_base()

@dataclass
class Factors(Base):
    """The factor table
    
    """
    __tablename__ = 'factors'
    reps = Column(Integer, primary_key=True)
    factor = Column(Float)

    def __repr__(self):
        return(f"Factor(id: {self.id}, factor{self.factor})")

@dataclass
class Exercises(Base):
    """The exercises table
    
    """
    __tablename__ = 'exercises'

    id=Column(Integer, primary_key=True)
    exercise_name=Column(String(50), nullable=False)
    description=Column(Text, nullable=True)

    def __repr__(self):
        return(f"Exercise(id: {self.id}, name: {self.exercise_name}, description: {self.description}")


if __name__ == '__main__':
    try:
        uri = f"cockroachdb://{os.environ['COCKROACH_ID']}@free-tier.gcp-us-central1.cockroachlabs.cloud:26257/activity?sslmode=verify-full&sslrootcert={os.environ['HOME']}/.postgresql/ca.crt&options=--cluster%3Dgolden-dingo-2123"
        engine = create_engine(uri)
    except Exception as e:
        print('Failed to connect to database.')
        print('{0}'.format(e))

    Base.metadata.create_all(engine)
