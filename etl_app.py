from constants import schedule_seconds
from helper_functions import read_from_log_file_write_to_table, update_summary_file

import time
import sys

def etl_loop():
    try:
        while True:
            read_from_log_file_write_to_table()
            update_summary_file()
            time.sleep(schedule_seconds)
    except KeyboardInterrupt:
        print('Appen stängs!')

if __name__ == '__main__':
    etl_loop()
