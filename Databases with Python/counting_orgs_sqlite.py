#counts organisations who sent emails (finds the domain name of the email addresses through slicing) and creates + saves the number of occurances of these domain names to a database 'Counts'
import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

#fname = input("Enter file name: ")
#if (len(fname) < 1): 
fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): 
        continue
    pieces = line.split()
    org = pieces[1]
    atpos = org.find("@")
    domain = org[atpos+1 :]
    print(org)
    print(domain)
    cur.execute('SELECT count FROM Counts WHERE org = ?', (domain,)) 
    row = cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', 
                    (domain,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (domain,))
    conn.commit()

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])
