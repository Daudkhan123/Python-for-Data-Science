from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

# for creating the sqlalchemy tables
# sqlalchemy is an ORM for python.

engine = create_engine('sqlite:///mymusic.db', echo=True)
Base = declarative_base()

class Artist(Base):
    """"""
    __tablename__ = "artists"

    id = Column(Integer, primary_key=True)
    name = Column(String)

class Album(Base):
    """"""
    __tablename__ = "albums"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    release_date = Column(Date)
    publisher = Column(String)
    media_type = Column(String)

    artist_id = Column(Integer, ForeignKey("artists.id"))
    artist = relationship("Artist", backref=backref("albums", order_by=id))

# create tables
Base.metadata.create_all(engine)

# for adding the records in the table

# add_data.py
import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from table_def import Album, Artist

engine = create_engine('sqlite:///mymusic.db', echo=True)

# create a Session
Session = sessionmaker(bind=engine)
session = Session()

# Create an artist
new_artist = Artist(name="Newsboys")

new_artist.albums = [Album(title="Read All About It",
                           release_date=datetime.date(1988,12,1),
                           publisher="Refuge", media_type="CD")]

# add more albums
more_albums = [Album(title="Hell Is for Wimps",
                     release_date=datetime.date(1990,7,31),
                     publisher="Star Song", media_type="CD"),
               Album(title="Love Liberty Disco",
                     release_date=datetime.date(1999,11,16),
                     publisher="Sparrow", media_type="CD"),
               Album(title="Thrive",
                     release_date=datetime.date(2002,3,26),
                     publisher="Sparrow", media_type="CD")]
new_artist.albums.extend(more_albums)

# Add the record to the session object
session.add(new_artist)
# commit the record the database
session.commit()

# Add several artists
session.add_all([
    Artist(name="MXPX"),
    Artist(name="Kutless"),
    Artist(name="Thousand Foot Krutch")
    ])
session.commit()

#update records
# add_data.py
import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from table_def import Album, Artist

engine = create_engine('sqlite:///mymusic.db', echo=True)

# create a Session
Session = sessionmaker(bind=engine)
session = Session()

# Create an artist
new_artist = Artist(name="Newsboys")

new_artist.albums = [Album(title="Read All About It",
                           release_date=datetime.date(1988,12,1),
                           publisher="Refuge", media_type="CD")]

# add more albums
more_albums = [Album(title="Hell Is for Wimps",
                     release_date=datetime.date(1990,7,31),
                     publisher="Star Song", media_type="CD"),
               Album(title="Love Liberty Disco",
                     release_date=datetime.date(1999,11,16),
                     publisher="Sparrow", media_type="CD"),
               Album(title="Thrive",
                     release_date=datetime.date(2002,3,26),
                     publisher="Sparrow", media_type="CD")]
new_artist.albums.extend(more_albums)

# Add the record to the session object
session.add(new_artist)
# commit the record the database
session.commit()

# Add several artists
session.add_all([
    Artist(name="MXPX"),
    Artist(name="Kutless"),
    Artist(name="Thousand Foot Krutch")
    ])
session.commit()

# how to delete the records

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from table_def import Album, Artist

engine = create_engine('sqlite:///mymusic.db', echo=True)

# create a Session
Session = sessionmaker(bind=engine)
session = Session()

res = session.query(Artist).filter(Artist.name=="MXPX").first()

session.delete(res)
session.commit()

# Reterival of the data from the sqlalchemy database

# queries.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from table_def import Album, Artist

engine = create_engine('sqlite:///mymusic.db', echo=True)

# create a Session
Session = sessionmaker(bind=engine)
session = Session()

# how to do a SELECT * (i.e. all)
res = session.query(Artist).all()
for artist in res:
    print(artist.name)

# how to SELECT the first result
res = session.query(Artist).filter(Artist.name=="Newsboys").first()

# how to sort the results (ORDER_BY)
res = session.query(Album).order_by(Album.title).all()
for album in res:
    print(album.title)

# how to do a JOINed query
qry = session.query(Artist, Album)
qry = qry.filter(Artist.id==Album.artist_id)
artist, album = qry.filter(Album.title=="Step Up to the Microphone").first()

# how to use LIKE in a query
res = session.query(Album).filter(Album.publisher.like("S%a%")).all()
for item in res:
    print(item.publisher)