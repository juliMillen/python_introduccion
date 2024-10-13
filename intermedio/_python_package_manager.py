## Python Package Manager ##

# PIP
import numpy  ##pip install numpy

# pip --version

print(numpy.version.version)

numpy_array = numpy.array([14,24,34,44,55])
print(type(numpy_array))

print(numpy_array * 2) ##multiplica todos los elementos del array por 2


#import pandas ## pip install pandas

## pip list
## pip uninstall
## pip show numpy

import requests # pip install requests

response =  requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
print(response)
print(response.status_code)
print(response.json())

## Arithmetics Package

import arithmetics
my_sum = arithmetics.sum_wto_values(5,4)
print(my_sum)