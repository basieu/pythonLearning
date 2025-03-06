# Zadanie: String upper, lower, strip
# 1) Napisz funkcję "getUserInformation" z trzema parametrami:
#    - name
#    - surname
#    - job
# 2) W "getUserInformation" zmień imię i nazwisko na duże litery, zawód na małe, dodatkowo wyczyść te wartości z białych znaków na ich początku i końcu
# 3) Połącz imię i nazwisko wraz z innym tekstem, aby uzyskać np:
#    "imię: ANIA, nazwisko: KOWALSKA, zawód: testerka
# 4) Zwróć powstały tekst z funkcji
# 5) Wywołaj funkcję "getUserInformation" na następujących danych i pokaż wynik w konsoli:
#    - Ania, Kowalska, Programistka
#    - Daniel, Lis, Administrator

def getUserInformation(name, surname, job):
    name = name.strip().upper()
    surname = surname.strip().upper()
    job = job.strip().lower()
    total = "imię: " + name + ", nazwisko: " + surname + ", zawód: " + job
    return total

print(getUserInformation(" Ania ", "Kowalska   ", "     Programistka"))
print(getUserInformation(" Daniel ", "          Lis", "     Administrator     "))