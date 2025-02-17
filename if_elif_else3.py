# Napisz program sprawdzający wymagania potencjallnego kandydata na programistę:
# 1) Dodaj zmienną 'experience' z wartością 2, kolejną 'languagues' z listą elementów: "python", "typesript", "javascript", "java"
#    Ostatnią zmienną będzie 'contractType' o wartości "b2b"
# 2) Wykorzystaj instrukcję 'if' z operatorem 'and' do sprawdzenia czy doświadczenie kandydata wynosi 2 lub więcej lat oraz czy zna język python i java.
#    Pamiętaj o wykorzystaniu operatora 'in' do sprawdzenia czy wartość jest w liście
# 3) Jeśli powyższe warunki są spełnione zrób kolejny 'if' i sprawdź czy typ kontraktu to "b2b" lub "employment"
#    Zaprezentuj w terminalu informację, że kandydat jest przyjęty, gdy warunki są spełnione.
# 4) W przypadku, gdy warunki nie są spełnione, pokaż w konsoli stosowny komunikat


experience = 2
languages = ["python", "typescript", "javascript", "java"]
contractType = "b2b"

if experience >= 2 and "python" in languages and "java" in languages:
    if contractType == "b2b" or contractType == "employment":
        print("Kandydat jest przyjęty")
    else:
        print("Kandydat oczekuje innej umowy:", contractType)
else:
    print("Kandydat nie spełnia warunków")