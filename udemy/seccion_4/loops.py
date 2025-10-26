dic = {'clave1':'a', 'clave2':'b', 'clave3':'b'}

#Recorrer las claves:

for elemento in dic:
    print(elemento)

#Recorrer los valores:

for elemento in dic.values():
    print(elemento)

#Recorrer cada par:

for elemento in dic.items():
    print(elemento)

#Recorrer con una variable para llave y valor

for key, value in dic.items():
    print(key, value)

numero = 50
print(numero)
while numero >= 0:
    print(numero)
    numero = numero - 1