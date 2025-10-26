from os import system
system("cls")
'''generadores: es una forma especial de funciones que devuelven un iterador'''

'''Funcion normal'''


def mi_funcion():
    lista = []
    for x in range(1, 5):
        lista.append(x * 10)
    return lista


'''Funcion generadora'''


def mi_generador():
    for x in range(1, 5):
        yield x * 10


print(mi_funcion())  # Llama a la funcion normal
print(mi_generador())  # Llama a la funcion generadora

# Para obtener el valor de la funcion generadora, se debe usar next()
generador = mi_generador()
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
# print(next(generador))  # ya no tiene mas numeros


# En el caso del generador se pueden colocar muchos yield y no va a
# Cancelar el flujo
def mi_generador():
    x = 1
    yield x

    x += 1
    yield x

    x += 1
    yield


g = mi_generador()

# Devuelve cada uno de los yield, se puede ejecutar
# Código entre cada llamada.
print(next(g))
print(next(g))

print('Hola mundo')

print(next(g))
