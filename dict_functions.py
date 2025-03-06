# Zadanie: W tym zadaniu będziesz używać słowników do zarządzania prostą książką adresową. Nauczysz się dodawać, usuwać, kopiować oraz przeszukiwać dane w słowniku
# 
# Kroki do wykonania:
# 1) Stwórz słownik "addressBook" zawierający początkowo jedną osobę: Jan Kowalski, mieszka w Gdańsku, kod pocztowy 80-000
# 2) Dodaj do książki adresowej nową osobę: Anna Nowak, mieszka w Warszawie, kod pocztowy 00-001
# 3) Usuń Jan Kowalski z książki adresowej
# 4) Skopiuj książkę adresową do nowej zmiennej i sprawdź, czy kopia jest identyczna (porównaj referencje i zawartość)
# 5) Sprawdź, czy w skopiowanej książce jest osoba, która mieszka w Krakowie. Jeśli nie, wyświetl odpowiedni komunikat
# 6) Wyświetl wszystkie klucze i wartości w książce adresowej

addressBook = {
    "Jan Kowalski": {
        "city": "Gdańsk", 
        "postalCode": "80-000"
    }
}

addressBook["Anna Nowak"] = {"city": "Warszawa", "postalCode": "00-001"}

print(addressBook)
del addressBook["Jan Kowalski"]
print(addressBook)

newBook = addressBook.copy()

print(newBook)
print(id(newBook))
print(id(addressBook))

found = False
for i in newBook:
    if newBook[i]["city"] == "Kraków":
        found = True
        print(i, "mieszka w Krakowie")
    else:
        continue

if not found:
    print("Nikt z książki nie mieszka w Krakowie")

print(addressBook.keys())
print(addressBook.values())