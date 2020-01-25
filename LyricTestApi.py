import lyricsgenius

genius = lyricsgenius.Genius('rk7Bf0CVL9lOWaEaxZnrOTIiAp2qXwMaKfJfWd3XPoLGGxAgJWz1zl1dwwgoCz17')
genius.remove_section_headers = True

def get_song_name(title, artist):

    # Use genius api to find song and convert to dictionary for indexing
    song = genius.search_song(title, artist)

    # Use this to see if search gave no results
    if song == None:
        return { 'status': 'not'} 

    song = song.__dict__["_body"]

    # See if search gave too many results
    if song["annotation_count"] > 5:
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
        'title': found_title,
        'artist': found_artist,
        'lyrics': lyrics
    }


def process_lyrics(lyrics):
    return lyrics.split("\n")
    return list(filter(lambda x: x != "", lyrics.split("\n")))


def main():
    song = get_song_name('Rap God', 'Eminem')
    print(song)

if __name__ == '__main__':
    main()