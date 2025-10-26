import os
os.system('cls')

#Herencia.
#Clase hija que hereda metodos y atributos.

class Animal:
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print('Este animal ha nacido')

class Pajaro(Animal):
    pass

#Comprobar herencia
print(Pajaro.__bases__)
print(Animal.__subclasses__())

#instancia de Pajaro, probar metodo heredado
piolin = Pajaro(2, 'amarilo')
piolin.nacer()
print(piolin.color)
