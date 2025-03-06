# Zadanie: W tym zadaniu skorzystasz z operacji na listach do zorganizowania listy gości oraz listy potraw na imprezie
# 
# Kroki do wykonania:
# 1) Stwórz listę "guests" z pięcioma imionami gości
# 2) Wyświetl długość listy gości, aby sprawdzić, ilu masz gości
# 3) Dodaj jeszcze dwóch gości na koniec listy
# 4) Jeden z gości nie może przyjść. Usuń go z listy
# 5) Posortuj listę gości alfabetycznie i wyświetl ją
# 6) Stwórz listę "dishes" z trzema potrawami
# 7) Dodaj do listy potraw jeszcze dwie nowe potrawy
# 8) Wyświetl potrawę, która znajduje się na środku listy
# 9) Usuń ostatnią potrawę z listy
# 10) Sprawdź, czy na liście potraw znajduje się "pizza", jeśli tak, wyświetl komunikat "pizza jest na liście", w przeciwnym razie dodaj pizzę do listy potraw

guests = ["Ola", "Ania", "Jan", "Zuzia", "Kamil"]
dishes = ["hot-dog", "tortilla", "frytki"]

print(len(guests))
guests.extend(["Adam", "Kasia"])
print(guests)
guests.remove("Zuzia")
print(guests)
guests.sort()
print(guests)

print("\n")

print(dishes)
dishes.extend(["sushi", "tacos"])
print(dishes)
print(dishes[len(dishes)//2])
dishes.pop()
print(dishes)

if "pizza" in dishes:
    print("Pizza jest na liście")
else:
    dishes.append("pizza")
    print(dishes)