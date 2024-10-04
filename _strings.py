### STRINGS ###
my_string = "My string"

my_other_string = 'Mi otra otro string'

print(len(my_string))
print(len(my_other_string))

### CONCATENACION ###
print(my_string + " " + my_other_string)

my_new_line_string= "Es un string \n con salto de linea"
print(my_new_line_string)


my_tab_string = "\tEste es un string con tabulacion"
print(my_tab_string)


my_scape_String = "\tEste es un String \n escapado"
print(my_scape_String)

## Formateo ##
name, surname,age = "Julian", "Millen", 24
print("Mi nombre es %s %s y mi edad es %s".format(name,surname,age))
print("Mi nombre es %s %s y mi edad es %s" %(name,surname,age))



##Desempaquetado de caracteres ##
language = "Python"
a, b, c, d, e, f = language
print(a)
print(b)


##Division

language_slice = language[1:3]
print(language_slice)


##Reverse
reversed_language = language[::-1]
print(reversed_language)
