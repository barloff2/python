import os, time
os.system('cls')
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, saldo_cuenta):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.saldo_cuenta = saldo_cuenta
    def __str__(self):
        return f"Nombre Completo: {self.nombre} {self.apellido} - Número Cuenta: {self.numero_cuenta} - Saldo Cuenta: {self.saldo_cuenta}"
    def depositar(self, valor):
        self.saldo_cuenta += valor
        print(f'Nuevo saldo {self.saldo_cuenta}')
        time.sleep(5)
    def retirar(self, valor):
        self.saldo_cuenta = self.saldo_cuenta - valor
        print(f'Nuevo saldo {self.saldo_cuenta}')
        time.sleep(5)


cliente = Cliente('Stiven', 'Parada', '00001', 2000)

opcion = 0

def borrar_pantalla():
    os.system('cls')

def ingreso_valor():
    valor = input('Ingresa el valor a retirar: ')
    if not valor.isnumeric() or int(valor) < 0:
        print('Ingrese un valor correcto')
        time.sleep(5)
        return -1
    return int(valor)

while opcion != 3:
    borrar_pantalla()
    print(cliente)
    opcion = input('Ingrese una opción:\n 1- Retirar \n 2- Depositar \n 3- Salir\n ')
    if not opcion.isnumeric() or int(opcion) < 0 or int(opcion) > 3:
        print('Ingresa una opción valida')
        continue
    opcion = int(opcion)
    if opcion == 1:
        if cliente.saldo_cuenta == 0:
            print('No puedes retirar tu saldo es 0')
            time.sleep(5)
            continue
        valor = ingreso_valor()
        if valor == -1:
            continue
        if valor > cliente.saldo_cuenta :
            print('Saldo insuficiente')
            time.sleep(5)
            continue
        cliente.retirar(valor)
    if opcion == 2:
        valor = ingreso_valor()
        if valor == -1:
            continue
        cliente.depositar(valor)

