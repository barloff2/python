###
# 03 - variables
# Sirven poara guardar datos en memoria
# Python es un lenguaje de tipoado dinámico y de tipado fuerte.
###

#Asignar una variable

my_name = "Stiven"

print(my_name)

age = 32
print(age)

age = 30
print(age)

#Tipado dinámico: el tipo de dato se determina en tiempo de ejecución, no se tiene que declarar explicitamente.
name = "Stiven"
print(type(name))

name = 32
print(type(name))

#Tipado fuerte: no realiza conversiones de tipo automaticas

#print(10 + "2")

#f-string (Literal de cadena de formato)
#desde la version 3.6.
print(f"hola {my_name}, tengo {age + 1} años")

# No recomendada forma de asignar variables
name, age, city = "stiven", 30, "Bogotá"

#Convenciones de nombres de variables
mi_nombre_de_variable = "ok" #snake_case
nombre = "ok"

MiNombreDeVariable = "ko" #PascalCase
minombredevariable = "ko" #todojunto

mi_nombre_de_variable_123 = "ok"

#Python no tiene constantes.
MI_CONSTANTE = 3.14 #UPPER_CASE -> constantes no se deberia cambiar.

# nombres no válidos de variables
# 123123 = "ko"
# mi-variable = "ko"
# mi variable = "ko"

#Es una anotación, no reserva el tipo de variable. se puede ajustar en typecheck para que revise, pero si se ejecuta va a seguir funcionado.
is_user_logged_in: bool = True
print(is_user_logged_in)

is_user_logged_in = 42
print(is_user_logged_in)

name: str = "Stiven"