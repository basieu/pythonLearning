# Zadanie: Napisz program, który przeliczy wiek psa na ludzkie lata
# 
# Kroki do wykonania:
# 1) Poproś użytkownika o wprowadzenie wieku psa w latach i zapisz tę wartość do zmiennej.
# 2) Użyj instrukcji warunkowych, aby obliczyć wiek psa w ludzkich latach.
#     - Pierwszy rok życia psa to 15 ludzkich lat
#     - Drugi rok życia psa to 9 ludzkich lat
#     - Każdy kolejny rok to 5 ludzkich lat
# 3) Jeśli podana wartość wieku psa jest mniejsza niż 0, wyświetl komunikat o błędzie.
# 4) Wyświetl wynik obliczeń w konsoli.


dogAge = float(input("Wprowadź wiek psa: "))
humanAge = 0

if dogAge < 0:
    print("Wiek psa nie może być mniejszy niż 0")
elif dogAge <= 1:
    humanAge = dogAge * 15
elif dogAge <= 2:
    humanAge = 15 + (dogAge - 1) * 9
else:
    humanAge = 24 + (dogAge - 2) * 5

print("Wiek psa w ludzkich latach:", humanAge)