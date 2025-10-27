''' Comprimir y descomprimir archivos '''


import zipfile, os, shutil



# Comprimir archivos.
ruta = os.getcwd() + '\\udemy\\seccion_9\\'
"""
# Crear elemento para realizar el zip
mi_zip = zipfile.ZipFile(ruta + 'archivo_comprimido.zip', 'w')


mi_zip.write(ruta + 'mi_texto_A.txt')
mi_zip.write(ruta + 'mi_texto_B.txt')
mi_zip.close()"""

# Descomprimir archivos

"""zip_abierto = zipfile.ZipFile(ruta + 'archivo_comprimido.zip', 'r')


zip_abierto.extractall(ruta)
zip_abierto.close()"""


# Comprimir y Descomprimir con shutil

carpeta_origen = 'C:\\Users\\C82598B\\Music\\python\\udemy\\seccion_8'

archivo_destino = 'Todo_Comprimido'

shutil.make_archive(archivo_destino, 'zip', carpeta_origen)


shutil.unpack_archive(archivo_destino + '.zip', 'Extraccion_terminada', 'zip')
