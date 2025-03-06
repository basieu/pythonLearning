# Zadanie: String to int, float conversion
# 1) Pobierz liczbę całkowitą od użytkownika do zmiennej za pomocą funkcji "input", przekaż do niej informację: "Podaj liczbę całkowitą"
# 2) Zmień typ wartości z tekstu na liczbę całkowitą
# 3) Stwórz funkcję "calculateSquareArea" z parametrem "height", która zwraca powierzchnię kwadratu
# 4) Wywołaj funkcję z wcześniej pobraną liczbą całkowitą, wynik pokaż w konsoli
# 5) Pobierz od użytkownika liczbę dziesiętną
# 6) Oblicz powierzchnię kwadratu z podaną liczbą dziesiętną, zaokrąglij wynik do dwóch miejsc po przecinku i pokaż w konsoli

def calculateSquareArea(height):
    return height * height

intNumber = int(input("Podaj liczbę całkowitą: "))

print(calculateSquareArea(intNumber))

floatNumber = float(input("Podaj liczbę dziesiętną (z kropką): "))

print(calculateSquareArea(floatNumber))
print(round(calculateSquareArea(floatNumber), 2))