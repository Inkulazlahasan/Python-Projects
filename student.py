from course import Course

class Student:
    def __init__(self,name, roll,password):
        self.name = name
        self.roll = roll
        self.courses = []
        self.__password = password

    def enroll_course(self,course):
        self.courses.append(course)

    def get_password(self):
        return self.__password