import sqlite3
conn=sqlite3.connect('data.db')
cur=conn.cursor()
cur.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER
)
''')
cur.execute('INSERT INTO Users (id, username, email, age) VALUES (?, ?, ?, ?)', (1, 'Vasya', 'vasya@example.com', 128))
conn.commit()
conn.close()
