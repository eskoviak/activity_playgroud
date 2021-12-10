import csv, os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy_cockroachdb import run_transaction
from models import Factors, Exercises, Categories

class Loader:
    """ PRIVATE FUNCTIONS """
    def __init__(self):
        self._uri = f"cockroachdb://{os.environ['COCKROACH_ID']}@free-tier.gcp-us-central1.cockroachlabs.cloud:26257/activity?sslmode=verify-full&sslrootcert={os.environ['HOME']}/.postgresql/ca.crt&options=--cluster%3Dgolden-dingo-2123"


    def __get_session(self):
        """Gets a sessionmaker object
        
        Opens the cockroach instance based on the URL and returns the sessionmaker object which can be used by other routines.
        """
        return sessionmaker(bind=create_engine(self._uri))

    def __read_csv_file(self, filename : str ) -> dict:
        
        return csv.DictReader(open(filename, newline='\n'), delimiter=',', dialect='excel')

    def __insert_factors(self, s : sessionmaker, data : dict):
        new_factors = []
        for item in data:
            new_factors.append(Factors(
                reps = item['reps'],
                factor = item['factor']
            ))

        s.add_all(new_factors)

    def __insert_exercises(self, s : sessionmaker, data : dict):
        new_exercises = []
        for item in data:
            new_exercises.append(Exercises(
                id = item['id'],
                exercise_name = item['exercise_name'],
                description = item['description']
            ))

        s.add_all(new_exercises)

    """ PUBLIC FUNCTIONS """ 
    def load_factors(self):
        """load_factors
        
            Transaction wrapper function for __insert_factors
            
        """
        return run_transaction(self.__get_session(), 
            lambda s : self.__insert_factors(s, self.__read_csv_file('data/factors.csv')) )

    def load_exercises(self):
        """load_exercises
        
            Transaction wrapper for __insert_exercises
        """
        return run_transaction(self.__get_session(), 
            lambda s : self.__insert_exercises(s, self.__read_csv_file('data/exercises.csv')) )
