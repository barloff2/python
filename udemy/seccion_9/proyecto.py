import time
import os
import re
import math
from datetime import date
from pathlib import Path

os.system('cls')

'''Descomprimir archivo'''

'''
carpeta_origen = 'C:\\Users\\C82598B\\Downloads'
archivo = 'Proyecto+Dia+9.zip'

carpeta_destino = 'C:\\Users\\C82598B\\Music\\python\\udemy\\seccion_9\\
    Extraccion_terminada'


shutil.unpack_archive(carpeta_origen + '\\' +
    archivo, carpeta_destino, 'zip')'''


inicio = time.time()
carpeta_origen = 'C:\\Users\\C82598B\\Music\\python\\udemy\\seccion_9\\' + \
                 'Extraccion_terminada\\Mi_Gran_Directorio'


def recorrer_carpetas(carpeta):
    lista_archivos = []
    for raiz, dirs, archivos in os.walk(carpeta):
        for archivo in archivos:
            lista_archivos.append(os.path.join(raiz, archivo))
    return lista_archivos


def procesar_archivos(lista_archivos):
    patron = r'N\D{3}-\d{5}'
    archivos_encontrados = {}
    for archivo in lista_archivos:
        file = Path(archivo)
        cnt = re.search(patron, file.read_text())
        if cnt:
            archivos_encontrados[file.name] = cnt.group()
    return archivos_encontrados


def mostrar_resultados(archivos_num_serie):
    print(f'Fecha de busqueda: {date.today().strftime("%d/%m/%Y")}')
    print('ARCHIVO\t\tNRO. DE SERIE')
    print('--------\t----------')
    for archivo, num_serie in archivos_num_serie.items():
        print(f'{archivo}\t{num_serie}')
    print(f'Números encontrados {len(archivos_num_serie)}')


lista_archivos = recorrer_carpetas(carpeta_origen)

archivos_num_serie = procesar_archivos(lista_archivos)
mostrar_resultados(archivos_num_serie)

fin = time.time()
tiempo = fin - inicio
print(f'Tiempo de busqueda: {math.ceil(tiempo)} segundos')
