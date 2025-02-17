# 1) Napisz funkcję "findLargest", która przyjmuje dwie liczby jako parametry "num1" i "num2". Funkcja musi pokazać w konsoli informację, która liczba jest większa oraz jej wartość lub że liczby są równe
# 2) Dodatkowo funkcja zwraca większą liczbę dzięki "return"
# 3) Sprawdź funkcję, przekazując wartości 3 i 10, pokaż w konsoli wynik
# 4) Sprawdź funkcję, przekazując wartości 12 i 7, pokaż w konsoli wynik


def findLargest(num1, num2):
    if num1 > num2:
        print("num1 jest większe:", num1)
        return num1
    elif num1 < num2:
        print("num2 jest większe:", num2)
        return num2
    else:
        print("Liczby są równe:", num1)
        return num1



print(findLargest(3,10))
print(findLargest(12,7))
print(findLargest(5,5))