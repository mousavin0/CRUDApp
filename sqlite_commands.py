import sqlite3
database_name = "users_data.db"
def prepare_relational_database():
    conn = sqlite3.connect(database_name)
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

def run_prepared_statements(query,values,print_statement=''):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    cursor.execute(query,values)
    conn.commit()
    print(print_statement)
    cursor.close()
    conn.close()

def add_user(firstname,lastname,username,password_hash,address,telephone):
    sql_query = """ INSERT INTO users (firstname,lastname,username,password_hash,address,telephone) VALUES (?,?,?,?,?,?)"""
    values = (firstname,lastname,username,password_hash,address,telephone)
    run_prepared_statements(sql_query,values,'Du har skapat ett konto!')



def is_username_unique(username):
    return True

