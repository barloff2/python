from os import system
system("cls")


""" decoradores: como funcionan y para que sirven
    Un decorador es una función que recibe otra función como argumento
    y devuelve una nueva función que generalmente extiende el comportamiento
    de la función original sin modificar su código.
"""


def mayuscula(texto):
    print(texto.upper())


def minuscula(texto):
    print(texto.lower())


'''Todo en python es un objeto, incluidas las funciones.'''

mi_funcion = mayuscula
mi_funcion("Hola Mundo")  # Llama a mayuscula("Hola Mundo")


'''Las funciones pueden ser pasadas como argumentos a otras funciones.'''


def una_funcion(funcion):
    return funcion


una_funcion(mayuscula)("Probando")  # Llama a mayuscula("Probando")


'''definir funciones dentro de otras funciones'''


def cambiar_letras(tipo):
    def mayuscula(texto):
        return texto.upper()

    def minuscula(texto):
        return texto.lower()

    if tipo == "mayuscula":
        return mayuscula
    else:
        return minuscula


mi_funcion = cambiar_letras("mayuscula")
print(mi_funcion("Hola"))  # Llama a mayuscula("Hola")


'''Definir decoradores'''


def decorar_saludo(funcion):
    def envolver(palabra):
        print("Hola")
        funcion(palabra)
        print("Adiós")
    return envolver


"""@decorar_saludo
def mayusculas(texto):
    print(texto.upper())

@decorar_saludo
def minusculas(texto):
    print(texto.lower())"""


mayusculas_decorada = decorar_saludo(mayuscula)
mayusculas_decorada("Hola Mundo")
