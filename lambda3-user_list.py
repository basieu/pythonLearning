# Zadanie: Napisz program do przetwarzania danych użytkowników z listy
# 
# Kroki do wykonania:
# 1) Stwórz listę słowników "users", gdzie każdy słownik zawiera klucze "name" i "age" z przykładowymi danymi użytkowników
# 2) Użyj "filter()" do wyfiltrowania użytkowników, który mają więcej niż 18 lat
# 3) Użyj "map()" do podwojenia wieku przefiltrowanych użytkowników
# 4) Użyj "reduce" do zsumowania wszystkich lat po przetworzeniu
# 5) Wyświetl sumę lat przefiltrowanych i przetworzonych użytkowników

from functools import reduce

users = [
    {"name": "jan", "age": 15},
    {"name": "Anna", "age": 25},
    {"name": "Piotr", "age": 30},
    {"name": "Katarzyna", "age": 22}
]

adults = list(filter(lambda user: user["age"] > 18, users))

doubleAge = list(map(lambda y: y["age"] * 2, adults))

totalAge = reduce(lambda a, b: a + b, doubleAge)
print(totalAge)