import random

class Student:
    def __init__(self, name, surname, age, city):
        self.name = name
        self.surname = surname
        self.age = age
        self.city = city
        self.schoolName = None
        self.fieldOfStudy = None

    def printInfo(self):
        print(self.name, self.surname, self.age, self.city, self.schoolName, self.fieldOfStudy)


class School:
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.studentsList = []
        self.fieldsOfStudy = ["IT", "Medicine", "Law"]

    def addStudent(self, student):
        if isinstance(student, Student):
            self.studentsList.append(student)
            student.schoolName = self.name
            student.fieldOfStudy = random.choice(self.fieldsOfStudy)

    def printShoolInfo(self):
        print("School Name:", self.name)
        for el in self.studentsList:
            el.printInfo()

student1 = Student("Jan", "Kowalski", 23, "Warszawa")
student2 = Student("Kasia", "Nowak", 21, "Lublin")

school = School("University of General Sciences", "Kraków")
school.addStudent(student1)
school.addStudent(student2)
school.printShoolInfo()
