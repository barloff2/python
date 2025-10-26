#Clases con atributos
import os
os.system('cls')


class Pajaro:
    #Atributos de clase
    alas = True

    #Constructor con atributos de instancia.
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

##No se puede crear la clase sin parametros
#mi_pajaro = Pajaro()

mi_pajaro = Pajaro('negro', 'Tucan')

#Llamar párametro
print(mi_pajaro.color)
print(f'Mi pajaro es un {mi_pajaro.especie} de color {mi_pajaro.color}')

#Atributos de clase, se puede consultar directamente desde la clase
print(Pajaro.alas)
#O con el objeto
print(mi_pajaro.alas)