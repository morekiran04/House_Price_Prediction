import sqlite3

conn = sqlite3.connect("house_data.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS predictions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    area INTEGER,
    rooms INTEGER,
    location TEXT,
    predicted_price REAL
)
""")

conn.commit()
conn.close()

print("Database created successfully!")