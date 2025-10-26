import os

os.system('cls')

#Objetos de tipo diccionario: puede contener listas, diccionarios dentro de esos diccionarios

diccionario = {
    'c1' : 'valor1', 'c2' : 'valor2'
}
print(diccionario)
print(diccionario["c1"])


cliente = {
    'nombre': 'juan', 'apellido' : 'fuentes', 'peso' : 70, 'altura' : 1.81
}
consulta = cliente["apellido"]
print(consulta)

dic = {
    'c1' : 55, 'c2' : [10,20,30], 'c3' : cliente
}

print(dic["c2"][1])
print(dic["c3"]["altura"])

#Ejercicio

dic = {
    'c1' : ['a', 'b', 'c'],
    'c2' : ['d', 'e', 'f']
}

print(dic['c2'][1].upper())

#Adicionar al diccionario

dic2 = {
    1:'a', 2:'b'
}

print(dic2)

dic2[3] = 'c'
print(dic2)

#Sobreescribir un valor de una clave

dic2[2] = 'B'
print(dic2)

#traer todas las llaves, valores y todo lo que tiene el diccionario

print(dic2.keys())
print(dic2.values())
print(dic2.items())



#Tuples se escribe con parentesis, son inmutables. ocupan menos espacio de memoria, a prueba de daños, puede tener cualquier tipo de dato

mi_tuple = (1,2,(10,20),4)
print(type(mi_tuple))

#Indices

print(mi_tuple[-2])
print(mi_tuple[0])

print(mi_tuple[2][0])

#sobreescribir

mi_tuple = list(mi_tuple)

print(type(mi_tuple))

mi_tuple = tuple(mi_tuple)

print(type(mi_tuple))


#Asignar el contenido del tuple a variables. (Se puede hacer con la lista y con los tuples)

t = (1,2,3)

x,y,z = t

print(x,y,z)

#ver el tamaño

print(len(t))

#Contar cuantas veces esta un elemento en el tuple
print(t.count(2))
#buscar el indice del elemento buscado
print(t.index(3))