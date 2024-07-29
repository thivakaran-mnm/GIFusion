import sqlite3
import pandas as pd

# Create SQLite database
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# Creating table
cursor.execute('''
CREATE TABLE Logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    num TEXT NOT NULL
)
''')

# Inserting data into table
data = [
    ('1',),
    ('1',),
    ('1',),
    ('2',),
    ('1',),
    ('2',),
    ('2',)
]
cursor.executemany('INSERT INTO Logs (num) VALUES (?)', data)


# Query to find numbers that appear at least three times consecutively
query = '''
SELECT DISTINCT l1.num AS ConsecutiveNums
FROM Logs l1
JOIN Logs l2 ON l1.id = l2.id - 1 AND l1.num = l2.num
JOIN Logs l3 ON l2.id = l3.id - 1 AND l2.num = l3.num
'''


res = pd.read_sql_query(query, conn)


print(res)
