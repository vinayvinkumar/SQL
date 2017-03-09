## 3. Connect to the database ##

import sqlite3 as sq
conn = sq.connect("jobs.db")

## 6. Running a query ##

import sqlite3
conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

query = "select * from recent_grads;"
cursor.execute(query)
results = cursor.fetchall()
print(results[0:2])

cursor.execute("select Major from recent_grads;")
majors = cursor.fetchall()
print(majors[0:3])

## 8. Fetching a specific number of results ##

import sqlite3
conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()
five_results = cursor.execute("select Major,Major_category from recent_grads;").fetchmany(5)

## 9. Closing the connection ##

conn = sqlite3.connect("jobs.db")
conn.close()

## 10. Practice ##

import sqlite3 as sq
conn = sq.connect("jobs2.db")
cursor = conn.cursor()
reverse_alphabetical = cursor.execute("select Major from recent_grads order by Major desc;").fetchall()
conn.close()