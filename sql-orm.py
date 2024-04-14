from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from our localhost "chinook" dababase
db = create_engine("postgresql:///chinook")
base = declarative_base()


#create a class-based model for the "artist" table
class Artist(base):
    __tablename__ = "artist"
    artist_id = Column(Integer, primary_key=True)
    name = Column(String)


# create a class-based model for the "Album" table
class Album(base):
    __tablename__ = "album"
    album_id = Column(Integer, primary_key=True)
    title = Column(String)
    artist_id = Column(Integer, ForeignKey("Artist.artist_id"))


# create a class-based model for the "Track" table
class Track(base):
    __tablename__ = "track"
    track_id = Column(Integer, primary_key=True)
    name = Column(String)
    album_id = Column(Integer, ForeignKey("Album.album_id"))
    media_type_id = Column(Integer, primary_key=False)
    genre_id = Column(Integer, primary_key=False)
    composer = Column(String)
    milliseconds = Column(Integer, primary_key=False)
    bytes = Column(Integer, primary_key=False)
    unit_price = Column(Float)


# instead of connecting to the database directl;y, we will ask for a session 
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
#open an actuaal session by callin the Session() subclass defined above
session = Session()


# creating the database using declarative_base subclass
base.metadata.create_all(db)


# Query 1 - Select all records form the "artist" table
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.artist_id, artist.name, sep=" | ")

# Query 2 - Select only the "name" column from the "artist" table
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.name)

# Query 3 - Select only "Queen" form the "artist" table
# artist = session.query(Artist).filter_by(name="Queen").first()
# print(artist.artist_id, artist.name, sep=" | ")

# Query 4 - Select only by "artist_id" #51 from the "artist" table
# artist = session.query(Artist).filter_by(artist_id=51).first()
# print(artist.artist_id, artist.name, sep=" | ")

# Query 5 - Select only the albums with "artist_id" #51 on the "album" table
# albums = session.query(Album).filter_by(artist_id=51)
# for album in albums:
#     print(album.album_id, album.title, album.artist_id, sep=" | ")

# Query 6 - select all tracks where the composer is "Queen" form the "track" table
tracks = session.query(Track).filter_by(composer="Queen")
for track in tracks:
    print(
        track.track_id, 
        track.name, 
        track.album_id, 
        track.media_type_id, 
        track.genre_id, 
        track.composer, 
        track.milliseconds, 
        track.bytes, 
        track.unit_price, 
        sep=" | "
    )