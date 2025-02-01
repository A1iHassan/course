class Student:
    # Class property
    total_students = 0
    all_students = {}

    # Constructor
    def __init__(self, name):
        self.name = name
        self.grades = {}
        Student.total_students += 1
        self.student_id = Student.total_students
        Student.all_students[self.student_id] = self

    # Instance Methods
    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def get_average(self):
        return sum(self.grades.values()) / len(self.grades)

    @classmethod
    def get_top_student(cls):
        if not cls.all_students:
            return None
        top = ""
        top_avg = 0
        for i in cls.all_students.values():
            x = i.get_average()
            if top_avg < x:
                top = i.name
                top_avg = x
        return {"name": top, "avg": top_avg}

    @staticmethod
    def is_valid_grade(grade):
        return isinstance(grade, (int, float)) and 0 <= grade <= 100

# Example Usage:
student1 = Student("Alice")
student1.add_grade("Math", 90)
student2 = Student("Bob")
student2.add_grade("Math", 95)
top_student = Student.get_top_student()
print(top_student)  # Output: Bob