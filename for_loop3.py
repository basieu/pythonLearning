# 1) Stwórz krotkę z wartościami od 1 do 10
# 2) Zrób pętlę "for in" z krotką i wyświetl w konsoli tylko parzyste liczby. Skorzystaj z instrukcji warunkowej "if" oraz operatora % zwracającego resztę z dzielenia.

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

for x in numbers:
    if x % 2 == 0:
        print(x)