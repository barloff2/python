###
# 04 - Listas Métodos
#Los métodos mas importantes para trabajar con listas
###

import os
os.system('cls' if os.name == 'nt' else 'clear')


lista1 = ['a', 'b', 'c', 'd']

#append() -> Agrega un elemento al final de la lista
lista1.append('e')
print("append() ->", lista1)

#insert() -> Agrega un elemento en la posición indicada
lista1.insert(1, '@')
print("insert() ->", lista1)

#extend() -> Agrega los elementos de una lista a otra
lista1.extend(['🏃', '😍' ])
print("extend() ->", lista1)

#remove() -> Elimina el primer elemento con el valor indicado
lista1.remove('@') #Elimina el primer elemento que encuentra con el valor '@'
print("remove() ->", lista1)

#pop() -> Elimina el elemento en la posición indicada y lo retorna
ultimo = lista1.pop() #Elimina el último elemento de la lista y lo retorna.
print("Elemento eliminado con pop():", ultimo)
print("pop() ->", lista1)
#tambien se puede eliminar un elemento en una posición específica, por ejemplo: lista1.pop(1)
lista1.pop(1) #Elimina el elemento en la posición 1
print("pop(1) ->", lista1)

del lista1[-1]  #Elimina el último elemento de la lista a lo bestia.
print("del lista1[-1] ->", lista1)

#clear() -> Elimina todos los elementos de la lista
lista1.clear() #Deja la lista vacía
print("clear() ->", lista1)

#eliminar un rango de elementos

lista1 = ['😺', '😸', '😹', '😻', '😼', '😽', '🙀', '😿', '😾']
print(lista1)
del lista1[1:3] #Elimina los elementos desde la posición 2 hasta la 4 (5 no incluido)
print("del lista1[1:3] ->", lista1)

#Mas metodos utiles

print("Ordenar listas modificando la original") #No devuelve nada, modifica la lista original
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
numbers.sort() #Ordena la lista de menor a mayor
print("sort() ->", numbers)

print("Ordenar listas creando una nueva")
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_numbers = sorted(numbers) #Crea una nueva lista ordenada de menor a mayor
print("sorted() ->", sorted_numbers)
print("Original:", numbers)

print("Ordenar una lista de cadenas de texto todo minuscula")

frutas = ['banana', 'manzana', 'kiwi', 'pera', 'naranja']
sorted_frutas = sorted(frutas) #Ordena la lista de cadenas de texto alfabéticamente
print("sorted() ->", sorted_frutas)

print("Ordenar una lista de cadenas de texto (mezclas de mayusculas y minusculas)")

frutas = ['banana', 'Manzana', 'Kiwi', 'pera', 'Naranja']
frutas.sort(key=str.lower) #Ordena la lista de cadenas de texto alfabéticamente sin importar mayusculas o minusculas
print("sort(key=str.lower) ->", frutas)


#Más cositas útiles
animals = ['🐼', '🐸', '🦁', '🐷', '🐵', '🐶', '🐺', '🐱', '🐭', '🐹', '🐰', '🐼']
print(len(animals)) #len() -> Devuelve la cantidad de elementos en la lista
print(animals.count('🐼')) #count() -> Devuelve la cantidad de veces que aparece un elemento en la lista
print('🐶' in animals) #in -> Devuelve True si el elemento está en la lista, False si no
print('🦊' in animals) #in -> Devuelve True si el elemento está en la lista, False si no