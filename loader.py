import csv, os
#from hashlib import new
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Factors, Exercises

class Loader:
    """ PRIVATE FUNCTIONS """
    def __init__(self):
        self._uri = f"postgresql+psycopg2://postgres@localhost/activity"

#    def __get_session(self):
#        """Gets a sessionmaker object
#        
#        Opens the cockroach instance based on the URL and returns the sessionmaker object which can be used by other routines.
#        """
#        return sessionmaker(bind=create_engine(self._uri))

    def __read_csv_file(self, filename : str ) -> dict:
        """reads the file into a internal dictionary

        :param filename; the FQN of the file to be read
        :type filename: str
        :return: a dictionary of the csv file
        :rtype: dict
        """
        
        return csv.DictReader(open(filename, newline='\n'), delimiter=',', dialect='excel')

    def __insert_factors(self, data : dict):
        new_factors = []
        for item in data:
            new_factors.append(Factors(
                reps = item['Reps'],
                factor = item['Factor']
                )
            )

        Session = sessionmaker(create_engine(self._uri))
        with Session.begin() as session:
            session.add_all(new_factors)



    #def __insert_exercises(self, s : sessionmaker, data : dict):
    #    new_exercises = []
    #    for item in data:
    #        new_exercises.append(Exercises(
    #            id = item['id'],
    #            exercise_name = item['exercise_name'],
    #            description = item['description']
    #        ))
    ##
    #    s.add_all(new_exercises)

    """ PUBLIC FUNCTIONS """ 
    def load_factors(self):
        """load_factors
        
            Transaction wrapper function for __insert_factors
            
        """

        return self.__insert_factors(self.__read_csv_file('data/ORM Factors.csv'))

    #def load_exercises(self):
    #    """load_exercises
    #    
    #        Transaction wrapper for __insert_exercises
    #    """
    #    return run_transaction(self.__get_session(), 
    #        lambda s : self.__insert_exercises(s, self.__read_csv_file('data/exercises.csv')) )
