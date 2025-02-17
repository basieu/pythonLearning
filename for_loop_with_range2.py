# Zadanie: Napisz program, który utworzy listę zawierającą kwadraty liczb od 1 do N, gdzie N jest wartością wprowadzoną przez użytkownika. Na koniec program powinien wyświetlić utworzoną listę.
# 
# Kroki do wykonania:
# 1) Poproś użytkownika o wprowadzenie liczby N.
# 2) Użyj pętli "for" wraz z funkcją "range" do wygenerowania liczb od 1 do N.
# 3) Dla każdej liczby z tego zakresu, oblicz jej kwadrat i dodaj do listy.
# 4) Po zakończeniu pętli, wyświetl listę zawierającą kwadrat liczb.
# 5) Przed wyświetleniem, sprawdź za pomocą instrukji "if", czy lista nie jest pusta

N = int(input("Wprowadź ilość liczb: "))
squareList = []

for number in range(1, N+1):
    squareList.append(number ** 2)

if len(squareList) != 0:
    print(squareList)
else:
    print("Lista jest pusta")