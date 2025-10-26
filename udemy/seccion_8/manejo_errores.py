# try
# except
# finaly
from os import system
system('cls')


def suma():
    n1 = int(input("numero 1: "))
    n2 = int(input("numero 2: "))
    print(n1 + n2)
    print("Gracias por sumar" + n1)

# para validar error

# try:
#    #Código que se quiere probar
#    suma()
# except:
#    #Código a ejecutar si hay un error
#    print('hiciste algo mal')
# else:
#    # Código a ejecutar si no hay un error
#    print('Hiciste todo bien')
# finally:
#    #Código que se va a ejecutar de todos modos
#    print('eso fue todo')


# Llamar diferentes tipos de errores
# try:
#    suma()
# except TypeError:
#    print("Estas intentando concatenar tipos distintos")
# except ValueError:
#    print('Ese no es un número')
# else:
#    print('Hiciste todo bien')
# finally:
#    print('Eso fue todo')


# Ejemplo con un número solicitado por consola

def pedir_numero():
    while True:
        try:
            numero = int(input('Dame un número: '))
        except:
            print('Ese no es un número')
        else:
            print(f'Ingresaste el número {numero}')
            break
    print('gracias')


pedir_numero()
