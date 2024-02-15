from constants import schedule_seconds, login_log_file
import csv 
from sqlite_commands import add_login
from datetime import datetime
from helper_functions import prepare_log_file

import os
if __name__ == '__main__':
    prepare_log_file()
    # while True:
    

    with open(login_log_file,'r') as f:
        reader_obj = csv.DictReader(f) 
        for row in reader_obj: 
            login_datetime = datetime(int(row['year']),int(row['month']),int(row['day']),
                            int(row['hour']),int(row['minute']),int(row['second']))
            user_id = int(row['user_id'])
            add_login(user_id,login_datetime)

        os.remove(login_log_file)
            # print(row['user_id'])


        # time.sleep(schedule_seconds)
