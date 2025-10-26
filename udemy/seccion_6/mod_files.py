import os 

os.system('cls')

##Modos de aperturas metodo open
#r = solo lectura
#w = solo escritura (se vacia si existe o se crea si no existe)
#a = escritura al final del archivo (no se vacia si existe pero lo crea si no existe)

#archivo = open('test.txt','r')

#Se debe agregar los componentes de salto de linea y demas o utilizando ''' o """
archivo = open('test1.txt', 'w')
archivo.write('hola\n')
archivo.write('mundo')

archivo.write('''
pendejas
mamadas
''')

#escribe esa lista de string concatenandola. pero no agrega ningun espacio
#archivo.writelines(['hola', 'mundo', 'aqui', 'estoy'])

lista = ['hola', 'mundo', 'aqui', 'estoy']

for p in lista:
    archivo.writelines(p + '\n')


archivo.close()

#abrir archivo al final y escribir al final
archivo = open('test1.txt', 'a')

archivo.write('Bienvenido')

archivo.close()