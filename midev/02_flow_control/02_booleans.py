###
# 02 - Booleans
# Valores lógicos: True (verdadeiro) e False (falso)
# Fundamentales para el control de flujo y la lógica en programación
###

import os
os.system("cls")

#Los Booleanos representan dos valores: True (verdadero) y False (falso)

print("\nValores Booleanos básicos:")
print(True)   # Imprime True
print(False)  # Imprime False

#Operadores de comparación devuelven valores booleanos
print("\nOperadores de comparación:")
print("5 > 3:", 5 > 3)     # True
print("5 < 3:", 5 < 3)     # False
print("5 == 5:", 5 == 5)   # True (igualdad)
print("5 != 3:", 5 != 3)   # True (desigualdad)
print("5 >= 5:", 5 >= 5)   # True (mayor o igual)
print("5 <= 3:", 5 <= 3)   # False (menor o igual)  

print("\nComparación de cadenas:")
print("manzana < pera:", "manzana" < "pera")  # True (orden alfabético)
print("'Hola' == 'hola':", "Hola" == "hola")  # False (distingue mayúsculas)

#Operadores lógicos combinan valores booleanos
print("\nOperadores lógicos:") 
print("True and True:", True and True)     # True
print("True and False:", True and False)   # False
print("False or True:", False or True)     # True
print("False or False:", False or False)   # False
print("not True:", not True)                 # False
print("not False:", not False)               # True

# Tablas de verdad (para referencia)
print("\nTablas de verdad:")
print("AND:")
print("A     B     A and B")
print("True  True  ", True and True)
print("True  False ", True and False)
print("False True  ", False and True)
print("False False ", False and False)

print("\nOR:")
print("A     B     A or B")
print("True  True  ", True or True)
print("True  False ", True or False)
print("False True  ", False or True)
print("False False ", False or False)

print("\nNOT:")
print("A     not A")
print("True  ", not True)
print("False ", not False)

