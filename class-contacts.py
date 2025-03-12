# Zadanie: Stwórz klasę "SimCard" reprezentującą kartę sim telefonu z kontaktami
# 1) Klasa ustawia atrybut/zmienną klasy "contacts" jako listę w konstruktorze
# 2) Dodaj metodę "addContact" przyjmującą oprócz "self" również parametry "name" i "telephone". Sprawdź funkcją "isinstance" czy przekazane dane są prawidłowe, czyli "str" i "int". Stwórz słownik z "name" i "telephone" i dodaj go do listy kontaktów obiektu powstałego na bazie klasy
# 3) Napisz metodę "showContacts", która w pętli pokaże kolejne kontakty w terminalu
# 4) Stwórz instancję klasy "SimCard"
# 5) Dodaj poniższe kontakty:
#    - "Ola", 98765432
#    - "Adam", 12345678
#    - 100, 12345789
#    - "Kasia", "numer"
#       Część danych jest nieprawidłowa, więc nie powinny być dodane przez "addContact"
# 6) Wyświetl kontakty z "showContacts()"

class SimCard:
    def __init__(self) -> None:
        self.contacts = []
    
    def addContact(self, name, telephone):
        contact = {
            "name": None,
            "telephone": None
        }

        if isinstance(name, str) and isinstance(telephone, int):
            contact["name"] = name
            contact["telephone"] = telephone
            self.contacts.append(contact)
    
    def showContacts(self):
        for i in self.contacts:
            print(i["name"], i["telephone"])

sim = SimCard()
sim.addContact("Ola", 98765432)
sim.addContact("Adam", 12345678)
sim.addContact(100, 12345789)
sim.addContact("Kasia", "numer")
sim.showContacts()
    