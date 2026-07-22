from database import *

while True:
    print("\n===== Student Database =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Update Marks")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Name: ")
        age = int(input("Age: "))
        course = input("Course: ")
        marks = float(input("Marks: "))

        add_student(name, age, course, marks)

    elif choice == "2":
        view_students()

    elif choice == "3":
        name = input("Enter name to search: ")
        search_student(name)

    elif choice == "4":
        student_id = int(input("Enter student ID: "))
        delete_student(student_id)

    elif choice == "5":
        student_id = int(input("Student ID: "))
        marks = float(input("New Marks: "))
        update_marks(student_id, marks)

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")