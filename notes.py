"""Notes Utility Class

Handles decoding notes and creating the output string
"""
from dataclasses import dataclass
from dataclasses import field

@dataclass(repr=False)
class Notes:
    entries : list[str] = field(default_factory=list, repr=False)
    dict_flags = {
            "r" : "repeat reps",
            "d" : "Double Hand",
            "s" : "Single Hand",
            "l" : "lap = 15 yd",
            "e" : "EMOM",
            "k" : "Keiser",
            "a" : "Alternating",
            "_" : "Superset"
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
        self.__clear__()

    def __add_note__(self, note : str):
        self.entries.append(note)

    ## Public Functions
    def add_note(self, note : str):
        """Decodes the note string passed back to a list notes

        :param note: The string returned from the converter
        :type note: str
        :return: expanded string of 'english' notes
        :rtype: str

        """
        self.entries.__add_note__(note)