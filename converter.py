"""Converter Interface

Contains the converter class, which provides utilities to convert the input csv file into series for use in analysis.

"""
import re
import numpy as np
from dataclasses import dataclass
@dataclass
class Converter:

    def __init__(self):
        self._multipler_regex = re.compile('^\d*(?=x)')
        self._sequence_regex = re.compile('(?<=x)(\()?([0-9.]([,\s])*)+(\))?')
        self._flag_regex = re.compile('(?<=\))([a-zA-Z]*)(_[a-z])?')
        self._ladder_op_regex = re.compile('[>]')


    ### Private Functions
    def __get_series(self, cadence_str : str):
        """converts the input string into a series (list)

        Args:
            self ([object pointer]): [reference to this class]

        Returns:
            (list, str) : the first list is the nd.series ready parsed from the notation, the second is a list of flags found
        """
        #str_flags = None
        list_cadence = []

        #flags = re.search(self._flag_regex, cadence_str)
        #if flags: str_flags = flags.group(0)

        for token in self.__tokenize(cadence_str):
            list_cadence.extend(self.__parseOperators(token))
        return (list_cadence)

    def __tokenize(self, inStr):
        """tokenize
        
        Breaks the string on the the + character
        
        """
        if inStr.find('+') > -1:
            return inStr.split('+')
        else:
            return [inStr]

           
    def __parseOperators(self, inStr : str) -> list:
        """Parse Operators
        
        Takes a notation string from the input, and attempts to creat an np.series based on the notation.  This is used
        for either the cadence or the weights field.

        Args:
        inStr (str) : the input notation

        Returns:
        list (np.series) : the converted string

        """
        multiplier = re.match(self._multipler_regex, inStr)
        if not multiplier: 
            rstring = (f"x({inStr})").replace('((', '(').replace('))', ')')
        else: rstring = inStr
        rstring = rstring.replace(')', ',)').replace(',,', ',')
        ladder = re.search(self._ladder_op_regex, rstring)
        if ladder:
            #end = re.match(r'(?<=->)\d+', rstring)
            start =  re.search(r'(?=>)[0-9]+', rstring)
            print (start)
            return( [] )
        sequence = re.search(self._sequence_regex, rstring)
        if not sequence:
            """ Check to see if the text 'BW' 
                Weights only
            """
            if sequence := re.search(r'BW', rstring):
                return ( ['BW'])
            else: return( [] )
        return (np.tile(list(eval(sequence.group(0))), int(multiplier.group(0) if multiplier else 1)))

    """Public Functions"""
    def get_series(self, notations : list):
        """convert the notation list to a np.series.

        :param notations: the field as entered in the incoming csv
        :type notations: list
        :return: np.series
        :rtype: list<list>
        
        """
        series = []
        for item in notations:
            series.append(self.__get_series(item))

        return series
