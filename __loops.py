### Loops ###

#While

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else:
    print("Mi condicion es mayor o igual que 10")

print("La ejecucion continua")

#For

my_list = [35,44,14,24,39,55,67]

for element in my_list:
    print(element)

my_tuple = (35,1.77,"Julian","Millen")

for element in my_tuple:
    print(element)

'''''
my_set = {"Julian","Millen",24}
for element in my_set:
    print(element)
    if element == "Millen":
        break
else:
    print("El bucle for ha finalizado")
'''
