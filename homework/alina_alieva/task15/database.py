import mysql.connector as mysql

db = mysql.connect(
    user="st-onl",
    passwd="AVNS_tegPDkI5BlB2lW5eASC",
    host="db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com",
    port=25060,
    database="st-onl",
)
cursor = db.cursor(dictionary=True)
cursor.execute("INSERT INTO students (name, second_name) VALUES ('New', 'Student')")
student_id = cursor.lastrowid
cursor.execute(f"SELECT * FROM students where id = {student_id}")
new_student = cursor.fetchone()
print(new_student)

books = [("Book1", student_id), ("Book2", student_id), ("Book3", student_id)]
cursor.executemany(
    "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)", books
)
db.commit()
cursor.execute(f"SELECT * FROM books LIMIT 5")
all_books = cursor.fetchall()
for book in all_books:
    print("All books:", book)

cursor.execute(
    "INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)",
    ("NEW alina group test 2", "2025-10-25", "2025-12-25"),
)
db.commit()
group_id = cursor.lastrowid
cursor.execute(f"SELECT * FROM `groups` WHERE id = {group_id}")
group = cursor.fetchone()
print(group)
cursor.execute(f"UPDATE students SET group_id = {group_id} WHERE id = {student_id}")
db.commit()
print(f"{student_id} {group_id}")

cursor.executemany(
    "INSERT INTO subjects (title) VALUES (%s)",
    [("Subject for my test user Alina 2",), ("Subject Two for my test user Alina 3",)],
)
db.commit()
cursor.execute(f"SELECT * FROM subjects")
subject = cursor.fetchall()
for sub in subject:
    print(sub)

lessons = []
for subject_item in subject:
    subject_id = subject_item["id"]
    subject_title = subject_item["title"]
    lessons.append((f"{subject_title} Lesson 1", subject_id))
    lessons.append((f"{subject_title} Lesson 2", subject_id))
cursor.executemany("INSERT INTO lessons (title, subject_id) VALUES (%s, %s)", lessons)
db.commit()

cursor.execute(f"SELECT * FROM lessons ORDER BY id DESC LIMIT 20")
created_lessons = cursor.fetchall()

print("Lessons:")

marks = []
for lesson in created_lessons:
    lesson_id = lesson["id"]
    value = 7
    marks.append((student_id, lesson_id, value))
    print(lesson)
cursor.executemany(
    "INSERT INTO marks (student_id, lesson_id, value) VALUES (%s, %s, %s)", marks
)
db.commit()

cursor.execute(
    "SELECT * FROM marks WHERE student_id = %s ORDER BY id DESC LIMIT 5", (student_id,)
)
print(cursor.fetchall())

cursor.execute(f"SELECT * FROM marks WHERE student_id = {student_id}")
student_marks = cursor.fetchall()
print("All student marks:")
for mark in student_marks:
    print(mark)

cursor.execute(f"SELECT * FROM books WHERE taken_by_student_id = %s", (student_id,))
student_books = cursor.fetchall()
for book in student_books:
    print(book)

query = f"""
SELECT 
    s.id AS student_id,
    s.name,
    s.second_name,
    g.title AS group_title,
    b.title AS book_title,
    subj.title AS subject_title,
    l.title AS lesson_title,
    m.value
FROM students s
LEFT JOIN `groups` g ON s.group_id = g.id
LEFT JOIN books b ON b.taken_by_student_id = s.id
LEFT JOIN marks m ON m.student_id = s.id
LEFT JOIN lessons l ON m.lesson_id = l.id
LEFT JOIN subjects subj ON l.subject_id = subj.id
WHERE s.id = {student_id}
ORDER BY subj.id, l.id;
"""
cursor.execute(query)
student_full_info = cursor.fetchall()

print("\n--- FULL STUDENT INFO ---")
for row in student_full_info:
    print(row)
db.close()
