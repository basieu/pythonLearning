# Zadanie: String functions
# 1) Napisz funkcję "getEmailParts" przyjmującą parametr "email"
# 2) Wykorzystaj pobieranie fragmentów tekstu w python, aby rozłożyć email na części i zapisz je w zmiennych:
#    - user - od początku emaila do ostatniego znaku przed "@"
#    - domainName - tekst za "@" i przed kropką
#    - domainExt - tekst za ostatnią kropką do końca
# 3) Zwróć słownik z funkcji z elementami jak powyższe zmienne
# 4) Przetestuj funkcję na emailu:
#    - ola@domena.com

def getEmailParts(email):
    monkeyId = email.find("@")
    dotId = email.rfind(".")
    if monkeyId >= 0 and dotId >= 0 and monkeyId < dotId:
        user = email[0:monkeyId]
        domainName = email[monkeyId + 1 : dotId]
        domainExt = email[dotId + 1 : ]
        return {"user": user, "domainName": domainName, "domainExt": domainExt}
    else:
        return None


print(getEmailParts("ola@domena.com"))
print(getEmailParts("ola.kowalska@domena.com"))