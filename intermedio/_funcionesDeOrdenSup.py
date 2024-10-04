## Funciones de Orden Superior ##

def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

def sum_two_values_and_value(first_value, second_value, fsum_one):
    return fsum_one(first_value + second_value)

print(sum_two_values_and_value(5,2, sum_one))
print(sum_two_values_and_value(5,2,sum_five))


## Clousures ##
## retornan una funcion, no un valor u otra cosa

def sum_ten():
    def add(value):
        return value + 10
    return add

add_clousure = sum_ten()
print(add_clousure(5))

## sum_ten con parametros

def sum_tenn(original_value):
    def add(value):  
        return value + 10 + original_value
    return add

add_clousure2 = sum_tenn(1)
print(add_clousure2(5))


## Funciones de Orden superior incorporadas (Built-in Higher Order Function) ##

numbers = [2, 6, 10, 14, 20]

def multiply_two(number):
    return number * 2

## Map
print(list(map(multiply_two,numbers)))
print(list(map(lambda number: number * 2 ,numbers)))

