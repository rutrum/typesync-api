# API for the Lyric Typing Website thing for BoilerMakeVII

Manages the database stuff and the lyric api stuff for the front end stuff.

## Routes

### `GET /lyrics/artist/<artist>/song/<song>`

Searches for lyrics of the song `song` by `artist`.

### `GET /scores/artist/<artist>/song/<song>`

Searches for previous scores of the song `song` by `artist`.

### `POST /scores`

Allows the user to update scores into the database.