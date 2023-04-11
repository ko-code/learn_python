### Clases ###

class Person:

    def __init__(self, name, surname, alias = 'sin alias'):
        
        self.fullname = f"{name} {surname} {alias}"
        self.__name = name
        self.__surname = surname

    def get_name(self):
        return self.__name  

    def get_surname(self):
        return self.__surname  
    
    def walk(self):
        print(f"{self.fullname} esta caminando")

my_person = Person("Cristian", "Rojas")
my_person.walk()
# print(f"{my_person.name} {my_person.surname}")
my_person.get_name()

my_other_person = Person("Cristian", "Rojas", "R3tr0D3v")
my_other_person.name = "Gabriel"
my_other_person.walk()
