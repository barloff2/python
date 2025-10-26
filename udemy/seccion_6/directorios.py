##trabajo de directorios.
# siempre trabaja en la misma ruta donde esta corriendo el programa.
# para acceder puede ser tambien con toda la ruta de acceso.

import os
os.system('cls')

#Ruta actual donde se esta trabajando.
ruta = os.getcwd()

#Cambiar de directorio
ruta = os.chdir('C:\\Users\\Stiven\\Documents\\python\\python\\udemy\\prueba') 
archivo = open('archivo.txt')

print(archivo.read())


#crear carpetas
new_dir = os.makedirs('C:\\Users\\Stiven\\Documents\\python\\python\\udemy\\prueba\\otra')

#Obtener el path y el nombre de una ruta.

ruta = 'C:\\Users\\Stiven\\Documents\\python\\python\\udemy\\seccion_6\\test1.txt'

elemento = os.path.basename(ruta)
directorio = os.path.dirname(ruta)

#obtener una tupla para obtener los dos
rutas = os.path.split(ruta)

print(f"Elemento: {elemento}, directorio: {directorio}, rutas {rutas}")

#eliminar una carpeta
os.rmdir('C:\\Users\\Stiven\\Documents\\python\\python\\udemy\\prueba\\otra')


##Abrir un archivo en otra carpeta
otro_archivo = open('C:\\Users\\Stiven\\Documents\\python\\python\\udemy\\prueba\\archivo.txt')
print(otro_archivo.read())


#Ahora con path vamos a abrir el archivo.

#Sirve para crear o mover archivos, enumerar archivos y crear rutas basadas en strings

from pathlib import Path, PureWindowsPath


#Se puede tambien todo en la misma liena de código.
carpeta = Path('/Users/Stiven/Documents/python/python/udemy/prueba')
#Se puede concatenar el archivo coin / y agrega uno de esos al final
archivo = carpeta / 'archivo.txt'

mi_archivo = open(archivo)

print(mi_archivo.read())



os.system('cls')

carpeta = Path('/Users/Stiven/Documents/python/python/udemy/prueba/archivo.txt')


#Validar si un archivo existe
if not carpeta.exists():
    print("Este archivo no existe")
else:
    print("Genial, existe")

#Leer texto del archivo, no es necesario cerrar ni abrir el archivo.
print(carpeta.read_text())

# devuelve el nombre del archivo del objeto path.
print(carpeta.name)

#devuelve la terminación del archivo
print(carpeta.suffix)

#devuelve el nombre sin la terminación
print(carpeta.stem)

#Transformar cualquier ruta a la ruta de windows, para que se adapte al formato de windows

ruta_windows = PureWindowsPath(carpeta)
print(ruta_windows)


os.system('cls')
print('Mas metodos path')

# se puede utiulizar la variable home del usuario principal.
base = Path.home()
print(base)

#Construye archivos por medio de strings, esto es una ruta relativa.
guia = Path('Barcelona', 'Sagrada_Familia.txt')
print(guia)

#construir una ruta añadiendo la base

guia = Path(base, "Barcelona", 'Sagrada_Familia.txt')
print(base)

#Admite cualquier tipo de objeto como parametro incluso objetos path
guia = Path(base, 'Europa', 'España', Path("Barcelona", 'Sagrada_Familia.txt'))
print(guia)

#Cambiar el nombre del archivo al final de la ruta, cabiando el archivo de destino

guia2 = guia.with_name('La_Pedrera.txt')
print(guia2)

#Acceder a directorios que estan en el medio de la ruta
#devuelve la ruta de la carpeta que contiene el archivo, esto se puede llamar varias veces para recorrer el arbol de carpetas

print(guia.parent) #barcelona
print(guia.parent.parent) #españa
print(guia.parent.parent.parent) #europa

#Enumerar archivos dentro de un arbol de carpetas

#Es un iterable
guia = Path(Path.home(),"Europa")

#Glob es para buscar lso archivos que cumplan
#los ** es para que busque en todas las carpetas
for txt in Path(guia).glob('**/*.txt'):
    print(txt)


#Calcular rutas relacionadas entre si, para recuperar un porción de una ruta larga. ver contenido en rutas especificas.

guia = Path("Europa", 'España', 'Barcelona', 'Sagrada_Familia.txt')

en_europa = guia.relative_to(Path('Europa'))
en_espania = guia.relative_to(Path('Europa', 'España'))

print(en_europa)
print(en_espania)



os.system('cls')
print('Funciones y archivos')

