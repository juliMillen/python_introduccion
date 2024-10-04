## Funciones de Orden Superior ##

def sum_one(value):
    return value + 1

def sum_two_values_and_one(first_value, second_value, fsum_one):
    return fsum_one(first_value + second_value)

print(sum_two_values_and_one(5,2, sum_one))