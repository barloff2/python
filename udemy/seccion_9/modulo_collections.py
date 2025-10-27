from collections import Counter
from os import system

system('cls')
''' Completar y manejar las estructuras de datos mas eficientes'''

# Comportamiento de listas

# Contar cuantos números repetidos hay en una lista, con counter
numeros = [1,2,3,4,5,5,6,3,4,1,2,6,7,7]
print(Counter(numeros))

# Tambien se puede contar los elementos de un string
print(Counter('misisipi'))

# Tambien con una frase, contar las palabras
frase = 'al pan pan y al vino vino'
print(Counter(frase.split()))

# Metodos de counter

serie = Counter([1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3])

# Mostrar los elementos mas comunes en tuplas
# Si se coloca un número como parametro elije el top
print(serie.most_common(1))

# Imprimir una lista creada apartir de los elementos de serie, devuelve los elementos unicos
print(list(serie))


#################################################################

system('cls')
from collections import defaultdict

# Diccionario por defecto.

mi_dic = {'uno' : 'verde', 'dos' : 'azul', 'tres' : 'rojo'}
print(mi_dic['dos'])

# Si quiero consultar una llave que no existe ahi fallaria el programa,
# en ese momento entra defaultdict


# En caso de que no exista una clave que estoy pidiendo le asigne el valor nada 
mi_dic = defaultdict(lambda: 'nada')

print(mi_dic['cuatro'])
print(mi_dic)

#################################################################

system('cls')
from collections import namedtuple

# Tupla con nombres

mi_tupla = (500, 18, 65)
print(mi_tupla[1])

# Acceder a la tupla atraves de un nombre
# se le asigna a un objeto
Persona = namedtuple('Persona', ['nombre', 'altura', 'peso'])

# Instanciar persona.
stiven = Persona('Stiven', 1.80, 110)

# llamar las propiedades
print(stiven.altura)
# llamar por indice
print(stiven[1])



#####################################################

from collections import deque
'''Agregar al inicio y al final elementos a una lista'''


lista_ciudades = deque(["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"])

# Agregar un elemento al final
lista_ciudades.append('Bogota')

# Agregar al inicio

lista_ciudades.appendleft('Santo Domingo')

print(lista_ciudades)

# Eliminar el último elemento
lista_ciudades.pop()

# Eliminar el primer elemento
lista_ciudades.popleft()

print(lista_ciudades)