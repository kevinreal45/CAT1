class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.assignments = {}  # Dictionary: assignment names as keys, grades as values

    def add_assignment_and_grade(self, assignment, grade):
        self.assignments[assignment] = grade
        print(f"Grade '{grade}' added for assignment '{assignment}'.")

    def display_grades(self):
        if self.assignments:
            print(f"Grades for {self.name}:")
            for assignment, grade in self.assignments.items():
                print(f" - {assignment}: {grade}")
        else:
            print(f"{self.name} has no grades recorded.")


class Instructor:
    def __init__(self, name, course_name):
        self.name = name
        self.course_name = course_name
        self.students = []

    def add_student_to_course(self, student):
        self.students.append(student)
        print(f"Student {student.name} (ID: {student.student_id}) added to the course '{self.course_name}'.")

    def assign_grade_to_student(self, student_id, assignment, grade):
        for student in self.students:
            if student.student_id == student_id:
                student.add_assignment_and_grade(assignment, grade)
                print(f"Assigned grade '{grade}' to {student.name} for '{assignment}'.")
                return
        print(f"Student with ID {student_id} not found in the course.")

    def display_students_grades(self):
        if self.students:
            print(f"Grades for all students in '{self.course_name}':")
            for student in self.students:
                print(f"Student: {student.name}")
                student.display_grades()
        else:
            print(f"No students enrolled in '{self.course_name}'.")


# Interactive code
course_name = input("Enter the course name: ")
instructor_name = input("Enter the instructor's name: ")
instructor = Instructor(instructor_name, course_name)

while True:
    print("\nCourse Management Menu:")
    print("1. Add a student to the course")
    print("2. Assign a grade to a student")
    print("3. Display all students and their grades")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        student_name = input("Enter the student's name: ")
        student_id = input("Enter the student's ID: ")
        student = Student(student_name, student_id)
        instructor.add_student_to_course(student)

    elif choice == "2":
        student_id = input("Enter the student's ID: ")
        assignment_name = input("Enter the assignment name: ")
        grade = input("Enter the grade: ")
        instructor.assign_grade_to_student(student_id, assignment_name, grade)

    elif choice == "3":
        instructor.display_students_grades()

    elif choice == "4":
        print("Exiting the course management system.")
        break

    else:
        print("Invalid choice. Please select a valid option.")
