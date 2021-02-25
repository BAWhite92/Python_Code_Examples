#Using python to count email in a database
import sqlite3

#connect to database with name emaildb.sqlite, will create file when it runs if it doesn't exist
conn = sqlite3.connect('emaildb.sqlite')

#set the cursor (handle?) send sql commands through cursor
cur = conn.cursor()

#does nothing if the database does not exist, deletes the table 'Counts' from the database.
cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('CREATE TABLE Counts (email TEXT, count INTEGER)')

fname = input("Enter file name: ")
if (len(fname) < 1): 
    #need a file with a series of emails, in this case searching for lines with From: to identify the emails within the file
    fname = 'mbox-short.txt'
fh = open(fhand)
for line in fh:
    if not line.startswith('From: '): 
        continue
    pieces = line.split()
    email = pieces[1]
    #like a dictionary in a way. Use ? for sql injection attacks.
    cur.execute('SELECT count FROM Counts WHERE email = ?', (email,)) #? is placeholder to be replaces by email, you need to send a tuple to the ? hence the comma...
    #row will be info we get back from the database
    row = cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO Counts (email, count) VALUES (?, 1)', 
                    (email,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',
                    (email,))
    conn.commit()

#DONT FORGET ''' IS FOR MULTILINE STRINGS
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])



#
