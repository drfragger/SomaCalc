import sqlite3


conn = sqlite3.connect('items.db')

c = conn.cursor()

conn.close()