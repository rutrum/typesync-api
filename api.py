from flask import Flask, jsonify, request
app = Flask(__name__)

import LyricTestApi


@app.route('/lyrics/artist/<artist>/title/<title>')
def get_lyrics(artist, title):

    # Remove pipe delimeter
    artist = artist.replace("|", " ")
    title = title.replace("|", " ")

    response = LyricTestApi.get_song_name(title, artist)

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
    app.run()