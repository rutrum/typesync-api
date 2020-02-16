# API for the Lyric Typing Website thing for BoilerMakeVII

Manages the database stuff and the lyric api stuff for the front end stuff.

## Routes

### `GET /lyrics/artist/<artist>/song/<song>`

Searches for lyrics of the song `song` by `artist`.  Returns an object with the key `status` that is either "not" or "found".  If it is found, the key `lyrics` contains an array of strings where each string is a single line of the lyrics.

### `GET /scores/artist/<artist>/song/<song>`

Searches for previous scores of the song `song` by `artist`.  Returns an object with the key `status` that is either "not" or "found".  If it is found, the key `scores` returns an array of objects that contain `name` and `score` keys.

### `POST /scores/artist/<artist>/song/<song>`

Allows the user to update scores into the database.  Expects a json object with the key `name`, `score`.  Returns an object with the key `status` that is either `success` or `failure`.  If `failure`, there is a `message` key with a description of the error.

## Docker
```
docker build -t typesync/api .
docker run -d -p 8080:8080 --network host typesync/api
```
