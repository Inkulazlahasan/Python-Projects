def save_student(student):
    with open("Students.txt","a") as file:
        course_names = ",".join([str(course) for course in student.courses])
        file.write(f"\nName: {student.name},\nRoll: {student.roll},\nCourses: {course_names}\n\n")

def show_all_students():
    try:
        with open("Students.txt","r") as file:
            print("\n--- All Enrolled Students ---")
            for line in file:
                print(line.strip())

    except FileNotFoundError:
        print("No student found!")