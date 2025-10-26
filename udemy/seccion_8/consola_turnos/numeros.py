'''Modulo para decoradores y generadores'''


def decorador(turnos):
    '''Envuelve la funcion de turnos entre dos mensajes'''
    print('Su turno es')
    print(next(turnos))
    print('Aguarde y será atentido\n')


def turno_farmacia():
    '''Generador de turnos para farmacia'''
    turno = 1
    while True:
        yield f'F-{turno}'
        turno += 1


def turno_perfumeria():
    '''Gnerador de turnos para perfumeria'''
    turno = 1
    while True:
        yield f'P-{turno}'
        turno += 1


def turno_cosmeticos():
    '''Gnerador de turnos para cosméticos'''
    turno = 1
    while True:
        yield f'C-{turno}'
        turno += 1
