## Clases ##

class Persona:
    pass


print(Persona)
print(Persona())


class my_other_Person:
    def __init__(self, name, surname, alias= "Sin alias"):
        self.full_name = f"{name} {surname} {alias}"

    def walk (self):
        print(f"{self.full_name} Está caminando")

Persona = my_other_Person("Julian","Millen")
print(Persona.full_name)
Persona.walk()


my_person3 = my_other_Person("Ricardo","Kaka","Ricardinho")
print(my_person3.full_name)
my_person3.walk()
my_person3.full_name = "Ariel Millen velezano"
print(my_person3.full_name)
