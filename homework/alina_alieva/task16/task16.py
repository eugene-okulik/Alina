import csv
import os
import mysql.connector as mysql
from dotenv import load_dotenv
from pathlib import Path


load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSW = os.getenv("DB_PASSW")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

connection = mysql.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSW,
    port=DB_PORT,
    database=DB_NAME
)
cursor = connection.cursor()

csv_path = os.path.dirname(__file__)
file_path = os.path.join(csv_path, '..', '..', 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')
file_path = os.path.normpath(file_path)

missing_rows = []

with open(file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        name = row["name"].strip()
        second_name = row["second_name"].strip()
        group_title = row["group_title"].strip()
        book_title = row["book_title"].strip()
        subject_title = row["subject_title"].strip()
        lesson_title = row["lesson_title"].strip()
        mark_value = row["mark_value"].strip()
        query = """
                    SELECT * FROM marks m
                    JOIN students s ON m.student_id = s.id
                    JOIN `groups` g ON s.group_id = g.id
                    JOIN lessons l ON m.lesson_id = l.id
                    JOIN subjects subj ON l.subject_id = subj.id
                    WHERE s.name = %s
                      AND s.second_name = %s
                      AND g.title = %s
                      AND subj.title = %s
                      AND l.title = %s
                      AND m.value = %s
        """
        cursor.execute(query, (name, second_name, group_title,
                               subject_title, lesson_title, mark_value))
        result = cursor.fetchone()

        query_book = """
                SELECT b.id FROM books b
                JOIN students s ON b.taken_by_student_id = s.id
                WHERE s.name = %s
                  AND s.second_name = %s
                  AND b.title = %s
        """
        cursor.execute(query_book, (name, second_name, book_title))
        book_result = cursor.fetchone()

        if not result or not book_result:
            missing_rows.append(row)

if missing_rows:
    for r in missing_rows:
        print("нет в базе", r)
else:
    print("Все данные есть в базе.")

cursor.close()
connection.close()
