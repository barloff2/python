import os

os.system('cls')
#Rangos range, funcion que permite establecer un rango de numeros sin necesidad de una lista o una varible.

for numero in range(5):
    print(numero)

#si quiero hasta un número coloco el otro parametro, si necesito por pasos agrego el tercero.

for numero in range(20, 31):
    print(numero)

for numero in range(20, 31, 3):
    print(numero)

#Crear una lista del 1 hasta el 100

lista = list(range(1,101))
print(lista)

#Enumerador para acceder a los indices:

lista = ['a', 'b', 'c']
indice = 0

for item in lista:
    print(indice, item)
    indice += 1

#Mejor manera: crea una variable para indice y para el item

for indice, item in enumerate(lista):
    print(indice, item)


#Convertir mi lista en un taple:

mi_taple = list(enumerate(lista))
print(mi_taple)



##############################
#Zip cruza dos listas y devuelve una lista de taples según la posicion de los elementos, 0:0, tambien pueden ser diccionarios.
#combina hasta el largo de la lista mas corta.

nombres = ['Ana', 'Hugo', 'Valeria']
edades = [65, 29, 42]
ciudades = ['Lima', 'Madrid', 'Bogotá']

combinados = list(zip(nombres,edades,ciudades))

for nombre,edad,ciudad in combinados:
    print(f"{nombre} tiene {edad} y vive en {ciudad}")



###########################################
#Min y Max sirven para detectar los valores mas altos y bajos en una colección o lista


menor = min(58,96,44,35)
mayor = max(58,96,44,35)
print(menor)

lista = [58,96,44,35]
print(f'El menor es: {min(lista)} y el mayor es {max(lista)}')


#Organización de strings 

nombres = ['stiven', 'pablo', 'valentina', 'aleria']

print(min(nombres))


#Ahora solo con string, busca primero mayusculas

nombre = 'Stiven'
print(min(nombre.lower()))

#diccionarios

dic = {'c1':45, 'c2':11}

#Llaves
print(min(dic))
#valores.
print(min(dic.values()))


print('_'*20)

#########
#Random números aleatorios e importar.

from random import randint, uniform, random, choice, shuffle


#Numero aleatorio entero

aleatorio = randint(1,50)

print(aleatorio)

#Numero aleatorio decimal

aleatorio = round(uniform(1,5),1)
print(aleatorio)

#Da un número decimal entre 0 y 1

aleatorio = random()
print(aleatorio)


#Choice, trabajar con elemento aleatorios

colores = ['azul', 'rojo', 'verde', 'amarillo']
aleatorio = choice(colores)
print(aleatorio)

#Mezclar la lista, solo modifica la lista no se puede utilizar string.

numeros = list(range(5,50,5))
shuffle(numeros)
print(numeros)


print('_'*333 + '\n Comprension de listas')

palabra = 'python'

lista = []
for letra in palabra:
    lista.append(letra)

print(lista)

#mas resumido. con la comprensión

lista2 = [letra for letra in palabra]
lista3 = [letra for letra in 'valentina']
print(lista2)
print(lista3)

#valores numericos, se puede modificar el número antes de añadirlo a la lista ej dividir el numero multiplicar etc.

lista1 = [n/2 for n in range(0,21,2)]
print(lista1)

#condición de la lista
#puede colocarse el if al final despues del rango y si es necesario el else entonces se coloca despues del n o de la variable
lista = [n if n * 2 > 10 else 'no' for n in range(0,21,2)]
print(lista)

## Ejemplo convertir los pies a metros
pies = [10,20,30,40,50]
metros = [round(n/3.281,3) for n in pies]
print(metros)


#Coincidencias de patrones estructurales
'''serie = 'N-02'
if serie == 'N-01':
    print('Samsung')
elif serie == 'N-02':
    print('Nokia')
elif serie == 'N-03':
    print('Iphone')
else:
    print('No existe el producto')'''

"""match serie:
    case "N-01":
        print('Samsung')
    case 'N-02':
        print('Nokia')
    case 'N-03':
        print('Iphone')
    case _:
        print('No existe el producto')"""

cliente = {
    'nombre' : 'Stiven', 
    'edad' : 30,
    'ocupacion' : 'DevOps'
}

pelicula = {
    'titulo' : 'matrix',
    'ficha_tecnica': {
        'protagonista' : 'Keanu Reeves',
        'director' : 'Lana y Lilly Wachowski'
    }
}

elementos = [cliente, pelicula, 'libro']

for e in elementos:
    match e:
        case {'nombre': nombre, 'edad':edad, 'ocupacion':ocupacion}:
            print("Es un cliente")
            print(nombre,edad,ocupacion)
        case {'titulo':titulo, 'ficha_tecnica':{'protagonista':protagonista, 'director':director}}:
            print('Es una pelicula')
            print(titulo, protagonista, director)
        case _:
            print("No se que es esto")
