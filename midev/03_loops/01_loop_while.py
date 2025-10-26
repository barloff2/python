###
# 01 - Bucles while
# Permiten ejecutar un bloque de código mientras una condición sea verdadera.
###

import os
os.system("cls")  # Limpia la consola (funciona en Windows)

print("Bluce while")
contador = 0

while contador <= 5:
  print(contador)
  contador += 1  # Incrementa el contador para evitar un bucle infinito

# Utilizando la palabra clave 'break' para salir de un bucle infinito

print("\nBucle while con break")
contador = 0
while True:
  contador += 1
  print(contador)
  if contador == 5:
    break # Sale del bucle

#continue, que lo que hace es saltar esa iteración en concreto y continua con el bucle
print("\nBucle while con continue")
contador = 0
while contador < 10:
  contador += 1
  if contador % 2 == 0:
    continue # Salta la iteración si el número es par
    #este código no se ejecuta si el número es par
    lalalalladkfjekf2i233
  print(contador)

##else, esta condición cuando se ejecuta?
#print("\nBucle while con else")
#contador = 0
#while contador < 5:
#  print(contador)
#  contador += 1
#else:
#  print("El bucle ha terminado")
#
## pedirle al usuario que ingrese un número que es positivo y si no lo es, seguir pidiéndolo
#numero = -1
#while numero < 0:
#  numero = int(input("Ingresa un número positivo:"))
#  if numero < 0:
#    print("El número debe ser positvo. Inténtalo de nuevo.")
#
#print(f"El número que has introducido es: {numero}")


# try except para manejar errores de entrada del usuario

numero = -1
while numero < 0:
  try: 
    numero = int(input("Ingresa un número positivo:"))
    if numero < 0:
      print("El número debe ser positvo. Inténtalo de nuevo.")
  except:
    print("Lo que intruces debes ser un número o si no peta.")
    
print(f"El número que has introducido es: {numero}")
