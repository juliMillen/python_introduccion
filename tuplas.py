### tuplas ###

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35,1.77,'Julian','Millen')
my_other_tuple = (24,44,30)

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count("Millen")) #Si devuelve 1 es porque lo encontro y se devuelve 0 porque no se ha encontrado

print(my_tuple.index("Julian")) #Devuelve la posicion del valor

print(my_tuple + my_other_tuple)

my_sum_tuple = my_tuple + my_other_tuple
print("Esta es la suma de las dos tuplas: ",my_sum_tuple)

print(my_sum_tuple[3:6]) ## devuelve los valores entre 3 y 6

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[3] = "Poroto cubero"
my_tuple.insert(1,"Velez")
print(tuple(my_tuple))