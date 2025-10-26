import os

os.system('cls')

###
# Index() este metodo es para ver el indice de cada caracter.
###

nombre = "Valentina"
print(nombre[2])
print(nombre.index("l"))

#Busca desde el indice que se coloque y hasta el indice que se coloque en el tercer parametro. pero no es inclusivo. -1
print(nombre.index("a", 4))
#Si se busca una palabra, muestra donde comienza ese substring. y es sencible a mayusculas


#Otro metodo parecido es rindex, busca de derecha a izquierda. pero da el indice de izquierda a derecha.


# upper(), lower(), split(), join(), find(), replace().

a = "Aprender"
b = "Python"
c = "es"
d = "genial"
e = " ".join([a,b,c,d])
print(e)

#___________________________________________________________________________________________________________

#Inmutable los string

nombre = "Balentina"
#nombre[0] = "V"
print(nombre)

#Se puede multiplicar.

n1 = "Valen"
n2 = "tina"
print(n1 * 10)

#String con salto de lineas.

poema = """Mil pequeños peces blancos
comosi hirviera
el color del agua"""

print(poema)

#Buscar si existe una palabra en un string

print("agua" in poema)
print("agua" not in poema)

#Largo de un string

print(len(poema))




