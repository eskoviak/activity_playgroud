"""Converter interface

Contains the converter class, which provides utilities to convert the input csv file into series for use in analysis.

"""
import re
import numpy as np

class Converter:

    def __init__(self):
        self._multipler_regex = re.compile('^\d*(?=x)')
        self._sequence_regex = re.compile('(?<=x)(\()?([0-9.]([,\s])*)+(\))?')
        self._flag_regex = re.compile('(?<=\))([a-zA-Z]*)(_[a-z])?')


    ### Private Functions
    def __get_series(self, cadence_str : str):
        """converts the input string into a series (list)

        Args:
            self ([object pointer]): [reference to this class]

        Returns:
            (list, str) : the first list is the nd.series ready parsed from the notation, the second is a list of flags found
        """
        str_flags = None
        list_cadence = []

        flags = re.search(self._flag_regex, cadence_str)
        if flags: str_flags = flags.group(0)

        for token in self.__tokenize(cadence_str):
            list_cadence.extend(self.__parseOperators(token))
        return (list_cadence, str_flags)

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
        notes (Notes) : A Notes object for capturing notes during parsing


        Returns:
        list (np.series) : the converted string
            
        """
        multiplier = re.match(self._multipler_regex, inStr)
        if not multiplier: 
            rstring = (f"x({inStr})").replace('((', '(').replace('))', ')')
        else: rstring = inStr
        rstring = rstring.replace(')', ',)').replace(',,', ',')
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
    def get_series(self, notation : str):
        """convert the notation to a list ready to be converted to a np.series.  Also expand the short-hand
        flags to a list of notes

        :param notation: the field as entered in the incoming csv
        :type notation: str
        :return: (notation, notes)
        :rtype: tuple<list, list>
        """
        return self.__get_series(notation)
