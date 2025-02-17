# Liczby nieparzyste dodane do set
# 1) Dodaj listę "numbers" z wartościami od -3 do 3 z krokiem co 1
# 2) Dodaj "set" z wartością początkową -1
# 3) Stwórz pętlę "for in" z tablicą "numbers"
# 4) W każdej iteracji pętli sprawdź, czy liczba z listy jest nieparzysta, a następnie dodaj nieparzystą liczbę do zestawu
# 5) Wyświetl w konsoli nieparzyste liczby w "set" z pomocą pętli "for"


numbers = [-3, -2, -1, 0, 1, 2, 3]
set = {-1}
for x in numbers:
    if x % 2 != 0:
        set.add(x)


for i in set:
    print(i)