# Zadanie na przekazanie danych funkcji przez wartość
# 1) Napisz funkcję "increaseSalary" z dwoma parametrami liczbowymi: "money" oraz "bonus"
# 2) W funkcji podnieś wartość "money" o 20%. Następnie zwróć sumę "money" i "bonus".
# 3) Stwórz zmienną "salary" poza funkcją o wartości 5000
# 4) Wywołaj funkcję "increaseSalary" przekazując jako argument "salary" oraz 1000 jako "bonus". Zachowaj zwracaną wartość w zmiennej "newSalary"
# 5) Pokaż w konsoli wartości: "salary" i "newSalary"

def increaseSalary(money, bonus):
    money += money * 0.2
    return money + bonus

salary = 5000

newSalary = increaseSalary(salary, 1000)

print(salary)
print(newSalary)
print("id salary:", id(salary))
print("id newSalary:", id(newSalary))