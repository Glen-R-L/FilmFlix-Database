from connect import *

# Create tblFilms table

cursor.execute(
"""
Create Table tblFilms(
"filmID" Integer Not Null Unique,
"title" Text,
"yearReleased" Integer,
"rating" Text,
"duration" Integer,
"genre" Text,
Primary Key("filmID" AutoIncrement)
) 
"""
)

