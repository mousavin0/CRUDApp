

# to avoid revealing password in terminal
import getpass

#to check if files exist
import os
#to writerow in csv
import csv

from openpyxl import Workbook
from constants import login_log_file, login_history_file



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


def prepare_log_files():
    if not os.path.exists(login_log_file):
        header = ['username', 'year', 'month', 'day','hour','minute','second']
        with open(login_log_file, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(header)
    if not os.path.exists(login_history_file):
        wb = Workbook()
        ws = wb.active
        ws['A1'] = 'number_of_logins'
        ws['B1'] = 'year'
        ws['C1'] = 'month'
        ws['D1'] = 'day'
        ws['E1'] = 'hour'
        wb.save(login_history_file)

