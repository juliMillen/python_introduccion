### SETS ###

my_set = set() #creacion de un set
my_other_set = {}


print(type(my_set))
print(type(my_other_set)) #Inialmente es un diccionario

my_other_set = {"Julian","Millen",24}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add("Velez")
print(my_other_set) ##Un set no es una estructura ordenada
##Un set no admite repetidos

print("Julian" in my_other_set)
print("Julyan" in my_other_set)

my_other_set.remove("Velez")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

del my_other_set
#print(my_other_set)    elimina el set 


my_other_set = {"Kotlin","Swift","Python"}

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union({"C#","JavaScript"}))

print(my_new_set.difference(my_set))
