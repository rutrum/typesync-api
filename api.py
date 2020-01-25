from flask import Flask, jsonify, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


import LyricTestApi
import Database


@app.route('/all/artist/<artist>/title/<title>')
def get_all_metadata(artist, title):

    # Remove pipe delimeter
    artist = artist.replace("|", " ")
    title = title.replace("|", " ")

    return jsonify(LyricTestApi.all_metadata(artist, title))


@app.route('/lyrics/artist/<artist>/title/<title>')
def get_lyrics(artist, title):

    # Remove pipe delimeter
    artist = artist.replace("|", " ")
    title = title.replace("|", " ")

    response = LyricTestApi.get_song_name(artist, title)

    return jsonify(response)


# @app.route('/score/artist/<artist>/title/<title>', methods=['GET'])
# def view_scores(artist, title):

#     # Remove pipe delimeter
#     artist = artist.replace("|", " ")
#     title = title.replace("|", " ")



#     response = {
#         'status': 'found',
#         'scores': [
#             {
#                 'name': 'brad',
#                 'score': '55'
#             },
#             {
#                 'name': 'benjamin',
#                 'score': '42'
#             }
#         ]
#     }

#     return jsonify(response)


# @app.route('/score/artist/<artist>/title/<title>', methods=['POST'])
# def save_score(artist, title):
#     data = request.get_json()

#     # Remove pipe delimeter
#     artist = artist.replace("|", " ")
#     title = title.replace("|", " ")

#     return "Saving " + data['name'] + "'s score of " + str(data['score']) + " on " + title + " by " + artist


@app.route('/score', methods=['POST'])
def save_score():
    data = request.get_json()

    genius_id = data["genius_id"]
    name = data["name"]
    time = data["time"]

    # db.save(genius_id, name, time)

    return


@app.route('/leaderboards/<genius_id>')
def leaderboards(genius_id):
    x = 1
    # select * from entries where genius_id = `genius_id` order by time ASC limit 10
    return

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)