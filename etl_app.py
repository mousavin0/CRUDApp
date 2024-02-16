from constants import schedule_seconds
from helper_functions import read_from_log_file_write_to_table, update_summary_file, get_login_summary
from sqlite_commands import create_users_logins_tables
import time
import os
from constants import login_log_file

def etl_loop():
    try:
        while True:
            create_users_logins_tables()
            read_from_log_file_write_to_table()
            os.remove(login_log_file)
            update_summary_file()
            time.sleep(schedule_seconds)
    except KeyboardInterrupt:
        print('Appen stängs!')

if __name__ == '__main__':
    etl_loop()
    # print(get_login_summary())
