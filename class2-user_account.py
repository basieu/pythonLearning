# Zadanie: W tym zadaniu stworzysz prostą klasę reprezentującą konto użytkownika. Będziesz zarządzać podstawowymi informacjami o użytkowniku oraz umożliwisz zmianę hasła
# 
# Kroki do wykonania:
# 1) Stwórz klasę "User", która w konstruktorze przyjmuje dwa parametry:
#    - username
#    - password
#   Zapisz te wartości jako atrybuty obiektu.
# 2) Dodaj metodę "changePassword", która przyjmuje dwa argumenty:
#    - oldPassword
#    - newPassword
#   Sprawdź, czy stare hasło zgadza się z obecnym hasłem użytkownika. Jeśli tak, zmień hasło na nowe.
# 3) Stwórz instancję klasy "User" z przykładowym użytkownikiem.
# 4) Spróbuj zmienić hasło użytkownika za pomocą metody "changePassword". Najpierw użyj nieprawidłowego starego hasła, a następnie nowego

class User:
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password

    def changePassword(self, oldPassword, newPassword):
        if self.password == oldPassword:
            self.password = newPassword
            print("Hasło zostało zmienione")
        else:
            print("Nieprawidłowe dane")

    def showUser(self):
        print(self.username, self.password)


user1 = User("Ania", "zaq12WSX")
user1.changePassword("abcd", "zaq1@WSX")
user1.changePassword("zaq12WSX", "zaq1@WSX")
