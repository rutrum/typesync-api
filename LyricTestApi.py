import lyricsgenius

genius = lyricsgenius.Genius('rk7Bf0CVL9lOWaEaxZnrOTIiAp2qXwMaKfJfWd3XPoLGGxAgJWz1zl1dwwgoCz17')
genius.remove_section_headers = True

def get_song_name(title, artist):
    song = genius.search_song(title, artist)
    print(song.lyrics)
    print(song.title)
    print(song.artist)

if __name__ == '__main__':
    get_song_name('Rap God', 'Eminem')