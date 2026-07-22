import sqlite3

# Connect to database
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE,
    age INTEGER,
    course TEXT,
    marks REAL
)
""")
conn.commit()


def add_student(name, age, course, marks):
    try:
        cursor.execute(
            "INSERT INTO students(name, age, course, marks) VALUES(?,?,?,?)",
            (name, age, course, marks)
        )
        conn.commit()
        print("Student added successfully.")
    except sqlite3.IntegrityError:
        print("Student name already exists.")


def view_students():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    if not students:
        print("No students found.")
    else:
        print("\nID | Name | Age | Course | Marks")
        print("-" * 45)
        for student in students:
            print(student)


def search_student(name):
    cursor.execute("SELECT * FROM students WHERE name LIKE ?", ('%' + name + '%',))
    student = cursor.fetchall()

    if student:
        for s in student:
            print(s)
    else:
        print("Student not found.")


def delete_student(student_id):
    cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
    conn.commit()

    if cursor.rowcount:
        print("Student deleted.")
    else:
        print("Student not found.")


def update_marks(student_id, marks):
    cursor.execute(
        "UPDATE students SET marks=? WHERE id=?",
        (marks, student_id)
    )
    conn.commit()

    if cursor.rowcount:
        print("Marks updated successfully.")
    else:
        print("Student not found.")