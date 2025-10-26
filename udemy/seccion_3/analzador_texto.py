texto = input('Ingresa un texto: ')
letra_1 = input('Ingresa un primer caracter: ').lower()
letra_2 = input('Ingresa un segundo caracter: ').lower()
letra_3 = input('Ingresa un tercer caracter: ').lower()

#Primero
print(f"La cantidad de veces que aparece la letra {letra_1} es: {texto.lower().count(letra_1)}")
print(f"La cantidad de veces que aparece la letra {letra_2} es: {texto.lower().count(letra_2)}")
print(f"La cantidad de veces que aparece la letra {letra_3} es: {texto.lower().count(letra_3)}")

#Segundo
catidad_palabras = len(texto.split(" "))
print(f"La cantidad de palabras del texto son: {catidad_palabras}")

#Tercero
print(f"La primera letra del texto es: {texto[0]} y la ultima es: {texto[-1]}")

#Cuarto
print(f"texto invertido \n {texto[::-1]} \n")

#Quinto
respuestas = {
    False : 'no se encuentra en el texto',
    True : 'se encuentra en el texto'
}
print(f"La palabra 'Python' {respuestas[("Python" in texto)]}")