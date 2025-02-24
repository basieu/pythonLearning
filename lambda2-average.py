# Zadanie: Napisz program kalkulatora, który oblicza średnią arytmetyczną z listy liczb. Program powinien używać funkcji lambda, map oraz reduce do przetworzenia listy liczb i obliczenia wyniku.
# 
# Kroki do wykonania:
# 1) Zdefiniuj listę liczb, dla której ma zostać obliczona średnia arytmetyczna
# 2) Użyj funkcji map i lambda do przekształcenia listy liczb, jeśli to konieczne
# 3) Wykorzystaj funkcję reduce i lambda do obliczenia sumy wszystkich liczb z listy
# 4) Oblicz średnią arytmetyczną dzieląc sumę przez ilość liczb w liście
# 5) Wyświetl wynik

from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

doubleNumbers = list(map(lambda x: x * 2, numbers))

sumOfNumbers = reduce(lambda x, y: x + y, numbers)
sumOfDoubles = reduce(lambda x, y: x + y, doubleNumbers)

average = sumOfNumbers / len(numbers)
average2 = sumOfDoubles / len(doubleNumbers)

print("Średnia z numbers:", average)
print("Średnia z doubles:", average2)

