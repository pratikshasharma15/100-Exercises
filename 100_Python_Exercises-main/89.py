import sqlite3

conn = sqlite3.connect("database.db")

cursor = conn.cursor()

cursor.execute("SELECT country FROM countries WHERE area > 2000000")

country_name = cursor.fetchall()
conn.close()

for country in country_name:
    print(country[0])
