# Program ma na celu kwalifikację kandydatów do oddania krwi
# 1) Dodaj zmienną 'age' o wartości 18 oraz weight = 50
# 2) Napisz instrukcję wawrunkową 'if else' sprawdzającą czy kandydat ma wiek większy lub równy 18, jeśli tak, sprawdź kolejną instrukcją if else czy jego waga jest większa lub równa 50.
#    Jeśli oba warunki są spełnione, napisz w konsoli, że może oddać krew
# 3) W przypadku, gdy jakiś warunek nie jest spełniony, to po else napisz w konsoli dlaczego 


age = 18
weight = 50

if age >= 18:
    if weight >= 50:
        print("Kandydat może oddać krew.")
    else:
        print("Kandydat waży zbyt mało (", weight, "kg), by odddać krew.")
else:
    print("Kandydat jest zbyt młody (", age, "lat), by oddać krew.")


age = 15
weight = 50

if age >= 18:
    if weight >= 50:
        print("Kandydat może oddać krew.")
    else:
        print("Kandydat waży zbyt mało (", weight, "kg), by odddać krew.")
else:
    print("Kandydat jest zbyt młody (", age, "lat), by oddać krew.")


age = 20
weight = 48

if age >= 18:
    if weight >= 50:
        print("Kandydat może oddać krew.")
    else:
        print("Kandydat waży zbyt mało (", weight, "kg), by odddać krew.")
else:
    print("Kandydat jest zbyt młody (", age, "lat), by oddać krew.")