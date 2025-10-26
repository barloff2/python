#Interacciones entre diferentes funciones
from random import shuffle
# lista inicial

palitos = ['-', '--', '---', '----']

# Función que mezcla los palitos

def mezclar(palitos):
    shuffle(palitos)
    return palitos

# Funcion que permite al usuario elegir un palito

def probar_suerte():
    intento = ''
    while intento not in ['1', '2', '3', '4']:
        intento = input('Elige un palito (1, 2, 3, 4): ')    
    return int(intento)

# Función que se encargue de comprobar si el palito es el más corto

def chequear_intento(lista_palitos, intento):
    if lista_palitos[intento - 1] == '-':
        print('A lavar los platos')
    else:
        print('¡Te has salvado!')
    print(f'Has elegido el palito {lista_palitos[intento - 1]}')

palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
chequear_intento(palitos_mezclados, seleccion)