from random import randint
import os
os.system('cls')
intentos = 1
numero = randint(1,101)
nombre = input('Inserta tú nombre: ')
print(f'Hola {nombre}, he pensando un número entre 1 y 100, tienes ocho intentos para adivinarlo')


while intentos <= 8:
    num = int(input('Inserta un número: '))
    if num < 0 or num > 100:
        print('Ha elegido un número incorrecto')
    elif num < numero:
        print('Es incorrecto, ha elegido un número menor al secreto, subate ⬆️')
    elif num > numero:
        print('Es incorrecto, ha elegido un número mayor al secreto, bajate ⬇️')
    else:
        print(f'Has ganado en {intentos} intentos')
        break
    intentos += 1