class Employee:
    numOfEmployees = 0
    employeesList = []

    def __init__(self, name):
        self.name = name

        Employee.numOfEmployees += 1
        print(self.name, "numOfEmployees:", Employee.numOfEmployees)

        Employee.employeesList.append(self)

    def printEmployeesList(self):
        for el in Employee.employeesList:
            print(el.name)


employee1 = Employee("Ola")
employee2 = Employee("Karol")
employee3 = Employee("Kasia")
employee4 = Employee("Jan")

employee1.printEmployeesList()