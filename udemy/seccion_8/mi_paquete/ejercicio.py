#importar un módulo que estuviera en un paquete
# para importar todo se le coloca *

from paquete_stiven import suma_y_resta
##importar subpaquete
from paquete_stiven.subpaquete import saludo

suma_y_resta.resta(15, 2)
suma_y_resta.suma(10, 7)

saludo.hola()