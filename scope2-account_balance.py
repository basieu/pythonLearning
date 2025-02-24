# Zadanie: Napisz program do zarządzania stanem konta użytkownika, któy pozwala na dodawanie i usuwanie środków oraz wyświetlanie aktualnego stanu konta. Program powinien korzystać z globalnej zmiennej do przechowywania stanu konta oraz zawierać funkcje do modyfikacji tego stanu i wyświetlenia go.
# 
# Kroki do wykonania:
# 1) Zdefiniuj globalną zmienną "accountBalance" z wartością początkową 0
# 2) Napisz funkcję "addFunds", która przyjmuje kwotę do dodania do konta. Funkcja ta powinna modyfikować globalną zmienną "accountBalance"
# 3) Napisz funkcję "withdrawFunds", która przyjmuje kwotę do wypłaty z konta. Sprawdź, czy stan konta pozwala na wypłatę - jeśli nie, wyświetl odpowiedni komunikat
# 4) napisz funkcję "displayBalance", która wyświetla aktualny stan konta
# 5) Zapytaj użytkownika w pętli o działanie (dodanie środków, wypłata, wyświetlenie stanu konta) i odpowiednio zareaguj, wywołując odpowiednią funkcję


accountBalance = 0

def addFunds(income):
    global accountBalance
    accountBalance += income
    print("Dodano środki do konta:", income)

def withdrawFunds(withdraw):
    global accountBalance
    if accountBalance > withdraw:
        accountBalance -= withdraw
        print("Wypłacono środki:", withdraw)
    else:
        print("Brak wystarczających środków na koncie!")

def displayBalance():
    print("Stan konta: ", accountBalance)

while True:
    operation = input("Jaką oparację chcesz wykonać (wpłata/wypłata/saldo/koniec)? ")
    if operation.lower() == "koniec": break
    elif operation.lower() == "wplata" or operation.lower() == "wpłata":
        inAmount = float(input("Podaj kwotę: "))
        addFunds(inAmount)
    elif operation.lower() == "wyplata" or operation.lower() == "wypłata":
        outAmount = float(input("Podaj kwotę: "))
        withdrawFunds(outAmount)
    elif operation.lower() == "saldo":
        displayBalance()
    else:
        print("Wpisz prawidłową nazwę transakcji")