import re

def standard_lyrics(l):
    l = filter_characters(l)
    l = fix_whitespace(l)
    return split(l)

def simple_lyrics(l):
    l = remove_punctuation(l)
    l = l.lower()
    l = fix_whitespace(l)
    return split(l)

def fix_whitespace(lyrics):
    # Remove double spaces
    lyrics = re.sub('[ ]{2,}', ' ', lyrics)

    # Remove whitespace at beginning and end of lines
    lyrics = re.sub('^[ ]{1,}', '', lyrics)
    lyrics = re.sub('[ ]{1,}$', '', lyrics)
    return lyrics

# Splits lyrics by newlines and removes empty lines
def filter_characters(lyrics):
    return re.sub('[^A-Za-z0-9().,\s'"'"'!?]+','' , lyrics)

def remove_punctuation(lyrics):
    return re.sub('[^A-Za-z\s]+', '', lyrics)

# Split based on newline and remove empty lines
def split(lyrics):
    # Try to remove this map function sometime and
    # write better regex thx
    return list(map(lambda x: x.strip(), filter(lambda x: x != "", lyrics.splitlines())))