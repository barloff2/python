import bs4
import requests
import urllib3
import os

os.system('cls')

# Desactivar ssl
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url_base = 'https://books.toscrape.com/catalogue/page-{}.html'

# agregar un espacio para una variable del contenido de un string
# for n in range(1, 11):
#    print(url_base.format(n))


# Llamar la página para seleccionar los libros con 5 estrellas y 
# mostrar su titulo
titulo_rating_alto = []
for pagina in range(1, 51):
    print(f'buscando en la página {pagina}')
    # Llamar la página
    response = requests.get(url_base.format(pagina), verify=False)
    sopa = bs4.BeautifulSoup(response.text, 'lxml')
    libros = sopa.select('.product_pod')
    for libro in libros:
        # Cuando hay un espacio vacio se reemplaza por un .
        # Validar si tiene 4 o más estrellas
        if libro.select('.star-rating.Five') or libro.select('.star-rating.Four'):
            titulo_rating_alto.append(libro.select('a')[1]['title'])

print(len(titulo_rating_alto))
