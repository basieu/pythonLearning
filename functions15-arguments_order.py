# Zadanie: Napisz program, który pozwoli użytkownikowi zarezerwować bilety na koncert
# 
# Kroki do wykonania:
# 1) Zdefiniuj funkcję "bookTickets", która pryjmuje nazwę zespołu jako argument pozycyjny ("band"), liczbę biletów jako argument pozycyjny, a rodzaj biletów i sekcję jako argumenty nazwane z domyślnymi wartościami jako "standard" i "general"
# 2) Funkcja powinna wyświetlać informacje o rezerwacji, włączając w to wszystkie podane detale
# 3) Poproś uśytkownika o wprowadzenie nazwy zespołu i liczby biletów, następnie tylko je przekaż przy wywołaniu funkcji


def bookTickets(band, numOfTickets, /, *, typeOfTickets = "standard", section = "general"):
    print("Nazwa zespołu:", band, "\nIlość biletów:", numOfTickets, "\nRodzaj biletów:", typeOfTickets, "\nSekcja:", section)

band = input("Podaj nazwę zespołu: ")
numOfTickets = int(input("Podaj ilość biletów: "))

bookTickets(band, numOfTickets)