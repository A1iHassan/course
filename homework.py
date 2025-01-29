class student:
    school = {"not a class": 0}
    helper = 0

    def __init__(self, name, classes, grades):
        self.name = name
        self.classes = classes
        if not isinstance(grades, list):
            print("grades must be a list")
        else:
            self.grades = grades
        for i in student.school:
            if i == classes:
                student.school[i] += 1
            else:
                student.helper = 1
        if student.helper:
            student.school[classes] = 1
            student.helper = 0
    
    def __str__(self):
        return f"{self.name}, {self.classes}"
    
    def gpa(self, full):
        x = 0
        y = len(self.grades)

        for i in self.grades:
            x += i

        print(f"{self.name}: {(x / y)}/{full}")
    
    @classmethod
    def num_of_students(cls, sp_class):
        return cls.school[sp_class]
    
    def intro(self):
        print(f"this is {self.name} from class {self.classes}")


ali = student("ali hassan", "first", [22, 30, 44])
ali.intro()
ali.gpa(50)
print(student.num_of_students("first"))