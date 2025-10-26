import os 
from random import choice
os.system('cls')


palabras = ['familia', 'escuela', 'trabajo', 'tiempo', 'amistad', 'comida', 'salud', 'dinero', 'viajes', 'película', 'musica', 'internet', 'telefono', 'equipo', 'jardín', 'ciudad', 'mañana', 'historia', 'ciencia', 'artes']
palabra = list(choice(palabras))

print(palabra)
oculto = list('_' * len(palabra))
vidas = 6

while vidas > 0:
    print(" ".join(oculto))
    if oculto == palabra :
        print('Ganaste')
        break
    letra = input('Ingrese una letra: ')
    if len(letra) > 1 or letra.isnumeric():
        print('Siga las instrucciones, intente de nuevo.')
        continue
    indices = [indice for indice,let in enumerate(palabra) if letra == let]
    if len(indices) == 0:
        vidas -= 1
        print(f"La letra {letra} no esta, te quedan {vidas} vidas.")
        if vidas == 0:
            print('Perdiste')
            break
        continue
    for i in indices:
        oculto[i] = letra

