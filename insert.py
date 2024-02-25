import sqlite3

connection = sqlite3.connect('homescapes_database.db')

with open('reset.sql') as f:
    connection.executescript(f.read())