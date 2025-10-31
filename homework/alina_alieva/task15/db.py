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
cursor.execute("SELECT * FROM students where id = %s", (student_id,))
new_student = cursor.fetchone()
print(new_student)

books = [("Book1", student_id), ("Book2", student_id), ("Book3", student_id)]
cursor.executemany(
    "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)", books
)
db.commit()
cursor.execute("SELECT * FROM books LIMIT 5")
all_books = cursor.fetchall()
for book in all_books:
    print("All books:", book)

cursor.execute(
    "INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)",
    ("NEW alina group test 2", "2025-10-25", "2025-12-25"),
)
db.commit()
group_id = cursor.lastrowid
cursor.execute("SELECT * FROM `groups` WHERE id = %s", (group_id,))
group = cursor.fetchone()
print(group)

cursor.execute("UPDATE students SET group_id = %s WHERE id = %s",
               (group_id, student_id,))
db.commit()
print(f"{student_id} {group_id}")

subject_to_add = [
    "Subject for my test user Alina 2",
    "Subject Two for my test user Alina 3"
]
subject_ids = []
for title in subject_to_add:
    cursor.execute("INSERT INTO subjects (title) VALUES (%s)", (title,))
    db.commit()
    subject_ids.append(cursor.lastrowid)
print("Subjects ------:")
for title, sid in zip(subject_to_add, subject_ids):
    print(sid)

lesson_to_add = [
    ("Lesson A", 0),
    ("Lesson B", 0),
    ("Lesson C", 1),
    ("Lesson D", 1),
]

lessons_ids = []
for lesson_title, subj_index in lesson_to_add:
    subject_id = subject_ids[subj_index]
    cursor.execute(
        "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)",
        (lesson_title, subject_id)
    )
    db.commit()
    lessons_ids.append(cursor.lastrowid)
print("Lessons ----")
for lid in lessons_ids:
    print(lid)

marks = []
for lesson_id in lessons_ids:
    value = 7
    cursor.execute(
        f"INSERT INTO marks (student_id, lesson_id, value) VALUES (%s, %s, %s)",
        (student_id, lesson_id, value)
        )
    db.commit()
    marks.append((lesson_id, value))

print("Marks ------")
for lesson_id, value in marks:
    print({lesson_id}, {value})


cursor.execute("SELECT * FROM marks WHERE student_id = %s", (student_id,))
student_marks = cursor.fetchall()
print("All student marks:")
for mark in student_marks:
    print(mark)

cursor.execute("SELECT * FROM books WHERE taken_by_student_id = %s", (student_id,))
student_books = cursor.fetchall()
for book in student_books:
    print(book)

query = """
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
WHERE s.id = %s
ORDER BY subj.id, l.id;
"""
cursor.execute(query, (student_id,))
student_full_info = cursor.fetchall()

print("\n--- FULL STUDENT INFO ---")
for row in student_full_info:
    print(row)
db.close()
