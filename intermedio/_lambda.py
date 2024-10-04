## Lambdas ##

sum_two_values = lambda first_value, second_value: first_value + second_value
print(sum_two_values(2,6))


multiply_values = lambda first_value, second_value: first_value * second_value
print(multiply_values(3,2))

def sum_three_values(value):
    return lambda first_value, second_value: first_value + second_value + value

print(sum_three_values(5)(2,4))