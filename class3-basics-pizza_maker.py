# Zadanie: Stwórz prostą klasę "Pizza", która pozwoli na tworzenie obiektu pizzy z listą składników
# 
# Kroki do wykonania:
# 1) Zdefiniuj klasę "Pizza" z konstruktorem, który tworzy atrybut "ingredients", będący pustą listą na start.
# 2) Dodaj metodę "addIngredient", która przyjmuje jeden parametr - składnik do dodania do pizzy. Sprawdź, czy składnik jest typu "str", jeśli tak - dodaj go do listy.
# 3) Dodaj metodę "showIngredients", która wyświetla wszystkie składniki pizzy.
# 4) Stwórz instancję klasy "Pizza"
# 5) Dodaj składniki do pizzy, używając metody "addIngredient":
#    - "ser"
#    - "pomidor"
#    - "pieczarki"
# 6) Wyświetl składniki pizzy, wywołując metodę "showIngredients"

class Pizza:
    def __init__(self):
        self.ingredients = []

    def addIngredient(self, ingredient):
        if isinstance(ingredient, str):
            self.ingredients.append(ingredient)

    def showIngredients(self):
        print("Składniki pizzy:")
        for i in self.ingredients:
            print(" -", i)

pizza = Pizza()
pizza.addIngredient("ser")
pizza.addIngredient("pomidor")
pizza.addIngredient("pieczarki")
pizza.showIngredients()