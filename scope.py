# Zadanie:
# 1) Stwórz globalną zmienną "employees", która jest pustą listą
# 2) Napisz funkcję "addEmployee", która przyjmuje "email" i "salary", wewnątrz stwórz słownik z tymi samymi parametrami. Następnie dodaj go do globalnej listy "employees", stosując funkcję "append"
# 3) Wywołaj funkcję "addEmployee" dla trzech dowolnych pracowników o pensjach: 6000, 8000, 10000, wpisz dowolne maile
# 4) Dodaj funkcję "increaseSalary" z dwoma argumentami: "employees" i "pctIncrease". Jako pierwszy argument będzie przekazywana lista pracowników, a do drugiego wartość podwyżki. Przejdź po wszystkich pracownikach i zwiększ pensję pracowników o przekazaną wartość procentową "pctIncrease"
# 5) Zwiększ pensje pracowników z funkcją "increaseSalary" o 20%, wyświetl listę w terminalu

employees = []

def addEmployee(email, salary):
    newEmployee = {"email": email, "salary": salary}
    employees.append(newEmployee)

addEmployee("jan@example.com", 6000)
addEmployee("ania@example.com", 8000)
addEmployee("ola@example.com", 10000)

def increaseSalary(employees, pctIncrease):
    for person in employees:
        person["salary"] *= 1 + pctIncrease / 100

increaseSalary(employees, 20)
print(employees)