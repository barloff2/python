nombre = input('Ingresa tu nombre: ')
ventas = float(input('Ingresa las ventas del mes: '))
comision = round((ventas * 13) / 100, 2)

print(f"Hola {nombre}, tu comisión de este mes es: {comision} pesos, felicitaciones!")
