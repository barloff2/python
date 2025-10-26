import os 
from random import choice
os.system('cls')

palabras = ['familia', 'escuela', 'trabajo', 'tiempo', 'amistad', 'comida', 'salud', 'dinero', 'viajes', 'película', 'musica', 'internet', 'telefono', 'equipo', 'jardín', 'ciudad', 'mañana', 'historia', 'ciencia', 'artes']
palabra = list(choice(palabras))

oculto = list('_' * len(palabra))

print(oculto)

print(''.join(palabra))

