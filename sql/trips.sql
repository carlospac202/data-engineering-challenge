CREATE TABLE IF NOT EXISTS trips
(
    id INTEGER PRIMARY KEY,
    region TEXT,
    origin_lat REAL,
    origin_lon REAL,
    destination_lat REAL,
    destination_lon REAL,
    datetime DATETIME,
    datasource TEXT
)