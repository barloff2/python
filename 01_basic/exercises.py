###
# exercises.py
# ejercicios para practicar los conceptos aprendidos en las lecciones
###

print("\nEjercicio 1: imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en lineas separadas.")

###código

print("Stiven\nParada")

print("______________________________________________")


print("Muestra los tipos de datos de las siguentes variables")

a = 15
b = 3.14159
c = "Hola Mundo"
d = True
e = None

##código

print(f"Variable a: {type(a)}, variable b {type(b)}, variable c {type(c)}, variable d {type(d)}, variable e {type(e)}")

print("--------------")

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

### Completa aquí

num = "12345"
print(int(num)) 
print(float(num)) # se agrega un decimal

num = 3.99
print(int(num)) # 

print("--------------")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

# "Hola! Me llamo midudev y tengo 39 años, mido 1.70 metros"

### Completa aquí

nombre, edad, altura = "Stiven", 30, 1.80

print(f"Hola! me llamo {nombre} y tengo {edad}, mido {altura}")

print("--------------")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

resultado = int(round(3.1416) / 2)
print("Valor de PI (aproximado):", 3.1416)
print("PI redondeado:", round(3.1416))
print("División entera de PI redondeado entre 2:", resultado)