import lyricsgenius


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

    # return song

    # Use this to see if search gave no results
    if song == None:
        return { 'status': 'not'} 

    uuid = id

    # See if search gave too many results
    #if song["annotation_count"] > 50:
    #   return { 'status': 'not'} 

    found_title = song["title"]
    found_artist = song["primary_artist"]["name"]
    album_art = song["header_image_url"]

    # See if song is instrumental
    # if song["instrumental"]:
    #     return { 
    #         'status': 'instrumental',
    #         'genius_id': uuid,
    #         'title': found_title,
    #         'artist': found_artist,
    #         'album_art_url': album_art
    #     }

    # lyrics = process_lyrics(song["lyrics"])

    # total_char = -1 # ignoring final newline
    # for lyric in lyrics:
    #     total_char += len(lyric) + 1 # add for newline
    
    return {
        'status': 'found',
        'genius_id': uuid,
        'title': found_title,
        'artist': found_artist,
        #'lyrics': lyrics,
        'album_art_url': album_art,
        #'total_char': total_char
    }


def get_song_name(artist, title):

    # Use genius api to find song and convert to dictionary for indexing
    song = genius.search_song(title, artist)

    # Use this to see if search gave no results
    if song == None:
        return { 'status': 'not'} 

    uuid = song.__dict__["_id"]
    
    song = song.__dict__["_body"]

    # See if search gave too many results
    #if song["annotation_count"] > 50:
    #    return { 'status': 'not'} 

    found_title = song["title"]
    found_artist = song["primary_artist"]["name"]
    album_art = song["header_image_url"]

    # See if song is instrumental
    if song["instrumental"]:
        return { 
            'status': 'instrumental',
            'genius_id': uuid,
            'title': found_title,
            'artist': found_artist,
            'album_art_url': album_art
        }

    lyrics = process_lyrics(song["lyrics"])

    total_char = -1 # ignoring final newline
    for lyric in lyrics:
        total_char += len(lyric) + 1 # add for newline
    
    return {
        'status': 'found',
        'genius_id': uuid,
        'title': found_title,
        'artist': found_artist,
        'lyrics': lyrics,
        'album_art_url': album_art,
        'total_char': total_char
    }


# Splits lyrics by newlines and removes empty lines
def process_lyrics(lyrics):
    no_empty = list(filter(lambda x: x != "", lyrics.split("\n")))
    # todo: regex to remove all weird characters
    return no_empty


if __name__ == '__main__':
    main()