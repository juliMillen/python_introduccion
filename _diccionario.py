### Dictionaries ###

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre":"Julian","Apellido":"Millen","Edad":24}
print(my_other_dict)

my_dict = {
    "Nombre":"Julian",
    "Apellido":"Millen",
    "Edad":24,
    "Lenguajes": {"Java","C#","Python"}
}
print(my_other_dict)
print(my_dict)

print(len(my_other_dict))

print(my_dict["Nombre"])

my_dict["Nombre"] = "Ricardo"
print(my_dict["Nombre"])

#print(my_dict[1])

my_dict["Calle"] = "Calle Millen"
print(my_dict)

del my_dict["Calle"]
print(my_dict)

print("Julian" in my_dict)  
print("Apellido" in my_dict) #Lo que hacemos aca es buscar por clave

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_new_dict = my_other_dict.fromkeys(("Nombre",1))
print(my_new_dict)
