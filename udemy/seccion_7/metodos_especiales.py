#Metodos thunder o mágicos
#son los que tienen el siguente formato __nombre__
# __init__
# __mro__
# __bases__
import os
os.system('cls')

mi_lista = [1,1,1,1,1,1,1]

#saber cuantos numeros tiene mi lista
print(len(mi_lista))

class Objeto:
    pass

#mi_objeto = Objeto()
#print(len(mi_objeto))

os.system('cls')

class CD:
    def __init__(self, autor, titulo, canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones
    #Ajustar como se muestra mi metodo cuando lo imprimo. si no muestra un str por defecto
    def __str__(self):
        return f'Album: {self.titulo} de {self.autor}'
    #Ajustar el largo de mi CD, para que no arroje error
    def __len__(self):
        return self.canciones
    #Eliminar e informar, por defecto del no informa.
    def __del__(self):
        print('Se ha eliminado el CD')

mi_cd = CD('Pink Floyd', 'The Wall', 24)

##Visualizar como es mi album
print(mi_cd)

#Largo de mi CD
print(len(mi_cd))

#eliminar
del mi_cd


