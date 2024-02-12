import sqlite3

def prepare_relational_database():
    conn = sqlite3.connect("users_data.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
                   user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   firstname TEXT NOT NULL,
                   lastname TEXT NOT NULL,
                   username TEXT UNIQUE NOT NULL,
                   password_hash TEXT NOT NULL,
                   address TEXT,
                   telephone TEXT )""")
    conn.commit()
    cursor.close()
    conn.close()

def add_user():
    pass

def is_username_unique(username):
    return True

