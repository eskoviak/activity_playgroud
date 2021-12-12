"""cadence module

Used to process the cadence and weight notation found in the .csv file

"""
import re
import numpy as np

class Cadence:

    def __init__(self):
        self._dict_flags = {
            "r" : "repeat reps",
            "d" : "Double Hand",
            "s" : "Single Hand",
            "l" : "lap = 15 yd",
            "e" : "EMOM"
        }
        self._notes  = ''
        self._multipler_regex = re.compile('^\d*(?=x)')
#        self._sequence_regex = re.compile('(?<=x)(\()?(\w([,\s])*)+(\))?')
        self._sequence_regex = re.compile('(?<=x)(\()?([0-9.]([,\s])*)+(\))?')
        self._flag_regex = re.compile('(?<=\))[a-zA-Z]+')


    """Private Functions"""
    def __get_cadence(self, cadence_str : str) -> list():
        """converts the input string into a series (list)

        Args:
            self ([object pointer]): [reference to this class]

        Returns:
            [(list)]: [a list (series) expanded to include the total number of moves]
        """
        list_cadence = []
        for token in self.__tokenize(cadence_str):
            list_cadence.extend(self.__parseOperators(token))
        return list_cadence

    def __tokenize(self, inStr):
        """tokenize
        
        Breaks the string on the the + character
        
        """
        if inStr.find('+') > -1:
            return inStr.split('+')
        else:
            return [inStr]

    def __clear_notes(self):
        self._notes = ''

    def __get_notes(self):
        return self._notes
        
    def __add_note(self, note):
        if len(self._notes) == 0:
            self._notes = note
        else:
            self._notes += ', ' + note

        
    def __parseOperators(self, inStr : str) -> list:
        """Parse Operators
        
        Takes a notation string from the input, and attempts to creat an np.serices based on the notation.  This is used
        for either the cadence or the weights field.  It also maintains the notes for that line.  Note:  The caller is 
        responsible for clearing the notes, as this function may be called multiple times per line.

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
        sequence = re.search(self._sequence_regex, rstring)
        if not sequence:
            """ Check to see if the text 'BW' 
                Weights only
            """
            if sequence := re.search(r'BW', rstring):
                self.__add_note('Body Weight')
                return ( [] )
        if not sequence:
            """ Bail """
            self.__add_note('Unknown notation')
            return ( [] )
        flags = re.search(self._flag_regex, rstring)

        """ Check the flags """
        if flags:
            for flag in flags.group(0):
                if flag in self._dict_flags:
                    #if flag == 'r': mode = 'repeat'
                    self.__add_note(self._dict_flags[flag])
                else:
                    raise NameError


        # need to check to see if set has an operator embedded
        """
        if set.count('-->') == 1:
            start, stop = set.split('-->')
            start = int(re.sub('\(','',start))
            stop = int(re.sub('\)','',stop))
            if stop < start:
                step = -1
                stop -= 1
            else:
                step = 1
                stop += 1
            set = np.arange(start, stop, step)
        else:
            # otherwise, evaluate set
            set = list(eval(set))
        

        if mode == 'tile':
            outList = np.tile(list(eval(sequence.group(0))), int(multiplier.group(0) if multiplier else 1))
        elif mode == 'repeat':
            outList = np.repeat(list(eval(sequence.group(0))), int(multiplier.group(0) if multiplier else 1))
        """
        return (np.tile(list(eval(sequence.group(0))), int(multiplier.group(0) if multiplier else 1)))

    """Public Functions"""
    def get_cadence(self, notation : str) -> list:
        return self.__get_cadence(notation)

    def clear_notes(self):
        self.__clear_notes()

    def print_notes(self):
        return self.__get_notes()