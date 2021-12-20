"""Notes Interface

Handles decoding notes and creating the output list
"""
from dataclasses import dataclass
from dataclasses import field

@dataclass(repr=False)
class Notes:
    entries : list[str] = field(default_factory=list, repr=False)
    _dict_flags = {
            "r" : "repeat reps",
            "d" : "Double Hand",
            "s" : "Single Arm/Side",
            "l" : "lap = 15 yd",
            "e" : "EMOM",
            "k" : "Keiser",
            "a" : "Alternating",
            "b" : "Double Bell"
        }

    ## Private functions
    def __init__(self):
        self.entries = list()

    
    def __repr__(self):
        first = True
        notes = ''
        for entry in self.entries:
            if first:
                notes = entry
            else:
                notes += f", {entry}"
            first = False
        return notes

    def __clear__(self):
        self.entries.clear

    def clear_notes(self):
        """Clears the notes

        """
        self.__clear__()

    def __add_note__(self, note : str):
        self.entries.append(note)

    def __decode_notes(self, note : str):
        """Converts note string from input to comma separted string 

        :param note: This coded string from the input
        :type note: str
        :return: the decoded notes in a comma sep string
        :rtype: str
        """
        decoded_notes = []
        first = True
        subscript = False
        for token in note:
            if subscript:
                decoded_notes += ('Superset ' + token if first else ', Superset ' + token)
                if first: first = False
                subscript = False
                continue
            if token == '_':
                subscript = True
                continue
            if token in self._dict_flags:
                decoded_notes += (self._dict_flags[token] if first else ', ' + self._dict_flags[token])
                if first: first = False
            else:
                decoded_notes += f" *{token}* "
        return decoded_notes        

    ## Public Functions
    def add_note(self, note : str):
        """Decodes the note string passed back to a list notes

        :param note: The string returned from the converter
        :type note: str
        :return: expanded string of 'english' notes
        :rtype: str
        """
        self.entries.__add_note__(note)

    def decode_notes(self, notes: list):
        """Decodes a series of shorthand notes into a series of english notes

        :param notes: the input series
        :type notes: list
        :return: A list of english strings from the decoded notes
        :rtype: list<str>
        
        Uses the following flags:

        "r" : "repeat reps",
        "d" : "Double Hand",
        "s" : "Single Arm/Side",
        "l" : "lap = 15 yd",
        "e" : "EMOM",
        "k" : "Keiser",
        "a" : "Alternating",
        "b" : "Double Bell"
        """
        notes_list = []
        for note in notes:
            notes_list.append(self.__decode_notes(note))
        return notes_list
