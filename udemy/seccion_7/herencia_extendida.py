import os
os.system('cls')

#Herencia extendida, puede heredad tambien de 2 clases y la herencia tambien. se puede heredad mas abajo aun.
#Metodos heredado
#Metodos modificados
#metodos nuevos

class Animal:
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print('Este animal ha nacido')
    
    def hablar(self):
        print("Este animal emite un sonido")

class Pajaro(Animal):

    #Metodo 1
    #def __init__(self, edad, color, altura_vuelo):
    #    self.edad = edad
    #    self.color = color
    #    self.altura_vuelo = altura_vuelo

    #Metodo 2

    def __init__(self, edad, color, altura_vuelo):
        super().__init__(edad, color)
        self.altura_vuelo = altura_vuelo

    #Metodo heredado y modificado
    def hablar(self):
        print('pio')

    #Metodo nuevo
    def volar(self, metros):
        print(f'El pajaro vuela {metros} metros')


piolin = Pajaro(2, 'amarilo', 60)
mi_animal = Animal(5, 'negro')

##Metodos
#Metodo heredado
piolin.nacer()

#Metodo Heredado y modificado
piolin.hablar()

#Metodo nuevo
piolin.volar(4)

##Atributos propios de la clase Pajaro
#creando el metodo __init__



##### Herencia multiple
os.system('cls')

class Padre:
    def hablar(self):
        print('Hola')

class Madre:
    def reir(self):
        print('ja ja')
    
    def hablar(self):
        print('Que tal')

#La herencia depende del orden que se coloque las clases
#Si esta primero Padre, la prioridad de los metodos la tendra esta.
class Hijo(Padre, Madre):
    pass

class Nieto(Hijo):
    pass


#Pruebas herencia extendida y multiple.
#Herencia de parte del Padre
mi_nieto = Nieto()
mi_nieto.hablar()

#Herencia de parte de la Madre
mi_nieto.reir()

#Orden de herencia de los metodos
print(Nieto.__mro__) #<class '__main__.Nieto'>, <class '__main__.Hijo'>, <class '__main__.Padre'>, <class '__main__.Madre'>, <class 'object'>)