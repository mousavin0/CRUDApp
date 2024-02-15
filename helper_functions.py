

# to avoid revealing password in terminal
import getpass

#to check if files exist
import os
#to writerow in csv
import csv

from openpyxl import Workbook
from constants import login_log_file, login_history_file

from datetime import datetime


from sqlite_commands import get_user_id

def get_nonempty_input(fieldname, is_password=False):
    prompt = f'Ange ditt {fieldname}: '
    while True:
        if is_password:
            user_input = getpass.getpass(prompt)
        else:
            user_input = input(prompt)
        if user_input.strip():  # Check if the input is not empty after stripping whitespace
            return user_input.strip()
        else:
            print(f'{fieldname} får inte vara tom.')





def append_to_log(username):
    prepare_log_file()
    with open(login_log_file,'a') as f:    
        writer = csv.writer(f)
        dt=datetime.now()
        user_id = get_user_id(username)
        writer.writerow([user_id,dt.year,dt.month,dt.day,dt.hour,dt.minute,dt.second])


def prepare_log_file():
    if not os.path.exists(login_log_file):
        header = ['user_id', 'year', 'month', 'day','hour','minute','second']
        with open(login_log_file, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(header)


# def prepare_history_file():
#         if not os.path.exists(login_history_file):
#             wb = Workbook()
#             ws = wb.active
#             ws['A1'] = 'number_of_logins'
#             ws['B1'] = 'year'
#             ws['C1'] = 'month'
#             ws['D1'] = 'day'
#             ws['E1'] = 'hour'
#             wb.save(login_history_file)

