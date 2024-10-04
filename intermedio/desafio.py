## ejercicio para practicar ##
''''
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
'''

def fizzBuzz():
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 5 == 0:
            print("buzz")
        elif i % 3 == 0:
            print("fizz")
        else:
            print(i)


fizzBuzz()

""""
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 """

def es_Anagrama(texto,texto2):

    if texto.lower() == texto2.lower():
        return False
    return sorted(texto.lower()) == sorted(texto2.lower())

print(es_Anagrama("bmx","xmb"))


'''
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
 '''

def fibonacci():
    prev = 0
    next = 1

    for i in range(0,50):
       print(prev)
       fib = prev + next
       prev = next
       next = fib

fibonacci()


'''
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
 '''

def es_Primo():
    for number in range(1,101):

        if number >= 2:

            es_divisible = False

            for i in range(2,number):
                if(number % i == 0):
                    es_divisible = True
                    break
            if not es_divisible:
                print(number)


es_Primo()







