# Zadanie:
# 1) Stwórz listę "names" z wartościami: Ola, Ania, Kasia
# 2) Z pomocą funkcji "map()" i lambdy dodaj do każdego imienia tekst " Kowalska"
# 3) Wyświetl nową listę w konsoli
# 4) Przefiltruj nową listę ze względu na długość tekstu, zachowaj w nowej liście tylko te, które mają więcej niż 12 znaków
# 5) Pokaż przefiltrowaną listę w konsoli


names = ["Ola", "Ania", "Kasia"]

fullNames = list(map( lambda x: x + " Kowalska", names))
print(fullNames)

longNames = list(filter(lambda x: len(x) > 12, fullNames))
print(longNames)