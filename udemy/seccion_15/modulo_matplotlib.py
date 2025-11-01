'''Importar para utilizar matplotlib'''

from turtle import color
import matplotlib.pyplot as plt
import numpy as np

# Creamos un gráfico utilzando plt.plot()
plt.plot([])
#plt.show()

# Graficamos una lista de numeros
a = [1, 5, 3, 8, 7, 15]
plt.plot(a)
#plt.show()

# Creamos dos listas, x e y. Llenamos lista x de valores del 1 al 100

x = list(range(1, 101))

# Los valores de y van a equivaler al cuadrado del respectivo valor en x con el mismo indice
y = []
for numero in x:
    y.append(numero**2)

# Graficas ambas listas creadas
plt.plot(x, y)
#plt.show()

'''Hay otra manera de crear gráficos en Matplotlib, utilizando el método orientado a objetos'''

# Creamos un gráfico utilizando plt.subplots()
fig, ax = plt.subplots()
ax.plot(x, y)
#plt.show()

'''Veamos cómo seria un flujo de trabajo en Matplotlib'''

# Importar y preparar la librería
# import matplotlib.pyplot as plt

# Preparar los datos
x = list(range(1, 101))
y = [numero**2 for numero in x]

# Preparar el área del grafico (fig) y el gráfico en sí (ax) utilizando plt.subplots()
fig, ax = plt.subplots()

# Añadimos los datos al gráfico
ax.plot(x, y)
# Personalizamos el grafico añadiendo titulo al grafico y a los ejes x e y
ax.set_title("Gráfico de Ejemplo")
ax.set_xlabel("Eje X")
ax.set_ylabel("Eje Y")

# Guardamos nuestro gráfico empleando fig.savefig()
#fig.savefig("grafico_ejemplo.png")

'''Veamos un grafico de dispersión'''

# Creamos un nuevo set de datos utilizando la libería numpy
x_1 = np.linspace(1, 100, 20)
y_1 = x_1**2

# Creamos el gráfico de dispersión en x vs y
fig, ax = plt.subplots()
ax.scatter(x_1, y_1)

# Visualizamos ahora la función seno, utilizando np.sin(x)
fig, ax = plt.subplots()
x_2 = np.linspace(-10, 10, 100)
y_2 = np.sin(x_2)
ax.scatter(x_2, y_2)
#plt.show()

'''Veamos ahora otro tipo de gráfico, un gráfico de barras, que por lo general asocia resultados numericos a variables categoricas'''

# Creamos un diccionario con tres platos y su respectivo precio
# Las claves del diccionario seran los nombres de las comidas, y los valores asociados, su precio
comidas = {"Pizza": 350, "Burger": 400, "Pasta": 150}

# Creamos un gráfico de barras donde el eje x está formado por las claves del diccionario y el eje y por los valores
fig, ax = plt.subplots()
ax.bar(comidas.keys(), comidas.values())
# Añadimos los titulos correspondientes
ax.set_title("Precios de Comidas")
ax.set_xlabel("Comida")
ax.set_ylabel("Precio")

# Probemos a continuación con un gráfico de barras horizontales
fig, ax = plt.subplots()
ax.barh(list(comidas.keys()), list(comidas.values()))

ax.set_title("Precios de Comidas")
ax.set_xlabel("Precio")
ax.set_ylabel("Comida")
# plt.show()

'''Un gráfico semejante es un histograma. Podemos generar números aleatorios que siguen una distribución normal, con la funcion randn'''

# Creamos una distribución de 1000 valores aleatorios distribuidos normalmente
x = np.random.randn(1000)
# Creamos el histograma utilizando ax.hist()
fig, ax = plt.subplots()
ax.hist(x)
# plt.show()
plt.close('all')  # Cierra todas las figuras
'''Veamos ahora un caso mas complejo, trabajando subplots, o figuras que contienen varios graficos'''

# Creamos una figura con 4 subgraficos (2 por fila)
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, figsize=(10, 5))
'''Añadimos datos a cada uno de los gráficos (axes)'''
# Creamos la misma disposición de gráficos, con un tamaño de figura de 10x5
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, figsize=(10, 5))
# Para nuestro primer gráfico, tomamos el conjunto x_1, y_1 y generamos un grafico de lineas
ax1.plot(x_1, y_1)
# segundo grafico x_2, y_2, y generamos un grafico de dispersion
ax2.scatter(x_2, y_2)
# creamos un grafico con los precios de tres comidas en la esquina inferior izquierda
ax3.bar(comidas.keys(), comidas.values())
# el grafico de la esquina inferior derecha sera un histograma de valores aleatorios con distrubición normal
ax4.hist(np.random.randn(1000))
plt.close('all')
'''Matplotlib tiene un conjunto de varios estilos disponibles, podemos verificarlos de la siguente manera'''

# Verificamos estilos disponibles

print(plt.style.available)


# Cambiamos el estudilo predeterminado por "seaborn-whitegrid"

plt.style.use('seaborn-v0_8-whitegrid')

'''Habiendo cambiado el estilo, cambiaremos tambien los colores de las lineas, puntos y barras en cada uno de los graficos por códigos hexadecimales a nuestra preferencia'''

# Copiamos los valores de los gráficos anteriores
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, figsize=(10, 5))
ax1.plot(x_1, y_1, color="#1f77b4")
ax2.scatter(x_2, y_2, color="#ff7f0e")
ax3.bar(comidas.keys(), comidas.values(), color="#2ca02c")
ax4.hist(np.random.randn(1000), color="#d62728")
plt.show()
