import string
from datetime import datetime, timedelta
from .print_sagou import print_error
import os

def get_columns_for_two(start_column = "", end_column = "", column_to_remove = ""):
    column_names = []
    for letter1 in string.ascii_uppercase:
        if letter1 >= start_column:
            column_names.append(letter1)
    for letter1 in string.ascii_uppercase:
        for letter2 in string.ascii_uppercase:
            ch = letter1 + letter2
            if ch == end_column:
                column_names.append(ch)
                if column_to_remove != "":
                    column_names.remove(column_to_remove)
                return column_names
            else:
                column_names.append(ch)



def get_date_list(start_date_str, end_date_str):
    start_date = datetime.strptime(start_date_str, '%d-%m-%Y')
    end_date = datetime.strptime(end_date_str, '%d-%m-%Y')
    date_list = []
    current_date = start_date
    if start_date_str == end_date_str:
        date_str = start_date.strftime('%d-%m-%Y')
        date_list.append(date_str)
        return date_list
    while current_date <= end_date:
        date_str = current_date.strftime('%d-%m-%Y')
        date_list.append(date_str)
        current_date += timedelta(days=1)
    if len(date_list) != 6: # to modify
        print_error("LES DATE QUI VOUS AVEZ INSERER N'EST PAS VALIDE")
    else:
        return date_list

def check_exist_file(file_path):
    if os.path.exists(file_path):
        return True
    else:
        return False


