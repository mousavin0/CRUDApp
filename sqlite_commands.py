import sqlite3
import bcrypt
from constants import database_name
def create_users_logins_tables():
    conn = sqlite3.connect(database_name)
    conn.execute("PRAGMA foreign_keys = 1")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
                   user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   firstname TEXT NOT NULL,
                   lastname TEXT NOT NULL,
                   username TEXT UNIQUE NOT NULL,
                   password_hash TEXT NOT NULL,
                   address TEXT,
                   telephone TEXT )""")
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS logins (
                   login_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   user_id INTEGER NOT NULL,
                   year INTEGER NOT NULL,
                   month INTEGER NOT NULL,
                   day INTEGER NOT NULL,
                   hour INTEGER NOT NULL,
                   minute INTEGER NOT NULL,
                   second INTEGER NOT NULL,
                   FOREIGN KEY (user_id) REFERENCES users(user_id)
                   )""")
    conn.commit()
    cursor.close()
    conn.close()



def get_login_summary():
    sql_query = """SELECT count(login_id) as number_of_logins, year, month, day, hour FROM logins GROUP BY hour"""
    result = run_READ_statements_fetch_all(sql_query)
    return result



def add_login(user_id,year, month,day,hour,minute,second):
    sql_query = """INSERT INTO logins (user_id, year, month,day,hour,minute,second) VALUES(?,?,?,?,?,?,?)"""
    values = (user_id,year, month,day,hour,minute,second)
    run_CUD_statements(sql_query,values)






def run_CUD_statements(query,values,print_statement=''):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    cursor.execute(query,values)
    conn.commit()
    cursor.close()
    conn.close()

def run_READ_statements_fetch_one(query,values,print_statement=''):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    cursor.execute(query,values)
    conn.commit()

    print(print_statement)
    # results = cursor.fetchall()
    # row_count = len(results)
    result = cursor.fetchone()

    cursor.close()
    conn.close()
    return result


def run_READ_statements_fetch_all(query):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    result = cursor.fetchall()

    cursor.close()
    conn.close()
    return result

def add_user(firstname,lastname,username,password_hash,address,telephone):
    sql_query = """ INSERT INTO users (firstname,lastname,username,password_hash,address,telephone) VALUES (?,?,?,?,?,?)"""
    values = (firstname,lastname,username,password_hash,address,telephone)
    run_CUD_statements(sql_query,values,'Du har skapat ett konto!')

def user_exists(username,password):
    sql_query = """ SELECT password_hash FROM users WHERE username = ?"""
    values = (username,)
    true_passowrd_hashed_query_results = run_READ_statements_fetch_one(sql_query,values)
    if true_passowrd_hashed_query_results:
        true_passowrd_hashed = true_passowrd_hashed_query_results[0]
        if bcrypt.checkpw(password.encode('utf-8'),true_passowrd_hashed):
            return True
    return False




def is_username_unique(username):
    sql_query = """ SELECT user_id FROM users WHERE username = ?"""
    values = (username,)
    user_id = run_READ_statements_fetch_one(sql_query,values)
    if user_id:
        return False
    return True

def update_user(username,field,new_value):
    userid = get_user_id(username)
    sql_query = f'UPDATE users SET {field} = ? WHERE user_id = ?'
    values = (new_value,userid)
    run_CUD_statements(sql_query,values)


def get_user_id(username):
    sql_query = """ SELECT user_id FROM users WHERE username = ?"""
    values = (username,)
    user_id_query_results = run_READ_statements_fetch_one(sql_query,values)
    user_id = user_id_query_results[0]
    return user_id



if __name__=="__main__":
    print(update_user('c','firstname','aa'))
    #print(get_user_id('c'))