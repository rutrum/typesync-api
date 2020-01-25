from flask import Flask, jsonify, request
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/lyrics/artist/<artist>/song/<song>')
def get_lyrics(artist, song):

    # Remove pipe delimeter
    artist = artist.replace("|", " ")
    song = song.replace("|", " ")

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


@app.route('/score/artist/<artist>/song/<song>', methods=['GET'])
def view_scores(artist, song):

    # Remove pipe delimeter
    artist = artist.replace("|", " ")
    song = song.replace("|", " ")

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


@app.route('/score/artist/<artist>/song/<song>', methods=['POST'])
def save_score(artist, song):
    data = request.get_json()
    # return artist + song + data['name']
    # db.save_score(data['name'], data['score'])
    return "Saving " + data['name'] + "'s score of " + str(data['score']) + " on " + song + " by " + artist



if __name__ == '__main__':
    app.run()