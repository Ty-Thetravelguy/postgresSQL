from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

# executing the instructions from our localhost "chinook" dababase
db = create_engine("postgresql:///chinook")

meta = MetaData(db)

# create variable for "Artist" table
artist_table = Table(
    "artist", meta,
    Column("artist_id", Integer, primary_key=True),
    Column("name", String)
)

# create variable for "album" table
album_table = Table(
    "album", meta,
    Column("album_id", Integer, primary_key=True),
    Column("title", String),
    Column("artist_id", Integer, ForeignKey("artist.artist_id"))
)

# create variable for "track" table
track_table = Table(
    "track", meta,
    Column("track_id", Integer, primary_key=True),
    Column("name", String),
    Column("album_id", Integer, ForeignKey("album.album_id")),
    Column("media_type_id", Integer, primary_key=False),
    Column("genre_id", Integer, primary_key=False),
    Column("composer", String),
    Column("milliseconds", Integer),
    Column("bytes", Integer),
    Column("unit_price", Float)
)

# making the connection
with db.connect() as connection:

    # Query 1 - Select all records form the "artist" table
    # select_query = artist_table.select()

    # Query 2 - Select only the "name" column from the "artist" table
    # select_query = album_table.select().with_only_columns([artist_table.c.name])

    # Query 3 - Select only "Queen" form the "artist" table
    # select_query = artist_table.select().where(artist_table.c.name == "Queen")

    # Query 4 - Select only by "artist_id" #51 from the "artist" table
    # select_query = artist_table.select().where(artist_table.c.artist_id == 51)

    # Query 5 - Select only the albums with "artist_id" #51 on the "album" table
    # select_query = album_table.select().where(album_table.c.artist_id == 51)

    # Query 6 - Select all tracks where the composer is "Queen" form the "track" table
    select_query = track_table.select().where(track_table.c.composer == "Queen")

    results = connection.execute(select_query)
    for result in results:
        print(result)
