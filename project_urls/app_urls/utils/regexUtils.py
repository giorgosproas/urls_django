import re

def isValidShortcode(shortcode):
    pattern = re.compile('^[a-zA-Z0-9_]{6}$')
    if pattern.match(shortcode)==None:
        return False
    else:
        return True