''' Modulo re para hacer busquedas sobre algun texto.
Construcciones de expresiones en general.'''


import re


texto = "Si necesitas ayuda llama al (608)-123-4567 las 24 horas al servicio de ayuda online."

palabra = 'ayuda' in texto

print(palabra)


## Ahora con RE

patron = 'ayuda'


busqueda = re.search(patron, texto)

# Devuelve un objeto match
# Devuelve None si no hay coincidencia
print(busqueda)


# devuelve el rango de la coincidencia
print(busqueda.span())

# Encontrar al final
print(busqueda.end())

# Encontrar mas de una
busqueda = re.findall(patron, texto)
print(busqueda)
# numero de elementos
print(len(busqueda))

# si quiero acceder a un elemento en particular
for hallazgo in re.finditer(patron, texto):
    print(hallazgo.span())


# Construir patrones especiales

texto = 'Llama al numero 608-123-4567 ya mismo'

patron = r'\d\d\d-\d\d\d-\d\d\d\d'

patron_mejorado = r'\d{3}-\d{3}-\d{4}'

patron_compilado = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
resultado = re.search(patron_compilado, texto)

print(resultado)

# group devuelve el texto (telefono de esta busqueda)
# se puede buscar por grupos. cuando se utiliza el compilado.
print(resultado.group(1))


''' Uso Practico para controlar condiciones'''

clave = input('Clave: ')
patron = r'\D{1}\w{7}'

chequear = re.search(patron, clave)

print(chequear)


'''Operadores especiales'''

texto = 'No atendemos los lunes por la tarde'

# Operadores logicos | -> o
buscar = re.search(r'lunes|martes', texto)

print(buscar)

# Comodin

buscar = re.search(r'demos', texto)
print(buscar)
# muestra la cantidad de letras que este despues del demos
buscar = re.search(r'...demos....', texto)

# acento circunflejo, verifica si un patron comienza al inicio del string

buscar = re.search(r'^\D', texto)
print(buscar)

# signo moneda para finalizar

buscar = re.search(r'\D\$', texto)
print(buscar)

# exclucion caracter con espacio vacio

buscar = re.findall(r'[^\s]+', texto)
print(buscar)

print(''.join(buscar))


def verificar_email(email):
    patron = r'.*\w+@\w+\.com'
    resultado = re.search(patron, email)
    print(resultado)
    if resultado:
        print("Ok")
    else:
        print("La dirección de email es incorrecta")


verificar_email('stiven.parada@hotmail.com.br')

