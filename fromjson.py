import sqlite3
import json

conn = sqlite3.connect('mech2.db')
conn.execute("CREATE TABLE mech_table (field1 text, field2 text, field3 text);")
with open('units.json', 'r') as json_file:
    data = json.load(json_file)
    for item in data:
        conn.execute("INSERT INTO mech_table (field1, field2, field3) VALUES (?, ?, ?)", (item["field1"], item["field2"], item["field3"]))
conn.commit()
conn.close()