import pygame
import random
import math
from pygame import mixer

''' Juego de pygame'''

# Inicializar a Pygame
pygame.init()

# Tamaño de pantalla Muestra pantalla
pantalla = pygame.display.set_mode((800, 600))

# Titulo e Icono

pygame.display.set_caption("Invasión Espacial")
icono = pygame.image.load("C:\\Users\\C82598B\\Music\\python\\udemy\\"
                          "seccion_10\\astronave.png")
pygame.display.set_icon(icono)

# Musica

mixer.music.load("C:\\Users\\C82598B\\Music\\python\\udemy\\seccion_10\\"
                 "MusicaFondo.mp3")
mixer.music.set_volume(0.3)
mixer.music.play(-1)

# Fondo

fondo = pygame.image.load("C:\\Users\\C82598B\\Music\\python\\udemy\\"
                          "seccion_10\\Fondo.jpg")

# Bala
img_bala = pygame.image.load("C:\\Users\\C82598B\\Music\\python\\udemy\\"
                             "seccion_10\\bala.png")

# Variables del jugador
jugador_x = 368
jugador_y = 500
jugador_x_cambio = 0

# Jugador
img_jugador = pygame.image.load("C:\\Users\\C82598B\\Music\\python\\udemy\\"
                                "seccion_10\\cohete.png")

# Variables de la bala
bala_x = 0
bala_y = 500
bala_x_cambio = 0
bala_y_cambio = 0.6
bala_visible = False

# texto final de juego
fuente_final = pygame.font.Font('freesansbold.ttf', 64)

# Variable puntaje
puntaje = 0
fuente = pygame.font.Font('freesansbold.ttf', 32)
texto_x = 10
texto_y = 10

# Enemigos
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 5

# Cargar enemigos
for enemigo in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load("C:\\Users\\C82598B\\Music\\python\\"
                                         "udemy\\seccion_10\\enemigo.png"))
    enemigo_x.append(random.randint(0, 736))
    enemigo_y.append(random.randint(50, 200))
    enemigo_x_cambio.append(0.5)
    enemigo_y_cambio.append(50)


# Función Jugador
def jugador(x, y):
    '''Situar jugador en la pantalla'''
    pantalla.blit(img_jugador, (x, y))


# Función Enemigo
def enemigo(x, y, ene):
    '''Situar enemigo en la pantalla'''
    pantalla.blit(img_enemigo[ene], (x, y))


# Disparar bala
def disparar_bala(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x + 16, y + 10))


# Detectar colisiones
def hay_colision(x_1, y_1, x_2, y_2):
    distancia = math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_1 - y_2, 2))
    return distancia < 27


# Funcion mostrar puntaje
def mostrar_puntaje(x, y):
    texto = fuente.render("Puntaje: " + str(puntaje), True, (255, 255, 255))
    pantalla.blit(texto, (x, y))


# game over función
def texto_final():
    mi_fuente_final = fuente_final.render('JUEGO TERMINADO',
                                          True, (255, 255, 255))
    pantalla.blit(mi_fuente_final, (75, 200))


# Loop para esperar eventos de la pantalla en pygame
se_ejecuta = True
while se_ejecuta:
    # Fondo de pantalla con imagen
    pantalla.blit(fondo, (0, 0))
    # Iterar eventos
    for evento in pygame.event.get():
        # Para salir del juego
        if evento.type == pygame.QUIT:
            se_ejecuta = False
        # Movimiento del jugador presionar flechas
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -0.3
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0.3
            if evento.key == pygame.K_SPACE and not bala_visible:
                mixer.Sound('C:\\Users\\C82598B\\Music\\python\\udemy\\'
                            'seccion_10\\disparo.mp3').play()
                bala_x = jugador_x
                disparar_bala(bala_x, bala_y)
        # keyup levantar flechas
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0
    # Actualizar la posición del jugador
    jugador_x += jugador_x_cambio
    # Mantener dentro de bordes
    if jugador_x <= 0:
        jugador_x = 0
    if jugador_x >= 736:
        jugador_x = 736

    # Actualizar la posición del enemigo
    for e in range(cantidad_enemigos):

        # fin del juego
        if enemigo_y[e] > 450:
            for k in range(cantidad_enemigos):
                enemigo_y[k] = 1000
            texto_final()
            break

        enemigo_x[e] += enemigo_x_cambio[e]

        # Mantener dentro de bordes
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = 0.2
            enemigo_y[e] += enemigo_y_cambio[e]
        if enemigo_x[e] >= 736:
            enemigo_x_cambio[e] = -0.2
            enemigo_y[e] += enemigo_y_cambio[e]
        # colision
        colision = hay_colision(enemigo_x[e], enemigo_y[e], bala_x, bala_y)
        if colision:
            mixer.Sound('C:\\Users\\C82598B\\Music\\python\\udemy\\'
                        'seccion_10\\Golpe.mp3').play()
            bala_y = 500
            bala_visible = False
            puntaje += 1
            enemigo_x[e] = random.randint(0, 736)
            enemigo_y[e] = random.randint(50, 200)
        # Actualizar enemigo
        enemigo(enemigo_x[e], enemigo_y[e], e)

    # Disparar mas balas
    if bala_y <= -64:
        bala_y = 500
        bala_visible = False
    # Movimiento bala
    if bala_visible:
        disparar_bala(bala_x, bala_y)
        bala_y -= bala_y_cambio
    # Pintar al jugador
    jugador(jugador_x, jugador_y)

    # Pintar puntaje
    mostrar_puntaje(texto_x, texto_y)
    # Actualizar pantalla
    pygame.display.update()
