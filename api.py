from flask import Flask, jsonify, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
import re

import LyricTestApi
import Database as db


@app.route('/all/artist/<artist>/title/<title>')
def get_all_metadata(artist, title):

    # Remove pipe delimeter
    artist = artist.replace("|", " ")
    title = title.replace("|", " ")

    print(LyricTestApi.all_metadata(artist, title))
    return jsonify(LyricTestApi.all_metadata(artist, title))


@app.route('/lyrics/artist/<artist>/title/<title>')
def get_lyrics(artist, title):

    # Remove pipe delimeter
    artist = artist.replace("|", " ")
    title = title.replace("|", " ")

    response = LyricTestApi.get_song_name(artist, title)
    print(response)
    for index, value in enumerate(response['lyrics']):
        response['lyrics'][index]= re.sub("[^A-Za-z0-9().,\s'!?]+",'' , value)

    return jsonify(response)

@app.route('/song/<id>')
def get_song(id):
    return LyricTestApi.get_song_by_id(id)


@app.route('/score', methods=['POST'])
def save_score():
    data = request.get_json()

    genius_id = data["genius_id"]
    name = data["name"]
    user_time = data["time"]

    import time
    millis = int(round(time.time() * 1000)) # math because time.time() is bad

    db.add_new_score(name, genius_id, millis, user_time, 0)

    return { 'status': 'success' }


@app.route('/leaderboards/<genius_id>/limit/<limit>')
def leaderboards(genius_id, limit):
    return db.get_song_leaderBoard(genius_id, limit)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)