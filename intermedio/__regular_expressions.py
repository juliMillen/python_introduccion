## Regular Expressions ##
import re

my_string = "Esta es la leccion numero 7: Expresiones Regulares"
my_other_String = "Esta no es la leccion numero 6: Manejo de ficheros"

match = re.match("Esta es la leccion", my_string, re.I)
print(match)


print(re.match("Esta es la leccion", my_string))

match = print(re.match("Esta es la leccion", my_other_String))
if not (match == None):
    print(match)
    start,end = match.span()
    print(my_string[start:end])

print(re.match("Expresiones Regulares", my_string))