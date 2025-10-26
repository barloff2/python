import numeros
from os import system


'''Modulo para lógica del programa'''

nuevoTurno = True
perfumeria = numeros.turno_perfumeria()
cosmeticos = numeros.turno_cosmeticos()
farmacia = numeros.turno_farmacia()


def validar_opcion(num):
    try:
        return int(num)
    except TypeError:
        print('No es una opción valida')
        return -1


def nuevo_turno():
    opcion = validar_opcion(input('Desea un nuevo turno?\n1- Sí\n2- No\n'))
    if opcion == 1:
        return True
    elif opcion == 2:
        return False
    else:
        print('Se creará nuevo turno por defecto')
        return True


def limpiar_pantalla():
    system('cls')


while nuevoTurno:
    limpiar_pantalla()
    valor = validar_opcion(
        input('1- Perfumería \n2- Farmacia \n3- Cosméticos\n')
    )
    if valor < 0:
        continue
    elif valor == 1:
        limpiar_pantalla()
        numeros.decorador(perfumeria)
        nuevoTurno = nuevo_turno()
    elif valor == 2:
        limpiar_pantalla()
        numeros.decorador(farmacia)
        nuevoTurno = nuevo_turno()
    else:
        limpiar_pantalla()
        numeros.decorador(cosmeticos)
        nuevoTurno = nuevo_turno()
