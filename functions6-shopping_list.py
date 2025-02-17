# Zadanie: Napisz program, który tworzy i wyświetla listę zakupów na podstawie wprowadzonych przez użytkownika produktów. Program nie będzie zwracał żadnej wartości, ale bezpośrednio wyświetli listę zakupów w konsoli
# 
# Kroki do wykonania:
# 1) Zdefiniuj funkcję "displayShoppingList", która przyjmuje jeden parametr: "shoppingList". Funkcja ta powinna wyświetlać wszystkie elementy listy zakupów, każdy element w nowej linii
# 2) Stwórz pustą listę zakupów
# 3) W pętli, poproś użytkownika o wprowadzenie nazw produktów do listy zakupów, aż do wpisania słowa "koniec"
# 4) Po zakończeniu wprowadzania, wywołaj funkcję "displayShoppingList", przekazując jej listę zakupów


def displayShoppingList(shoppingList):
    print("Lista zakupów:")
    for i in shoppingList:
        print("- ", i)


shoppingList = []

while True:
    element = input("Wprowadź element do listy zakupów: ")
    if element.lower() == "koniec": break
    shoppingList.append(element)


displayShoppingList(shoppingList)