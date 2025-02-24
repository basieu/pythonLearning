# Zadanie: Przekazywanie mutowalnych danych do funkcji, np. słownik
# 1) Utwórz słownik opisujący pracownika i zapisz go w zmiennej "employee". Do elementów słownika dodaj: name, email, rank (stopień - wpisz "programmer"), salary (8000)
# 2) Napisz funkcję "promoteToManager", która przyjmuje parametr o nazwie "user", gdzie przekazany będzie słownik.
# 3) Wewnątrz funkcji zmień wartości elementów przekazanego słownika "user", podnieś pensję o 50%, zmień "rank" na "manager". Dodatkowo sprawdź, czy przypadkiem przekazany pracownik już jest managerem, w takim wypadku podaj w konsoli, że osoba ta jest już managerem i wyjdź z funkcji z "return"
# 4) Wywołaj funkcję "promoteToManager" i przekaż utworzony na początku słownik, pokaż w konsoli, czy został on zaktualizowany.

employee = {
    "name": "Jan",
    "email": "jan@example.com",
    "rank": "programmer",
    "salary": 8000
}

def promoteToManager(user):
    user["salary"] += user["salary"] * 0.5
    if user["rank"] != "manager":
        user["rank"] = "manager"
    else:
        print("Ten pracownik już jest managerem")
        return
        
promoteToManager(employee)
print(employee)