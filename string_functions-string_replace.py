# Zadanie: String replace
# 1) Stwórz funkcję "cleanText", która będzie czyścić przekazany tekst z określonych słów
# 2) Użyj funkcji "replace" do zamiany podanych słów na wykropkowane, które wielokrotnie może pojawić się w przekazanym łańcuchu, np. php zmienisz na ***, java na **** itd.
# 3) Zastąp następujące słowa kluczowe:
#    JavaScript, java, php, html, css
# 4) Zwróć wyczyszczony tekst z funkcji "cleanText"
# 5) Wywołaj funkcję na następującym lub podobnym tekście:
#    """Programowanie zacząłem z językiem php, następnie poznałem: html i css, ale obecnie skupiam się na JavaScript"""
# 6) Pokaż wynik w konsoli

keyWords = ["JavaScript", "java", "php", "html", "css"]

text = "Programowanie zacząłem z językiem php, następnie poznałem: html i css, ale obecnie skupiam się na JavaScript"

def cleanText(someText):
    for i in keyWords:
        x = len(i)
        someText = someText.replace(i, "*" * x)
    print(someText)

cleanText(text)

print(text)
