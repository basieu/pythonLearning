class Person:
    def __init__(self, name, surname, city):
        self.name = name
        self.surname = surname
        self.city = city
        print("Person constructor")

    def printPersonInfo(self):
        print("Person info:", self.name, self.surname, self.city)


person1 = Person("Jan", "Kowalski", "Kraków")
person1.printPersonInfo()
print("--------")


class Employee(Person):
    def __init__(self, name, surname, city, company, salary):
        Person.__init__(self, name, surname, city)
        self.company = company
        self.salary = salary
        print("Employee constructor")

    def printEmployeeInfo(self):
        print("Employee info:", self.name, self.surname, self.city, self.company, self.salary)

employee1 = Employee("Kasia", "Nowak", "Lublin", "Company Ltd", 5000)
employee1.printPersonInfo()
employee1.printEmployeeInfo()
print("--------")


class Manager(Employee):
    def __init__(self, name, surname, city, company, salary, department):
        # super().__init__(name, surname, city, company, salary)    -    pobiera konstruktor z dziedziczonej klasy, nie trzeba "self"
        Employee.__init__(self, name, surname, city, company, salary)
        self.department = department
        print("Manager constructor")

    def printManagerInfo(self):
        print("Manager info:", self.name, self.surname, self.city, self.company, self.salary, self.department)


manager1 = Manager("Adam", "Lewandowski", "Warszawa", "WWA Tech", 10000, "IT")
manager1.printPersonInfo()
manager1.printEmployeeInfo()
manager1.printManagerInfo()