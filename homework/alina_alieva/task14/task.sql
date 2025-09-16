INSERT INTO `groups` (title, start_date, end_date) VALUES ('alina group test', '01.25', '02.25')
INSERT INTO students (name, second_name, group_id) VALUES ('QA Test', 'Alina', 21282)
INSERT INTO books (title, taken_by_student_id) VALUES ('Best book forever', 21307)
INSERT INTO books (title, taken_by_student_id) VALUES ('I do not know how they know it', 21307)
INSERT INTO books (title, taken_by_student_id) VALUES ('Are you seriously?', 21307)
INSERT INTO subjects (title) VALUES ('Subject for my test user Alina')
INSERT INTO subjects (title) VALUES ('Subject Two for my test user Alina')
INSERT INTO lessons (title, subject_id) VALUES ('Lesson 2', 12272)
INSERT INTO lessons (title, subject_id) VALUES ('Lesson 1', 12272)
INSERT INTO marks (value, lesson_id, student_id) VALUES ('10', 12744, 21307)
INSERT INTO marks (value, lesson_id, student_id) VALUES ('12', 12743, 21307)
INSERT INTO marks (value, lesson_id, student_id) VALUES ('15', 12742, 21307)
INSERT INTO marks (value, lesson_id, student_id) VALUES ('18', 12741, 21307)

select value from marks
where student_id = 21307

select title from books b
where taken_by_student_id = 21307

select students.name , students.second_name, books.title as books, g.title as team, m.value, l.title as lesson, s.title as subject from students
JOIN books on books.taken_by_student_id = students.id
JOIN `groups` g on g.id = students.group_id
JOIN marks m on m.student_id = students.id
JOIN lessons l on l.id = m.lesson_id
JOIN subjects s on s.id = l.subject_id
where students.id = 21307