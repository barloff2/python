import os

os.system('cls')


print('Ejercicio 1')


def devolver_distintos(*args):
    lista = list(args)
    suma = sum(args)

    if suma > 15:
        print('Mayor 15')
        return max(args)
    elif suma < 10:
        print('Menor 15')
        return min(args)
    else:
        print('entre')
        indice = int(len(args)/2)
        return args[indice]

print(devolver_distintos(1,1,4))


print('Ejercicio 2')


def devolver_palabra(palabra):
    lista = list(set(palabra))
    lista.sort()
    return lista

print(devolver_palabra('entretenido'))


print('Ejercicio 3')

def doble_cero(*args):
    for i in range(len(args)-1):
        if args[i] == 0 and args[i+1] == 0:
            return True
    return False

print(doble_cero(5,6,1,0,0,9,3,5))
print(doble_cero(6, 0, 5, 1, 0, 3, 0, 1))


print('Ejercicio 4')

def contar_primos(numero):
    primos = [2]
    iteracion = 3

    if numero < 2:
        return 0
    
    while iteracion <= numero:
        for n in range(3,iteracion,2):
            if iteracion % n == 0:
                iteracion +=2
                break
        else:
            primos.append(iteracion)
            iteracion += 2
    print(primos)
    return len(primos)

print(contar_primos(50))
