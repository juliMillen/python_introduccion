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

# search

search = re.search("Esta es la leccion", my_string,re.I)
print(search)
start,end = search.span()
print(my_string[start:end])

# findall

findall = re.findall("leccion",my_string,re.I)
print(findall)


# split

print(re.split(":",my_string))

# sub

print(re.sub("Expresiones","expresiones",my_string))

print(re.sub("leccion","LECCION",my_string))


# Patterns

pattern = r"[lL]eccion"
print(re.findall(pattern,my_string))

pattern = r"[lL]eccion|Expresiones"
print(re.findall(pattern,my_string))

pattern = r"[a-z]"
print(re.findall(pattern,my_string))

pattern = r"[0-9]"
print(re.findall(pattern,my_string))


# email validation regular expression
email = "julianmillen1@gmail.com"
pattern =  r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]+$"
print(re.findall(pattern, email))
print(re.match(pattern,email))
print(re.search(pattern,email))
