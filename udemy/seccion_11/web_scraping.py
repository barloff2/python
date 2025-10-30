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

barra_lateral = sopa.select('.sidebar-container')
# print(barra_lateral)

'''Extraer imagenes'''

url = ('https://www.escueladirecta.com/l/products?sortKey=name&sortDirection=asc&page=1')

resultado2 = requests.get(url, verify=False)
sopa = bs4.BeautifulSoup(resultado2.text, 'lxml')

# Obtener con una clase con nombres separados.
imagenes = sopa.find_all("img", class_="ProductImage object-cover w-full aspect-video")[0]['src']

imagen_curso = requests.get(imagenes)

f = open('mi_imagen.jpg', 'wb')
f.write(imagen_curso.content)
f.close()
