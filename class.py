class Student:
    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa

    def honorcheck(self):
        if self.gpa >= 5:
            return True
        else:
            return False

Student1 = Student("Nibba","CompSci",7.4)

print(Student1.honorcheck())

