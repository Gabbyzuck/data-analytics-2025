

### download and extract chinook sample DB
from urllib.request import Request, urlopen #downloads files from web
import zipfile #allows working with zip files
from functools import partial #defines how much data to read at a time
import os #interacts with operating system to check for files

chinook_url = 'http://www.sqlitetutorial.net/wp-content/uploads/2018/03/chinook.zip'
req = Request(chinook_url, headers={'User-Agent': 'Mozilla/5.0'})

if not os.path.exists('chinook.zip'): #checks if file is already downloaded
    print('downloading chinook.zip ', end='') #end='' prevents newline after print
    with urlopen(req) as response: #opens connection to URL
        with open('chinook.zip', 'wb') as f: #opens file to write binary data 'wb'
            for data in iter(partial(response.read, 4*1024), b''): #loop to read data in 4KB chunks and writes it to file and prints '.' each time it write a chunk for progress
                print('.', end='', flush=True)
                f.write(data)

zipfile.ZipFile('chinook.zip').extractall() #unzips and extracts everything
assert os.path.exists('chinook.db') #checks database file was successfully extracted

### useful: functions for displaying results from sql queries using pandas
from IPython.display import display
import pandas as pd

def sql(query):
    print()
    print(query)
    print()

def get_results(query):
    global engine
    q = query.statement if isinstance(query, sqlalchemy.orm.query.Query) else query
    return pd.read_sql(q, engine)

def display_results(query):
    df = get_results(query)
    display(df)
    sql(query)

import sqlalchemy
from sqlalchemy import func

from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///chinook.db")

connection = engine.connect()
#print("Connected!")
connection.close()

### useful: extract classes from the chinook database
metadata = MetaData()
metadata.reflect(engine)

print(metadata.tables.keys())

## we need to do this once
from sqlalchemy.ext.automap import automap_base

# produce a set of mappings from this MetaData.
Base = automap_base(metadata=metadata)

# calling prepare() just sets up mapped classes and relationships.
Base.prepare()

tracks = Base.classes.tracks
albums = Base.classes.albums
invoice_items = Base.classes.invoice_items
artists = Base.classes.artists


# also prepare an orm session

Session = sessionmaker(bind=engine)
session = Session()
top_3_tracks = session.query(tracks).limit(3).all()

#for t in top_3_tracks:
    #print(f"Track ID: {t.TrackId}, Name: {t.Name}, Album ID: {t.AlbumId}, Genre ID: {t.GenreId}")

top_20 = session.query(tracks, albums).join(albums, tracks.AlbumId == albums.AlbumId).limit(20).all()

#for t, a in top_20:
    #print(f"Track Name: {t.Name}, Album Titles: {a.Title}")

sales = session.query(invoice_items, tracks)\
    .join(tracks, invoice_items.TrackId == tracks.TrackId)\
    .limit(10)\
    .all()

#for item, track in sales:
    #print(f"Track Name: {track.Name}, Quantity Sold: {item.Quantity}")

top_tracks = (
    session.query(tracks.Name, func.sum(invoice_items.Quantity).label("total_sold"))
    .join(invoice_items, tracks.TrackId == invoice_items.TrackId)
    .group_by(tracks.TrackId)
    .order_by(func.sum(invoice_items.Quantity).desc())
    .limit(10)
    .all()
)

#for name, total in top_tracks:
    #print(f"Track: {name}, Times Sold: {total}")

top_artists = (
    session.query(artists.Name, func.sum(invoice_items.Quantity).label("total_sold"))
    .join(albums, artists.ArtistId == albums.ArtistId)
    .join(tracks, albums.AlbumId == tracks.AlbumId)
    .join(invoice_items, tracks.TrackId == invoice_items.TrackId)
    .group_by(artists.ArtistId)
    .order_by(func.sum(invoice_items.Quantity).desc())
    .limit(10)
    .all()
)

# Print results
for name, total in top_artists:
    print(f"Artist: {name}, Total Tracks Sold: {total}")