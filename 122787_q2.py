#Online course management

class Student:
    def __init__(self, student_id):
        self.student_id = student_id
        self.assignments = {}#dictionary, assignment names as keys and grades as values

    def add_assignment_and_grade(self):
        pass
    
    def display_grades(self):
        pass
class Instructor:
    def __init__(self, name, course_name):
        self.name =name
        self.course_name = course_name
        self.students = []
    
    def add_student_to_course(self):
        pass
    
    def assign_grade_to_student(self):
        pass
    
    def display_students_grades(self):
        pass
    
#interactive code to allow an instructor to add students and assign grades interactively 