# Zadanie z listą liczb od -4 do 4
# 1) Wyświetl w konsoli następujące informacje z użyciem pętli na liście oraz instrukcji "if else" w celu sprawdzenia czy liczba jest parzysta czy nieparzysta, dodaj informację w konsoli
# 2) Pamiętaj, że 0 będzie oddzielnym przypadkiem, który musisz sprawdzić jako pierwszy "if" i w jej bloku napisz w konsoli tekst: "Zero jest parzyste". Następnie w "elif" sprawdź, czy liczba jest parzysta czy nieparzysta

numbers = [-4, -3, -2, -1, 0, 1, 2, 3, 4]

for x in numbers:
    if x == 0:
        print("Zero jest parzyste")
    elif x % 2 == 0:
        print("Liczba", x, "jest parzysta")
    else:
        print("Liczba", x, "jest nieparzysta")