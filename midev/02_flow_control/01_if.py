###
# 01 - sentencias condicionales (if, elif, else)
# Permite ejecutar bloques de código solo si se cumplen ciertas condiciones.
###

import os
os.system("cls")

print("\nSentencia simple condicional")
edad = 18
#No utiliza llaves para definir bloques de código, sino indentación.
if edad >= 18:
  print("Eres mayor de edad")
  print("felicidades!")

edad = 15

if edad >= 18:
  print("Eres mayor de edad")
  print("felicidades!")


print("\nSentencia condicional con else")

edad = 15
if edad >= 18:
  print("Eres mayor de edad")
else:
  print("Eres menor de edad")

print("\nSentencia condicional con elif")
nota = 9
if nota >= 9:
  print("Sobresaliente")
elif nota >= 7:
  print("Notable")
elif nota >= 5:
  print("Aprobado")
else:
  print("!No está calificado¡")

print("\nCondiciones multiples")

#Pueblo de Barcerlona
edad = 16
tiene_licencia = True

#JavScript
#&& -> and
#|| -> or

if edad >= 18 and tiene_licencia:
  print("Puedes conducir 🚙")
else:
  print("Policia te va a multar 🚔")


# Venezuela un pueblo de isla margarita
if edad >= 18 or tiene_licencia:
  print("Puedes conducir en la isla margarita🚙")
else:
  print("Paga policia y te deja conducir 🚔")

es_fin_de_semana = False
#JavaScript -> !
if not es_fin_de_semana:
  print("hay que trabajar")

print("\nAnidar condicionales")
edad = 20
tiene_dinero = True
if edad >= 18:
  if tiene_dinero:
    print("Puedes ir a la discoteca")
  else:
    print("Quedate en casa")
else:
  print("No puedes entrar a la discoteca")


#mas facil de leer

# if edad < 18:
#   print("No puedes entrar a la discoteca")
# elif tiene_dinero:
#   print("Puedes ir a la discoteca")
# else:
#   print("Quedate en casa")

numero = 5

if numero:
  print("El número no es cero")

numero = 0
if numero:
  print("Aquí no entrará nunca")

nombre = ""
if nombre:
  print("El nombre no está vacío")

numero = 5 #asignación
es_el_tres = numero == 3 # comparación
if es_el_tres:
  print("El número es tres")

print("\nCondiciones en una línea (operador ternario)")
#Es una forma concisa de escribir una sentencia if-else en una sola línea.
#[código si cumple la condición] if [condición] else [código si no cumple la condición]

edad = 17

mensaje = "Es Mayor de edad" if edad >= 18 else "Es Menor de edad"
print(mensaje)


###
# EJERCICIOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

# Ejercicio 1

num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

if num1 == num2:
  print("Los números son iguales")
elif num1 > num2:
  print("El número 1 es mayor a el número 2")
else:
  print("El número 2 es mayor al número 1")

#Ejercicio 2
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
operador = str(input("Introduce la operación a realizar +, -, *, /: "))

if operador == '/' and num2 == 0:
  print("No se puede dividir por 0")
elif operador == '+':
  print(f"El resultado de la operación es: {num1 + num2}")
elif operador == '-':
  print(f"El resultado de la operación es: {num1 - num2}")
elif operador == '*':
  print(f"El resultado de la operación es: {num1 * num2}")
else:
  print(f"El resultado de la operación es: {num1 / num2}")

#Ejercicio 3# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

year = float(input("Introduce un año: "))
div_4 = year % 4
div_400 = year % 400
div_100 = year % 100
if not div_4 or not div_400:
  print("Es bisiesto")
else:
  print("No es bisiesto")


# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

age = float(input("Introduce tu edad: "))

if age >= 65:
  print("Adulto Mayor")
elif age >= 18:
  print("Adulto")
elif age >= 13:
  print("Adolescente")
elif age >= 3:
  print("Niño")
else:
  print("Bebe")