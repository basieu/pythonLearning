# Zadanie: W tym zadaniu wykorzystasz krotki do przechowywania i analizy danych demograficznych. Użyj podstawowych operacji na krotkach do manipulacji danymi oraz do wykonania prostych obliczeń
# 
# Kroki do wykonania:
# 1) Stwórz krotkę "population" zawierającą liczbę ludności w milionach dla pięciu wybranych krajów
# 2) Dodaj do krotki "population" dane dla kolejnego kraju
# 3) Wyświetl długość krotki "population", aby sprawdzić ile jest obecnie danych
# 4) Sprawdź, czy liczba 100 znajduje się w krotce "population"
# 5) Wyświetl liczbę ludności dla trzeciego kraju w krotce
# 6) Oblicz minimalną i maksymalną liczbę ludności w krotce "population"
# 7) Jeśli maksymalna liczba ludności w krotce jest większa niż 500, wyświetl komunikat "Znaleziono kraj o bardzo dużej populacji". W przeciwnym razie, wyświetl: "Wszystkie kraje mają populację poniżej 500 mln"

population = (38, 83, 320, 134, 432)
print(population)
population += (130,)
print(population)
print(len(population))
print("Czy jest kraj o populacji 100 mln?", 100 in population)
print(population[2])
print("Min:", min(population))
print("Max:", max(population))

if max(population) > 500:
    print("Znaleziono kraj o bardzo dużej populacji")
else:
    print("Wszystkie kraje mają populację poniżej 500 mln")