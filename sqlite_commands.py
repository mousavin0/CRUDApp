import sqlite3

def prepare_relational_database():
    conn = sqlite3.connect("users_data.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
                   user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   firstname TEXT,
                   lastname TEXT,
                   username TEXT UNIQUE,
                   password_hash TEXT,
                   address TEXT,
                   telephone TEXT )""")
    conn.commit()
    cursor.close()
    conn.close()

