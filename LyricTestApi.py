import lyricsgenius
import re
import string


genius = lyricsgenius.Genius('rk7Bf0CVL9lOWaEaxZnrOTIiAp2qXwMaKfJfWd3XPoLGGxAgJWz1zl1dwwgoCz17')
genius.remove_section_headers = True


def all_metadata(artist, title):
    song = genius.search_song(title, artist)
    if song == None:
        return None
    else: 
        return song.__dict__


def get_song_by_id(id):
    song = genius.get_song(id)["song"]

    # Use this to see if search gave no results
    if song == None:
        return { 'status': 'not'} 

    uuid = id

    found_title = song["title"]
    found_artist = song["primary_artist"]["name"]
    album_art = song["header_image_url"]
    
    return {
        'status': 'found',
        'genius_id': uuid,
        'title': found_title,
        'artist': found_artist,
        'album_art_url': album_art
    }


def get_song_name(artist, title):

    # Use genius api to find song and convert to dictionary for indexing
    song = genius.search_song(title, artist)

    # Use this to see if search gave no results
    if song == None:
        return { 'status': 'not'} 

    uuid = song.__dict__["_id"]
    
    song = song.__dict__["_body"]

    found_title = song["title"]
    found_artist = song["primary_artist"]["name"]
    album_art = song["header_image_url"]

    normal = normal_lyrics(song["lyrics"])

    total_char = -1 # ignoring final newline
    for lyric in normal:
        total_char += len(lyric) + 1 # add for newline
    
    return {
        'status': 'found',
        'genius_id': uuid,
        'title': found_title,
        'artist': found_artist,
        'lyrics': normal,
        'album_art_url': album_art,
        'total_char': total_char,
        'stats': stats(normal)
    }

def normal_lyrics(l):
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
    lyrics = re.sub('[ ]$', '\n', lyrics)
    lyrics = re.sub('^[ ]', '\n', lyrics)
    return lyrics

# Splits lyrics by newlines and removes empty lines
def filter_characters(lyrics):
    return re.sub('[^A-Za-z0-9().,\s'"'"'!?]+','' , lyrics)

def remove_punctuation(lyrics):
    return re.sub('[^A-Za-z\s]+', '', lyrics)

# Split based on newline and remove empty lines
def split(lyrics):
    return list(filter(lambda x: x != "", lyrics.split("\n")))


# Returns stats on the lyrics
# * Number of characters
# * Number of upper case letters
# * Number of punctuation marks
# * Number of digits
# * Number of whitespace characters
def stats(lyrics):
    stats = {
        'total': 0,
        'upper': 0,
        'lower': 0,
        'digit': 0,
        'white': 0,
        'punc': 0,
    }

    for lyric in lyrics:
        for char in lyric:
            stats['total'] += 1
            if char.isspace(): 
                stats['white'] += 1
                continue
            if char.isdigit(): 
                stats['digit'] += 1
                continue
            if char in string.punctuation: 
                stats['punc'] += 1
                continue
            if char.islower(): 
                stats['lower'] += 1
                continue
            if char.isupper(): 
                stats['upper'] += 1

    return stats

if __name__ == '__main__':
    main()