# Zadanie: Napisz program, który przechodzi przez zagnieżdżoną listę (listę list) i wypisuje wszystkie jej elementy
# 
# Kroki do wykonania:
# 1) Stwórz zmienną "nestedList", która będzie zawierać kilka list z różnymi typami elementów.
# 2) Użyj zagnieżdżonej pętli "for" do przejścia przez wszystkie listy i ich elementy
# 3) Wypisz każdy element z każdej listy


nestedList = [
    [1, 2, 3],
    ["a", "b", "c"],
    [10, "Andrzej", 43, "ola@example.com"]
]

for singleList in nestedList:
    for x in singleList:
        print(x)