# Zadanie: Napisz program, który dla podanego zakresu od 1 do N (gdzie N jest wartością wprowadzoną przez użytkownika) wypisze oddzielnie listy liczb parzystych i nieparzystych
# 
# Kroki do wykonania:
# 1) Poproś użytkownika o wprowadzenie liczby N, która określi zakres
# 2) Użyj pętli "for" z funkcją "range" do iteracji od 1 do N włącznie
# 3) Sprawdź za pomocą instrukcji warunkowej, czy aktualna liczba jest parzysta czy nieparzysta.
# 4) Dodaj liczby parzyste do jednej listy, a nieparzyste do drugiej
# 5) Po zakończeniu iteracji wyświetl obie listy.

N = int(input("Wprowadź ilość liczb: "))
evenNumbers = []
oddNumbers = []

for number in range(1, N+1):
    if number % 2 == 0:
        evenNumbers.append(number)
    else:
        oddNumbers.append(number)

if len(evenNumbers) != 0:
    print("Parzyste liczby z zakresu od 1 do", N, evenNumbers)
else:
    print("W danym zbiorze nie ma liczb parzystych")

if len(oddNumbers) != 0:
    print("Nieparzyste liczby z zakresu od 1 do", N, oddNumbers)
else:
    print("W danym zbiorze nie ma liczb nieparzystych")