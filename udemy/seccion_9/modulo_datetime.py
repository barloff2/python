# Manipulación de fechas y tiempos.

import datetime
import os
os.system('cls')

# Hora, tiempo en 24hrs no 12
mi_hora = datetime.time(22, 35)

print(type(mi_hora))
print(mi_hora)

# Imprimir minutos
print(mi_hora.min)
# Imprimir horas
print(mi_hora.hour)


# Fechas
#  Solo contiene fechas no horas
mi_dia = datetime.date(2025, 10, 16)
print(mi_dia)

# Mostrar año
print(mi_dia.year)

# Otro formato de fecha

print(mi_dia.ctime())

# mostrar la fecha actual

print(mi_dia.today())

####################################

# Iportar para manejar fecha y hora

from datetime import datetime

os.system('cls')

mi_fecha = datetime(2025, 5, 15, 22, 10, 15, 2500)

print(mi_fecha)

# Cambiar un dato

mi_fecha = mi_fecha.replace(month=11)

print(mi_fecha)


# Calcular tiempo entre fechas y horas

from datetime import date

#Manejo de días.

nacimiento = date(1995, 3, 5)
defuncion = date(2095, 6, 19)

vida = defuncion - nacimiento

print(vida)
# mostrar dias
print(vida.days)

# Ejemplo para manejo de horas

despierta = datetime(2022, 10, 5, 7, 30)
duerme = datetime(2022, 10, 5, 23, 45)

vigilia = duerme - despierta

# Ver en horas
print(vigilia)

# Ver en segundos
print(vigilia.seconds)

# Tiempo de vida stiven

nacimiento = date(1995, 6, 3)

vida = date.today() - nacimiento

print(vida)

datetime.today().minute