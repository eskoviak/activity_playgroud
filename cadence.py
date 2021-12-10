"""cadence module

Used to process the cadences found in the .csv file

"""
import re
import numpy as np

class Cadence:

    def __init__(self):
        self._dict_flags = {
            "r" : "repeat reps",
            "d" : "Double Hand",
            "s" : "Single Hand"
        }
        self._notes  = ''


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

    def __add_note(self, note):
        if len(self._notes) == 0:
            self._notes = note
        else:
            self._notes = ', ' + note

        
    def __parseOperators(self, inStr : str) -> ( list, str ):
        outList = []
        self._notes = ''
        mode = 'tile'  """default"""

        """Check to see if the notation is enclosed in (..)"""

        """Pick off the flags
        
        The flags are appended to the end of the string after the closing parenthesis (if present)

        """
        flags = inStr.split(')')[1]
        for flag in flags:
            if flag in self._dict_flags:
                if flag == 'r':
                    mode = 'repeat'
                self.__add_note(self._dict_flags[flag])
                inStr = inStr.replace(flag, '')
            else:
                raise NameError

        inStr.replace('*','x')
        
        if inStr.count('x') == 0:
            # basic Set
            mult = 1
            set=inStr
        else:
            (mult, set) = inStr.split('x')

        # need to check to see if set has an operator embedded
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
            outList= np.tile(set, int(mult))
        elif mode == 'repeat':
            outList = np.repeat(set, int(mult))

        return (outList, self._notes)

    """Public Functions"""
    def get_cadence(self, notation : str) -> list:
        return self.__get_cadence(notation)