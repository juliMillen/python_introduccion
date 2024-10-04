## Funciones ##

def function1():
    print("Esto es una funcion")

function1()

def sum_two_values (first_value,second_value):
    suma = first_value + second_value
    print(suma)

sum_two_values (12,2)
sum_two_values("5","9")


def sum_two_values_with_return(first_value, second_value):
    return first_value + second_value

mi_suma = sum_two_values_with_return(20,2)
print(mi_suma)


def print_texts(*text):
    print(text)

print_texts("Hola","Python","Millen")
