
# useful constants and character sets
BACKSLASH = r'\_'[0]
BANNER_LINE = r'% ' + '-' * 78
SPECIAL_CHARS = r'\#$%^&_{}~'
NON_ENCAPSULATION_CHARS = SPECIAL_CHARS + r' '
FONT_SIZES = ['8pt', '9pt', '10pt', '11pt', '12pt', '14pt', '17pt', '20pt']


def is_float(value):
    '''Returns if a value can be converted to float'''

    try:
        float(value)
        return True

    except ValueError:
        return False