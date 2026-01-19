from student import Student
from course import Course
from file_handler import save_student, show_all_students


def menu():
    print("\n--- School Management System ---")
    print("1. Add New Student")
    print("2. Show All Students")
    print("3. Exit")


while True:
    menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        roll = input("Enter roll number: ")
        password = input("Set password: ")

        student = Student(name, roll, password)

        course_count = int(input("How many courses to enroll? "))

        for i in range(course_count):
            course_name = input(f"Enter course {i+1} name: ")
            course = Course(course_name)
            student.enroll_course(course)

        save_student(student)
        print("Student enrolled successfully!")

    elif choice == "2":
        show_all_students()

    elif choice == "3":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")
