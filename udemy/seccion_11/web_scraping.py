'''Leer el código html, css o javascript de una página y poder utilizarlo para
convertirlo en objetos de python

html -> Estructura y contenido
css -> Estilo y presentación
javascript -> Comportamiento y funcionalidad
'''

import bs4
import requests
import urllib3
import os

os.system('cls')

# Desactivar ssl
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
url = ('https://escueladirecta-blog.blogspot.com/2024/07/copia-o-'
       'referencia.html')

resultado = requests.get(url, verify=False)

# Tipo del resultado
print(type(resultado))

# Contenido del resultado
# print(resultado.text)

# Parsear el contenido de la página.
sopa = bs4.BeautifulSoup(resultado.text, 'lxml')
# print(sopa)

# Para seleccionar etiqueta para traer e imprimir devuelve una lista.
print(len(sopa.select('p')))

# Ver elemento suelto con etiqueta
# print(sopa.select('p')[0])
# ver con etiqueta
# print(sopa.select('p')[0].getText())

parrafo_especial = sopa.select('p')[3].getText()
# print(parrafo_especial)

'''Extraer una clase completa'''
