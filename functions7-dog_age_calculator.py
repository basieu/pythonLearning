# Zadanie: Napisz program, który przelicza wiek psa na ludzkie lata. Program powinien prosić użytkownika o wprowadzenie wieku psa, a następnie obliczyć i wyświetlić jego wiek w ludzkich latach . Pierwsze dwa lata życia psa liczymy jako 10.5 ludzkiego roku każdy, a każdy kolejny rok jako 4 ludzkie lata.
# 
# Kroki do wykonania:
# 1) Zdefiniuj funkcję "calculateHumanYears", która przyjmuje wiek psa jako parametr. W funkcji użyj instrukcji "if-elif-else" do obliczenia wieku psa w ludzkich latach. Dla uproszczenia załóżmy, że ilość lat mniejsza lub równa 2 musi być pomnożona przez 10.5, a dla większych wartości trzeba zastosować działanie 21 + (dogYears - 2) * 4
# 2) Użyj pętli, aby umożliwić użytkownikowi wielokrotne używanie kalkulatora bez restartowania programu
# 3) Poproś użytkownika o wprowadzenie wieku psa
# 4) Wywołaj funkcję "claculateHumanYears" i przekaż jej wiek psa wprowadzony przez użytkownika
# 5) Wyświetl obliczony wiek psa w ludzkich latach 


def calculateHumanYears(dogYears):
    if dogYears <= 0:
        print("Błąd! Wiek psa nie może być zerem lub liczbą ujemną")
    else:
        if dogYears <= 2:
            result = dogYears * 10.5
            print("Wiek psa w ludzkich latach:", result)
        else:
            result = 21 + (dogYears - 2) * 4
            print("Wiek psa w ludzkich latach:", result)


while True:
    dogYears = float(input("Wprowadź wiek psa: "))
    calculateHumanYears(dogYears)

    again = input("Czy chcesz kontynuować? tak/nie ")
    if again.lower() != "tak": break