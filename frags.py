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