import os

os.system('cls')

#metodos para diccionarios

#dic = {'clave1':100, 'clave2':200}
#
#dic.popitem() #elimina el ultimo elemento del diccionario
#print(dic)
#
#
#cadena = ',:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#'
#cadena.lstrip(",:%_#") #elimina los caracteres indicados al inicio de la cadena
#print(cadena)


print('____'*10)
print('Funciones')

def saludar_persona(nombre):
    #Esta función sirve para saludar a una persona
    print(f"Hola {nombre}")

saludar_persona('Stiven')

print("____"*10)
print("retorno de valores return")

def multiplicar(num1, num2):
    return num1 * num2

resultado = multiplicar(5, 8)
print(resultado)

print("____"*10)
print("funciones dinamicas")

#Return termina la función.

def chequear_3_cifras(lista_numeros):
    lista_3_cifras = []
    for numero in lista_numeros:
        if numero in range(100, 1000):
            lista_3_cifras.append(numero)
        else:
            pass
    return lista_3_cifras

resultado = chequear_3_cifras([12, 45, 6789, 100, 600])
print(resultado)


#Ejemplo para desempaquetado de tuplas

precios_cafe = [('capuchino', 1.50), ('moka', 1.9), ('expreso', 1.20)]

def cafe_mas_caro(lista_precios):
    precio_mayor = 0
    cafe_mas_caro = ''
    for cafe, precio in lista_precios:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_mas_caro = cafe
    return (cafe_mas_caro, precio_mayor)

print(cafe_mas_caro(precios_cafe))

cafe, precio = cafe_mas_caro(precios_cafe)
print(f'El café más caro es {cafe} y su precio es {precio}€')



print("____"*10)
print("*args y **kwargs")
#*args y **kwargs

#args permite enviar una cantidad variable de argumentos a una función (tupla), cualquier nombre despues del asterisco

'''def suma(*args):
    total = 0
    for arg in args:
        total += arg
    return total'''

def suma(*numeros):
    return sum(numeros)

print(suma(5, 8, 10, 20))

#kwargs permite enviar una cantidad variable de argumentos nombrados (diccionario), cualquier nombre despues de los dos asteriscos

def suma(**kwargs):
    total = 0
    for clave, valor in kwargs.items():
        print(f'{clave} = {valor}')
        total += valor
    return total

print(suma(a=5, b=8, c=10))


def suma2(num1, num2, *args, **kwargs):
    print(f'num1 = {num1}')
    print(f'num2 = {num2}')

    for arg in args:
        print(f'arg = {arg}')
    for clave, valor in kwargs.items():
        print(f'{clave} = {valor}')

args = (10, 20, 30, 40, 50)
kwargs = {'a':1, 'b':2, 'c':3, 'x':'Uno', 'y':'Dos', 'z':'Tres'}


suma2(15, 25, *args, **kwargs)

print(len(kwargs))