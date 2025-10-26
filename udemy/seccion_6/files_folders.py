mi_archivo = open('test.txt')

#print(mi_archivo.read())

##El archivo se lee y guarda un checkpoint para seguir imprimiendo, si se imprime todo el archivo y se quiere leer solo una linea no va a funcionar.
#rstrip() es para quitar el salto de linea final
"""una_linea = mi_archivo.readline()
print(una_linea.rstrip())

una_linea = mi_archivo.readline()
print(una_linea.rstrip())

una_linea = mi_archivo.readline()
print(una_linea.rstrip())
"""

#Iteraciones por cada linea del archivo

"""for line in mi_archivo:
    print(f"aqui dice: {line}")
"""

#Guardar las lineas en una lista con readlines, solo para archivos pequeños.

lineas = mi_archivo.readlines()

print(lineas)




















mi_archivo.close()