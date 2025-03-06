# Zadanie: Napisz program sprawdzający, czy adres email jest poprawnie napisany
# 
# Kroki do wykonania:
# 1) Napisz funkcję "validateEmail", sprawdzającą w podstawowy sposób, czy email jest prawidłowy
# 2) Wykorzystaj "find()" do wyszukania fragmentów tekstu w email:
#    - sprawdź, czy istnieje w przekazanym do funkcji emailu znak @, zapisz index w "monkeyIndex"
#    - posiadając pozycję @, sprawdź czy istnieje znak kropki po małpie. Zapisz pozycję kropki w "dotIndex"
#    - jeżeli wszystkie powyższe warunki są spełnione zwróć "True", w innym wypadku "False"
# 3) Wywołaj funkcję z następującymi mailami, pokaż w konsoli, co zwraca funkcja:
#    - asia@example.com
#    - karol@domena
#    - user.com

def validateEmail(email):
    monkeyIndex = email.find("@")
    dotIndex = email.find(".")
    if monkeyIndex >= 0 and dotIndex >= 0 and monkeyIndex < dotIndex:
        return True
    else:
        return False
    
# Walidacja dopuszczająca kropkę przed znakiem "@"
def validateEmail2(email):
    monkeyIndex = email.find("@")
    dotIndex = email.rfind(".")
    if monkeyIndex >= 0 and dotIndex >= 0 and monkeyIndex < dotIndex:
        return True
    else:
        return False
    

print("Walidacja (wariant 1) dla adresu - asia@example.com |", validateEmail("asia@example.com"))
print("Walidacja (wariant 1) dla adresu - karol@domena |", validateEmail("karol@domena"))
print("Walidacja (wariant 1) dla adresu - user.com |", validateEmail("user.com"))
print("Walidacja (wariant 1) dla adresu - asia.kowalska@example.com |", validateEmail("asia.kowalska@example.com"))
print("\nWalidacja (wariant 2) dla adresu - asia@example.com |", validateEmail("asia@example.com"))
print("Walidacja (wariant 2) dla adresu - karol@domena |", validateEmail2("karol@domena"))
print("Walidacja (wariant 2) dla adresu - user.com |", validateEmail2("user.com"))
print("Walidacja (wariant 2) dla adresu - asia.kowalska@example.com |", validateEmail2("asia.kowalska@example.com"))