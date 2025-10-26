#Metodos para una clase.
import os
os.system('cls')

#init tambien es un método pero se puede construir otros, se parecen mucho a las funciones.

class Pajaro:
    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    #Siempre va self en los metodos.
    #para llamar un párametro de la clase se debe llamar self.
    def piar(self):
        print(f"pío, mi color es {self.color}")
    #Siempre va self en elos metodos.
    def volar(self, metros):
        print(f'Voló {metros} metros')

piolin = Pajaro('Amarillo', 'Canario')

piolin.piar()
piolin.volar(50)

#Tipos de métodos.

#Decoradores
# - métodos de instancia
    # def mi metodo(self)
        # acceder y modifica atributos del objeto.
        #acceder a otros métodos.
        #modificar el estado de la clase.
# - métodos de clase @classmethod
    # @classmethod
    # def mi_metodo(cls):
    #   print("algo")
    # No estan asociados a la instancia, si no a la clase, se puede llamar sin necesidad de crear un objeto
    # No pueden llamar otros metodos de la instancia, pero si modificar atributos de la clase.
# - métodos estáticos @staticmethod
    # @staticmethod
    # def mi_metodo():
    #   print("algo")
    # No reciben self ni cls, entonces no pueden modificar ningun estado de la clase, ni la instancia, ni parametros, ni llamar metodos.
    # Peros si pueden recibir parametros

os.system('cls')

class Pajaro2:
    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    #Siempre va self en los metodos.
    #Metodos instancia
    #para llamar un párametro de la clase se debe llamar self.
    def piar(self):
        print(f"pío, mi color es {self.color}")
    #Siempre va self en elos metodos.
    def volar(self, metros):
        print(f'Voló {metros} metros')
        #llamar otros metodos.
        self.piar()
    def pintar_negro(self):
        self.color = 'negro'
        print(f'Ahora el pajaro es {self.color}')

    #Metodos de clase
    @classmethod
    def poner_huevos(cls, cantidad):
        print(f'Puso {cantidad} huevos')
        #No puede llamar parametros de instancia
        #print(f"es de color {self.color}")

        #Cambio atributos de clase
        cls.alas = False
        print(Pajaro.alas)
    
    #Metodo estatico
    @staticmethod
    def mirar():
        print("El pajaro mira")

piolin2 = Pajaro2('Amarillo', 'Canario')

piolin2.alas = False
print(piolin2.alas)

#Ejecución metodo de clase y se puede llamar sin instanciar.
#Los otros metodos si o si se debe crear una instancia.
Pajaro2.poner_huevos(3)

#Llamado metodos estaticos
Pajaro2.mirar()



