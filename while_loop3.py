# Zadanie: Napisz program, który oblicza średnią arytmetyczną z podanej przez użytkownika listy liczb. Program powinien prosić użytkownika o wprowadzenie liczby elementów do obliczenia średniej, a następnie o wprowadzenie każdej z tych liczb
# 
# Kroki do wykonania:
# 1) Poproś użytkownika o wprowadzenie liczby elementów, z których ma być obliczona średnia.
# 2) Zainicjuj zmienną "sum" z wartością 0, która będzie przechowywać sumę wprowadzonych liczb.
# 3) Użyj pętli "while" do pobrania od użytkownika określonej liczby elementów. Po wprowadzeniu każdej liczby, dodaj ją do zmiennej "sum".
# 4) Oblicz średnią arytmetyczną, dzieląc sumę przez liczbę elementów.
# 5) Wyświetl wynikową średnią arytmetyczną z dokładnością do dwóch miejsc po przecinku.
# 6) Jeśli użytkownik wprowadzi liczbę elementów równą 0, wyświetl informację, że nie można obliczć średniej z 0 elementów.

numOfElements = int(input("Podaj liczbę elementów do obliczenia średniej:"))
sum = 0
i = 0

if numOfElements > 0:
    i = numOfElements

    while i > 0:
        element = int(input("Wprowadź liczbę:"))
        sum += element
        i -= 1
    else:
        average = sum/numOfElements
        print("Średnia arytmetyczna z wprowadzonych liczb:", round(average,2))

else:
    print("Błąd!")