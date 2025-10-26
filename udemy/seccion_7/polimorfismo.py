import os
os.system('cls')

#Polimorfismo, para ejecutar los metodos con el mismo nombre, pero que se encuentren en diferentes clases y que se ejecuten.

class Vaca:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + ' dice muuu')

class Oveja:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + ' dice beee')

vaca1 = Vaca('Lola')
oveja1 = Oveja('Nube')


#Pruebas de polimorfismo.


animales = [vaca1, oveja1]
for animal in animales:
    animal.hablar()

#______________________________________


def animal_habla(animal):
    animal.hablar()

animal_habla(vaca1)
animal_habla(oveja1)