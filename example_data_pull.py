import sqlite3
import pandas as pd

df = pd.read_csv("lyrics.csv")

df_queen = df[df['Band']=='Queen']

print(df_queen['Song'].values)
#############--------------SAMPLE_RESULTS--------------#############
# ['Jailhouse Rock' 'Introduction' 'Love Kills: The Ballad'
#  "Modern Times Rock'n'roll" 'Jesus' 'Keep Yourself Alive [#]'
# ...
#  'There Must Be More to Life Than This' 'Bohemian Rhapsody (Reprise)'
#  'Stone Cold' 'White Queen (As It Began) [Session 4]'
#  'Under Pressure [Maimmarktgelände, Mannheim, Germany, 21st June 1986]']


def query_metadata(qs):
    conn_metadata = sqlite3.connect("./db/track_metadata.db")
    result = conn_metadata.execute(qs).fetchall()
    conn_metadata.close()

    return result

## mxm_dataset.db: The database below contains 270K+ songs with lyrics but they are
##                 prestemmed and are almost unrecognizable "pretty" -> "pretti"
conn = sqlite3.connect("./db/mxm_dataset.db")

## track_metadata.db: contains meatadata for 1 million songs. Some not well titled
##                 http://millionsongdataset.com/pages/example-track-description/
conn_metadata = sqlite3.connect("./db/track_metadata.db")


query_metadata("SELECT artist_name, title, year FROM songs WHERE artist_name = 'Queen'")
#############--------------SAMPLE_RESULTS--------------#############
# 1. ('Queen', 'Body Language (1994 Digital Remaster)', 1982)
# 2. ('Queen', "'39 (Live) (1994 Digital Remaster)", 0)
# 3. ('Queen', "You're My Best Friend", 1975)