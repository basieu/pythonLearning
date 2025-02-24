# Zadanie: Napisz program, który oblicza ostateczną cenę produktu po zastosowaniu rabatu. Program powinien prosić użytkownika o wprowadzenie ceny początkowej produktu, a następnie obliczyć i wyświetlić cenę końcową
# 
# Kroki do wykonania:
# 1) Napisz funkcję "calculateFinalPrice", która przyjmuje dwa parametry: "initialPrice" (cena początkowa produktu) oraz "discount" (rabat w procentach)
# 2) W funkcji oblicz cenę produktu po rabacie i zwróć tę wartość
# 3) Poproś użytkownika o wprowadzenie ceny początkowej produktu oraz wielkości rabatu.
# 4) Wywołaj funkcję "calculateFinalPrice" z wprowadzonymu wartościami i przechowaj wynik
# 5) Wyświetl ostateczną cenę produktu.

def calculateFinalPrice(initialPrice, discount):
    finalPrice = initialPrice - initialPrice * discount
    return finalPrice

initalPrice = float(input("Wprowadź cenę początkową:"))
discount = float(input("Wprowadź wysokość rabatu (w %):"))/100

print("Cena po rabacie:", calculateFinalPrice(initalPrice, discount))