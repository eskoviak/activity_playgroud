"""
        if inStr.count('r') == 1:
            mode = 'repeat'
            inStr = inStr.replace('r','')

        if inStr.count('d') == 1:
            if len(notes) == 0:
                notes = 'Double Hand'
            else:
                notes._add_(', Double Hand')
            inStr = inStr.replace('d', '')

        if inStr.count('s') == 1:
            if len(notes) == 0:
                notes = 'Single Hand'
            else:
                notes._add_(', Single Hand')
            inStr = inStr.replace('s', '')
"""


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

    """