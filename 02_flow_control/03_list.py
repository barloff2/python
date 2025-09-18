###
# 03 - Listas
# Secuencias mutables de elementos
# Pueden contener elementos de diferentes tipos
###
import os

os.system('cls' if os.name == 'nt' else 'clear')
# Creción de listas
print("\nCreación de listas")
lista1 = [1, 2, 3, 4, 5] # Lista de enteros
lista2 = ["manzanas", "peras", "platanos"] # Lista de cadenas
lista3 = [1, "dos", 3.0, True] # Lista de tipos mixtos

lista_vacia = [] # Lista vacía
lista_de_listas = [[1, 2], ["calcetin", 4]] # Lista de listas
matrix = [[1, 2], [2, 3], [4, 5]] # Matriz

print(lista1)
print(lista2)
print(lista3)
print(lista_vacia)
print(lista_de_listas)
print(matrix)

# Acceso a elementos por indice

print("\nAcceso a elementos por índice")
print(lista2[0]) # manzanas
print(lista2[1]) # peras
print(lista2[-1]) # platanos (último elemento)
print(lista2[-2]) # peras (penúltimo elemento)

print(lista_de_listas[1][0]) # 3 (primer elemento de la segunda lista)

# Slicing (rebanado)
print("\nSlicing (rebanado)")
lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista1[1:4]) # [2, 3, 4] (elementos desde el índice 1 hasta el 3)
print(lista1[:3]) # [1, 2, 3] (elementos desde el inicio hasta el índice 2)
print(lista1[3:]) # [4, 5] (elementos desde el índice 3 hasta el final)
print(lista1[:]) # [1, 2, 3, 4, 5] (copia de toda la lista)

# HAY MÁS MAGIA
#print(lista1[desde:hasta:paso]) # paso indica el incremento entre índices (1 por defecto) 
print(lista1[::3]) # [1, 3, 5] (elementos en índices pares)
print(lista1[::-1]) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] (lista invertida)

# Modificar una lista
print("\nModificar una lista")
lista1[0] = 100 # Cambiar el primer elemento
print(lista1)

# Añadir elementos a una lista
print("\nAñadir elementos a una lista")
lista1 = [1, 2, 3]

#forma larga y menos eficiente
lista1 = lista1 + [4, 5, 6] # Concatenar listas
print(lista1)

#forma corta y más eficiente
lista1 += [7, 8, 9] # Concatenar listas
print(lista1)



