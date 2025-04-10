import os
import re
from datetime import datetime, timedelta


def line_action(line):
    data = re.search(r"(\d+).\s+(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+)\s+-\s+(.*)", line)

    if data:
        number = data.group(1)
        day = data.group(2)

        date_two_obj = datetime.strptime(day, "%Y-%m-%d %H:%M:%S.%f")
        if number == "1":
            new_date = date_two_obj + timedelta(days=7)
            print(f"1.{new_date}")
        elif number == "2":
            day_of_week = datetime.strftime(date_two_obj, "%A")
            print(f"2.{day_of_week}")
        elif number == "3":
            current_date = datetime.now()
            difference = current_date - date_two_obj
            print(f"3.{difference.days}")


current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, '..', '..', 'eugene_okulik', 'hw_13', 'data.txt')
file_path = os.path.normpath(file_path)
with open(file_path, 'r', encoding='utf-8') as file:
    file = file.readlines()
    for line in file:
        line_action(line)
