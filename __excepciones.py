## Excepciones ##

numberOne = 5
numberTwo = 1
#numberTwo = "1"

try:
    print(numberOne + numberTwo)
    print(" No se ha producido un error")
except:
    print("se ha producido un error")

# try except else

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else:
    #Se ejecuta si no se produce una excepcion
    print("La ejecucion continua correctamente")
finally:
    #se ejecuta siempre
    print("La ejecucion continua")