import sqlite3
#how to get data from your database to link with JSON following relations!


#if you wanted artist title and album name from databases, (2 database tables 1 called artist, 1 called album)
'SELECT Album.title, Artist.name FROM Album JOIN Artist ON Album.artist_id = Artist.id'

#would use normal connect etc and exeute etc (on clause decides where to connect tables) 

#so select the title of album and name of artist from the two stated tables.
#use join to show foreign key usage, and then state which row in first table leads to the corresponding table for the required second output.

#SO 1ST TABLE MENTIONED IS FIRST REQUIRED OUTPUT AND 2ND TABLE MENTIOONED IS THE ONE THAT FK LEADS TO AND IS SECOND REQUIRED OUTPUT

#can go deeper to 3 or 4 deep if needed for example.

#remove on clause and all possible combos are returned, can lead to a long wait and a mess if large tables!



