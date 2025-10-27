''' Medir la eficiencia del código o la duración de la ejecución de un bloque de código '''
from os import system
import time
import timeit

# Funciones que realizan lo mismo


def prueba_for(numero):
    lista = []
    for num in range(1, numero + 1):
        lista.append(num)
    return lista


def prueba_while(numero):
    lista = []
    num = 1
    while num <= numero:
        lista.append(num)
        num += 1
    return lista


print(prueba_for(15))
print(prueba_while(15))

# Medir tiempo

inicio = time.time()
prueba_for(10)
fin = time.time()
print(f"Tiempo de ejecución (for): {fin - inicio} segundos")

inicio = time.time()
prueba_while(10)
fin = time.time()
print(f"Tiempo de ejecución (while): {fin - inicio} segundos")


# Ahora es el turno de timeit revisar tiempo de ejecución de un fragmento de código
# Para esto, se utiliza la función timeit.timeit()
declaracion ='''
prueba_for(10)
'''
# contenido de la función

mi_setup = '''
def prueba_for(numero):
    lista = []
    for num in range(1, numero + 1):
        lista.append(num)
    return lista
'''

# number es el numero de veces que se ejecute

duracion = timeit.timeit(declaracion, setup=mi_setup, number=1000000)
print(duracion)


declaracion2 = '''
prueba_while(10)
'''

mi_setup2 = '''
def prueba_while(numero):
    lista = []
    num = 1
    while num <= numero:
        lista.append(num)
        num += 1
    return lista
'''

duracion2 = timeit.timeit(declaracion2, setup=mi_setup2, number=1000000)
print(duracion2)