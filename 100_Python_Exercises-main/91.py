import pandas as pd
import sqlite3

df = pd.read_csv("ten_more_countries.txt")

conn = sqlite3.connect("database.db")
curr = conn.cursor()
value = 51
for index, row in df.iterrows():
    print(row["Country"], row["Area"])
    curr.execute(
        "INSERT INTO countries VALUES (?,?,?,NULL)",
        (value, row["Country"], row["Area"]),
    )
    value += 1
conn.commit()
conn.close()
