### Condicionales ###

my_condition = False

if my_condition: #Es lo mismo que if my_condition == True:
    print("Ejecutando la condicion del if")

my_condition = 5 * 5

if my_condition == 10:
    print("Ejecutando la condicion del segundo if")


if my_condition >= 10:
    print("Ejecutando la condicion del tercer if")


if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20")
elif my_condition == 25:
    print("Es igual a 25")
else:
    print("Es menor o igual que 10 o mayor o igual que 20")

print("La ejecucion continua")

my_string = "My cadena de texto"

if my_string:
    print("Mi cadena de texto no esta vacia")
