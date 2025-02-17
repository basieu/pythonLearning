# Napisz dwie funkcje konwertujące temperaturę:
# 1) Funkcja "cToF" skonwertuje stopnie Celsjusza na Fahrenheita z wzoru:
#    fahrenheit = celsius * 9 / 5 + 32
# 2) Funkcja "fToC" skonwertuje stopnie Fahrenheita na Celsjusza z wzoru:
#    celsius = (fahrenheit - 32) * 5 / 9
# 3) Pokaż wynik w konsoli
# 4) Skonwertuj 20°C na Fahrenheita
# 5) Skonwertuj 86°F na Celsjusza
# kod specjalnego znaku stopni ° \xB0


def cToF(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    return fahrenheit

def fToC(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


print("20\xB0 Celsjusza to", cToF(20),"\xB0 Fahrenheita")
print("86\xB0 Fahrenheita to", fToC(86),"\xB0 Celsjusza")