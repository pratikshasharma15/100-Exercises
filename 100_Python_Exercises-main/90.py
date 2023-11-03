import sqlite3
import pandas as pd

conn = sqlite3.connect("database.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM countries WHERE area > 2000000")
country_name = cursor.fetchall()
conn.close()

df = pd.DataFrame(country_name)
df.to_csv("file2.csv", index=False)
