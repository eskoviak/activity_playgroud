'''Activity Interface

This module contains the Activity class, which provides interfaces for interacting with the activity application
'''
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, or_
from models import Factors, Exercises
from dataclasses import dataclass

#import numpy as np

@dataclass
class Activty:

    ### Private Functions
    def __init__(self):
        """creates the uri to connect
        """
        self._uri = f"postgresql+psycopg2://postgres@localhost/activity"

#    def _get_session(self):
#        """Gets a sessionmaker object
#        
#        Opens the cockroach instance based on the URL and returns the sessionmaker object which can be used by other routines.  This is a 
#        private function to be called internally.
#
#        Returns:
#        sessionmaker object
#       """
#        return sessionmaker(bind=create_engine(self._uri))

#    def _search_exercises(self, s : sessionmaker, phrase : str) -> dict():
#        """searches excercies for the phrase
#
#        Searches the exercises table (exercise_name and description) for the 
#        indicated phrase.  Interanl function
#
#        Returns
#        -------
#        A dictionary of the id, excercise_name and description
#        """
#        return s.query(Exercises).filter(or_(Exercises.exercise_name.ilike(f"%{phrase}%"), Exercises.description.ilike(f"%{phrase}%")))


    ## Public Functions
    def search_exercises(self, phrase : str):
        """Search the exercises database for a exercises which contain the search phrase.

        :param phrase:  The string to search for
        :type phrase: str
        :return: A dictiony of the id, name and description of the exercise
        :rtype: list<dict>

        The return object(s) in the list have the following format:

        Exercise(id: <id>, exercise_name: <name>, description: <description>)
        """
        #return self._search_exercises(self._get_session(), phrase)
        with Session(create_engine(self._uri)) as session:
            results = session.query(Exercises).filter(or_(Exercises.exercise_name.ilike(f"%{phrase}%"), Exercises.description.ilike(f"%{phrase}%")))
        return results
