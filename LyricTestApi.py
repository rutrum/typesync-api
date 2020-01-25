import lyricsgenius


genius = lyricsgenius.Genius('rk7Bf0CVL9lOWaEaxZnrOTIiAp2qXwMaKfJfWd3XPoLGGxAgJWz1zl1dwwgoCz17')
genius.remove_section_headers = True


def all_metadata(artist, title):
    song = genius.search_song(title, artist)
    if song == None:
        return None
    else: 
        return song.__dict__


def get_song_name(artist, title):

    # Use genius api to find song and convert to dictionary for indexing
    song = genius.search_song(title, artist)

    # Use this to see if search gave no results
    if song == None:
        return { 'status': 'not'} 

    uuid = song.__dict__["_id"]
    
    song = song.__dict__["_body"]

    # See if search gave too many results
    if song["annotation_count"] > 50:
        return { 'status': 'not'} 

    # See if song is instrumental
    if song["instrumental"]:
        return { 'status': 'instrumental' }

    found_title = song["title"]
    found_artist = song["primary_artist"]["name"]
    lyrics = song["lyrics"]

    lyrics = process_lyrics(lyrics)
    
    return {
        'status': 'found',
        'id': uuid,
        'title': found_title,
        'artist': found_artist,
        'lyrics': lyrics
    }


# Splits lyrics by newlines and removes empty lines
def process_lyrics(lyrics):
    return list(filter(lambda x: x != "", lyrics.split("\n")))


if __name__ == '__main__':
    main()