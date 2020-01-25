from flask import Flask, jsonify, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

import LyricTestApi


@app.route('/lyrics/artist/<artist>/title/<title>')
def get_lyrics(artist, title):

    # Remove pipe delimeter
    artist = artist.replace("|", " ")
    title = title.replace("|", " ")

    lyrics = LyricTestApi.get_song_name(title, artist)

    response = {
        'status': 'found',
        'lyrics': [
            "Jump back, what's that sound",
            "Here she comes, full blast and top down",
            "Hot shoe, burnin' down the avenue",
            "Model citizen zero discipline"
        ]
    }

    return jsonify(response)


@app.route('/score/artist/<artist>/title/<title>', methods=['GET'])
def view_scores(artist, title):

    # Remove pipe delimeter
    artist = artist.replace("|", " ")
    title = title.replace("|", " ")

    response = {
        'status': 'found',
        'scores': [
            {
                'name': 'brad',
                'score': '55'
            },
            {
                'name': 'benjamin',
                'score': '42'
            }
        ]
    }

    return jsonify(response)


@app.route('/score/artist/<artist>/title/<title>', methods=['POST'])
def save_score(artist, title):
    data = request.get_json()

    # Remove pipe delimeter
    artist = artist.replace("|", " ")
    title = title.replace("|", " ")

    return "Saving " + data['name'] + "'s score of " + str(data['score']) + " on " + title + " by " + artist


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)