## Error types ##

# SyntaxError
#print "Hola velez"

#correccion
print("Hola velez")

# NameError
#print(name)

#correccion
name = "Julian"
print(name)

# IndexError
my_list = ["Java","C#","JavaScript","Python","Swift"]
#print(my_list[5])

#correccion debe ser un numero valido de indice en la lista
print(my_list[1])
print(my_list[0])
print(my_list[3])


# ModuleNotFoundError

#import maths

#correccion
import math


# AttributeError
#print(math.PI)

#correccion
print(math.pi)


# KeyError

my_dict = {"Nombre":"Julian","Apellido":"Millen","Edad":24}
#print(my_dict[2])

#correccion
print(my_dict["Nombre"])


# TypeError
#print(my_list["Nombre"])  ##my_list debe recibir un entero como indice, no un string, por eso da error
print(my_list[3])



# ImportError

#from math import PI
from math import pi 
print(pi)