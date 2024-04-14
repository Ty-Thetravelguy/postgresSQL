import psycopg2


# connect to "chinook" database
connection = psycopg2.connect(database="chinook")

# build a cursor object of the database
cursor = connection.cursor()

# Query 1 - Select all records form the "artist" table
#cursor.execute('SELECT * FROM "artist"')

# Query 2 - Select only the "name" column from the "artist" table
#cursor.execute('SELECT "name" FROM "artist"')

# Query 3 - Select only "Queen" form the "artist" table
#cursor.execute('SELECT * FROM "artist" WHERE "name" = %s', ["Queen"])

# Query 4 - Select only by "artist_id" #51 from the "artist" table
#cursor.execute('SELECT * FROM "artist" WHERE "artist_id" = %s', [51])

# Query 5 - Select only the albums with "artist_id" #51 on the "album" table
#cursor.execute('SELECT * FROM "album" WHERE "artist_id" = %s', [51])

# Query 6 - select all tracks where the composer is "Queen" form the "track" table
cursor.execute('SELECT * FROM "track" WHERE "composer" = %s', ["Queen"])

# fetch the results (multiple)
results = cursor.fetchall()

# fetch the result (single)
#results = cursor.fetchone()

#close the connection
connection.close()

#print result
for result in results:
    print(result)
