'''Activity Interface

Classes
=======

Activity


Functions
=========

SearchExcercises

'''
from sqlalchemy.orm import sessionmaker, session
from sqlalchemy import create_engine, or_
from sqlalchemy_cockroachdb import run_transaction
from models import Factors, Exercises, Categories

import numpy as np, os, re

class Activty:

    """Private Functions"""
    def __init__(self):
        self._uri = f"cockroachdb://{os.environ['COCKROACH_ID']}@free-tier.gcp-us-central1.cockroachlabs.cloud:26257/activity?sslmode=verify-full&sslrootcert={os.environ['HOME']}/.postgresql/ca.crt&options=--cluster%3Dgolden-dingo-2123"

    def __get_session(self):
        """Gets a sessionmaker object
        
        Opens the cockroach instance based on the URL and returns the sessionmaker object which can be used by other routines.  This is a 
        private function to be called internally.

        Returns:
        sessionmaker object
        """
        return sessionmaker(bind=create_engine(self._uri))

    def __search_exercises(self, s : sessionmaker, phrase : str) -> dict():
        """searches excercies for the phrase

        Searches the exercises table (exercise_name and description) for the 
        indicated phrase.  Interanl function

        Returns
        -------
        A dictionary of the id, excercise_name and description
        """
        return s.query(Exercises).filter(or_(Exercises.exercise_name.ilike(f"%{phrase}%"), Exercises.description.ilike(f"%{phrase}%")))


    """Public Functions"""

    def search_exercises(self, phrase : str):
        """public wrapper for __search_exercises
        
        """
        return run_transaction(self.__get_session(),
            lambda s: self.__search_exercises(s, phrase))
