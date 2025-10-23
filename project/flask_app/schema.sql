CREATE TABLE IF NOT EXISTS songs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    song_link TEXT NOT NULL,
    song_id TEXT NOT NULL,
    track_name TEXT,
    artist_name TEXT,
    album_image_url TEXT
);