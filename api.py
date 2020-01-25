from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/lyrics/artist/<artist>/song/<song>')
def get_lyrics(artist, song):
    return artist + song


@app.route('/score/artist/<artist>/song/<song>', methods=['GET'])
def view_scores(artist, song):
    return "scores from " + artist + song


@app.route('/score', methods=['POST'])
def save_score():
    # Something about getting json data
    return "todo!"


if __name__ == '__main__':
    app.run()