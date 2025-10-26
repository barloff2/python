###
# 05 - Entrada de usuairo (input()) - version simplificada 
# La función input() permite obtener datos del usuario a través de la consola.
###

print("Hola, ¿Cómo te llamas?")
nombre = input()
print(f"Hola {nombre}, encantado de conocerte")


age = input("¿Cuantos años tienes\n")
print(f"Dentro de 20 años tendrás {int(age) + 20}")


print("Obtener multiples valores a la vez")
country, city = input("En que pais y ciudad vives\n").split() #Split por defecto lo hace con un espacio.
print(f"Vives en {country}, {city}")