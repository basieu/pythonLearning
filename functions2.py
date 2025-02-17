# Zadanie ze zwracanym słownikiem użytkownika
# 1) Stwórz funkcję "createUser" z parametrami:
#    - name
#    - contact
# 2) W ciele funkcji stwórz zmienną "user", w której będzie słownik reprezentujący użytkownika. Dodaj do słownika nazwę użytkownika z parametru.
# 3) Parametr "contact" będzie mógł przyjąć tekst lub liczbę. Sprawdź za pomocą funkcji "isinstance" jaki typ ma przekazany parametr "contact". Jeżeli jest to typ "string", to poniższy kod zwróci wartość "True" dla zmiennej "contact" (isinstance(contact, str)), który przypiszesz do słownika użytkownika. Natomiast jeśli "contact" jest liczbą, to zakładamy, że jest to numer telefonu, więc zapisz element "telephone" w zwracanym słowniku użytkownika. Do sprawdzenia czy "contact" jest liczbą użyj isinstance(contact, int)
# 4) Wywołaj funkcję z dwoma przypadkami:
#    - imię Ola, contact (string): ola@example.com
#    - imię Kasia, contact (number): 987654321
# Pokaż w konsoli zwrócone słowniki


def createUser(name, contact):
    user = {
        "name": name,
        "email": None,
        "telephone": None
    }

    if isinstance(contact, str):
        user["email"] = contact
    elif isinstance(contact, int):
        user["telephone"] = contact
    return user

print(createUser("Ola", "ola@example.com"))
print(createUser("Kasia", 987654321))