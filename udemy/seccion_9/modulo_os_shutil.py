''' Repaso de os '''

import os

os.system('cls')

# Dirección donde se encuentra ahora mismo.
print(os.getcwd())


# Abrir archivo y crearlo

archivo = open('curso.txt', 'w')
archivo.write('Texto de prueba')
archivo.close()

# listar archivos
print(os.listdir())


##
''' Mover Archivos con shutil'''

import shutil

# shutil.move('curso.txt', os.getcwd() + '\\seccion_9')



## Eliminar archivos

# os.rmdir elimina carpeta vacia
# os.unlink elimina un archivo en una ruta.

# shutil.rmt eliminar todo lo que hay una ruta y todas sus carpetas interiores sin preguntar.

# Metodo para enviar a la papelera y no eleiminar permanentemente
# pip install send2trash

import send2trash

# send2trash.send2trash(os.getcwd() + '\\seccion_9\\curso.txt')

###########

# Recorrer todos los archivos y carpetas de una ruta
# se utiliza walk y devuelve un generador.

# print(os.walk(os.getcwd()))

# carpeta -> subcarpetas -> archivos en tuplas

os.system('cls')

for carpeta, subcarpetas, archivos in os.walk(os.getcwd()):
    ''' Valida que la carpeta no sea .venv '''
    if '.venv' in carpeta:
        continue
    print(f'En la carpeta: {carpeta}')
    print('Las subcarpetas son: ')
    for subcarpeta in subcarpetas:
        print(f'\t{subcarpeta}')
    print('Los archivos son:')
    for archivo in archivos:
        print(f'\t{archivo}')
    print('\n')
