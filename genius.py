import lyricsgenius

# Local files for cleaning lyrics and determining stats
import clean
import stats

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

    std_lyrics = clean.standard_lyrics(song["lyrics"])
    std_stat = stats.get(std_lyrics)
    std_diff = stats.determine_difficulty(std_stat)

    simple_lyrics = clean.simple_lyrics(song["lyrics"])
    simple_stat = stats.get(simple_lyrics)
    simple_diff = stats.determine_difficulty(simple_stat)
    

    return {
        'status': 'found',
        'genius_id': uuid,
        'title': found_title,
        'artist': found_artist,
        'standard': {
            'lyrics': std_lyrics,
            'stats': std_stat,
            'diff': std_diff
        },
        'simple': {
            'lyrics': simple_lyrics,
            'stats': simple_stat,
            'diff': simple_diff
        },
        'album_art_url': album_art,
    }
