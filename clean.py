import re
import unicodedata

def standard_lyrics(l):
    l = remove_unicode(l)
    l = filter_characters(l)
    l = fix_whitespace(l)
    return split(l)

def simple_lyrics(l):
    l = remove_unicode(l)
    l = remove_punctuation(l)
    l = l.lower()
    l = fix_whitespace(l)
    return split(l)

def remove_unicode(lyrics):
    return unicodedata.normalize('NFKD', lyrics).encode('ascii', 'ignore').decode('utf-8')

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

    lines = lyrics.splitlines()


    thresh = 44

    new_lyrics = []
    for i, line in enumerate(lines):
        l = len(line)
        num_splits = l // thresh - 1

        for _ in range(num_splits):

            right = line[thresh:].find(" ")
            left = line[thresh::-1].find(" ")

            if right < left or (left == right and right > -1):
                first = line[:right+thresh]
                new_lyrics.append((i, first))
                line = line[right+thresh:]

            elif right > left:
                first = line[:thresh-left]
                new_lyrics.append((i, first))
                line = line[thresh-left:]

            elif left == -1 and right == -1:
                break

        if num_splits > 0:
            lines[i] = line

    print(new_lyrics)
    for (total, (i, lyric)) in enumerate(new_lyrics):
        lines.insert(i + total, lyric)

    return list(filter(
        lambda x: x != "",
        map(lambda x: x.strip(), lines)
    ))

    # Split long lines into small ones
