from tkinter import *
import datetime
import random

import pygame
from pygame import mixer

# Clases importantes para el videojuego:
# Clase "Jugador":
class Jugador:
    def __init__(self, nombre_jugador, vidas, sprite, posicion_x, posicion_y):
        
        self.nombre_jugador = nombre_jugador
        self.vidas = vidas
        self.sprite = sprite
        self.canvas = "" # Cargará la imagen en el escenario (sobre el canvas de la pantalla)
        self.posicion_x = posicion_x
        self.posicion_y = posicion_y

    # Métodos de la clase (movimiento, límites):
    # Movimiento horizontal:
    def movimiento_derecho(self, pixeles): # Los "pixeles" indican cuánto se moverá la nave sobre la pantalla

        if (self.posicion_x + pixeles < 1238): # Marca un límite, si el jugador se pasa del mismo, no se moverá más
            self.posicion_x = self.posicion_x + pixeles
            return pixeles
        else:
            return 0 # Si se pasó del límite, retornará 0, es decir, se moverá 0 pixeles.
    
    def movimiento_izquierdo(self, pixeles): 

        if (self.posicion_x - pixeles > 0):
            self.posicion_x = self.posicion_x - pixeles
            return pixeles
        else:
            return 0
    
    # Movimiento vertical:
    def movimiento_arriba(self, pixeles):

        if (self.posicion_y - pixeles > 0):
            self.posicion_y = self.posicion_y - pixeles
            return pixeles
        else:
            return 0
    
    def movimiento_abajo(self, pixeles):

        if (self.posicion_y + pixeles < 640):
            self.posicion_y = self.posicion_y + pixeles
            return pixeles
        else:
            return 0

# Clase "Asteroides":
class Asteroides:
    def __init__(self, sprite, posicion_x, posicion_y):

        self.fuerza = 1 # Valor predeterminado (siempre quitará una vida)
        self.vida = 1 # La vida de los asteroides siempre será uno
        self.sprite = sprite
        self.canvas = ""
        self.posicion_x = posicion_x
        self.posicion_y = posicion_y
        self.direccion_x = 1 # Es un valor temporal, cuando el asteroide llegue a un límite, el valor cambiará si signo, cambiando así la trayectoria horizontal
        self.direccion_y = 1

# Clases, "Nivel n":
# Clase nivel 1:
class Nivel1:
    def __init__(self, jugador, asteroide_1, asteroide_2, asteroide_3, tiempo_de_inicio):

        self.nivel = 1
        self.jugador = jugador
        self.asteroide_1 = asteroide_1
        self.asteroide_2 = asteroide_2
        self.asteroide_3 = asteroide_3
        self.tiempo_de_inicio = datetime.datetime.now()
        self.label_jugador = None
        self.label_tiempo = None

# Clase nivel 2:
class Nivel2:
    def __init__(self, jugador, asteroide_1, asteroide_2, asteroide_3, asteroide_4, tiempo_de_inicio):

        self.nivel = 2
        self.jugador = jugador
        self.asteroide_1 = asteroide_1
        self.asteroide_2 = asteroide_2
        self.asteroide_3 = asteroide_3
        self.asteroide_4 = asteroide_4
        self.tiempo_de_inicio = datetime.datetime.now()
        self.label_jugador = None
        self.label_tiempo = None

# Clase nivel 3:
class Nivel3:
    def __init__(self, jugador, asteroide_1, asteroide_2, asteroide_3, asteroide_4, asteroide_5, tiempo_de_inicio):

        self.nivel = 3
        self.jugador = jugador
        self.asteroide_1 = asteroide_1
        self.asteroide_2 = asteroide_2
        self.asteroide_3 = asteroide_3
        self.asteroide_4 = asteroide_4
        self.asteroide_5 = asteroide_5
        self.tiempo_de_inicio = datetime.datetime.now()
        self.label_jugador = None
        self.label_tiempo = None

# Funciones importantes (renderización, actualización, movimiento):
# Función de renderización:
def renderizacion(nivel, canvas_nivel, pantalla_nivel):

    # La siguiente condición renderizará ("dibujará") la nave del jugador en la pantalla del nivel en caso de que este proceso aún no se haya llevado a cabo.
    if nivel.jugador.canvas == "":
        nave_jugador_canvas = canvas_nivel.create_image(nivel.jugador.posicion_x, nivel.jugador.posicion_y, anchor = NW, image = nivel.jugador.sprite) # Se posicionará la nave en la posición que se haya especificado al crear el objeto.
        nivel.jugador.canvas = nave_jugador_canvas

        # Funciones que renderizarán el movimiento del jugador (cada vez que el jugador se mueva, lo dibujará en la posición exacta, dando ese efecto de movimiento)
        def movimiento_hacia_derecha(event):
            y = 0
            x = nivel.jugador.movimiento_derecho(10) # Note que la coordenada sobre la que ocurrirá el movimiento se llaman los métodos de movimiento definidos en la clase de jugador. Estos métodos cada vez que la nave se mueva irán evaluando que esta no llegue al límite establecido.
            canvas_nivel.move(nave_jugador_canvas, x, y)
        
        def movimiento_hacia_izquierda(event):
            y = 0
            x = nivel.jugador.movimiento_izquierdo(10) * -1 # Note que para el movimiento izquierdo, se cambia la dirección de la nave multiplicando un -1
            canvas_nivel.move(nave_jugador_canvas, x, y)
        
        def movimiento_hacia_arriba(event):
            x = 0
            y = nivel.jugador.movimiento_arriba(10) * -1 # Similar a la función anterior, se utiliza un -1 para que los pixeles no se sumen, sino que se resten para así permitir que la nave suba
            canvas_nivel.move(nave_jugador_canvas, x, y)
        
        def movimiento_hacia_abajo(event):
            x = 0
            y = nivel.jugador.movimiento_abajo(10)
            canvas_nivel.move(nave_jugador_canvas, x, y)

        # Asignación de teclas para el movimiento del jugador:
        pantalla_nivel.bind("<Right>", movimiento_hacia_derecha)
        pantalla_nivel.bind("<Left>", movimiento_hacia_izquierda)
        pantalla_nivel.bind("<Up>", movimiento_hacia_arriba)
        pantalla_nivel.bind("<Down>", movimiento_hacia_abajo)
        
        # Cargar y renderizar canvas de los asteroides:
        # Nivel 1:
        if nivel.nivel == 1:
            if nivel.asteroide_1.canvas == "" and nivel.asteroide_2.canvas == "" and nivel.asteroide_3.canvas == "":
                asteroide1 = canvas_nivel.create_image(nivel.asteroide_1.posicion_x, nivel.asteroide_1.posicion_y, anchor = NW, image = nivel.asteroide_1.sprite)
                nivel.asteroide_1.canvas = asteroide1

                asteroide2 = canvas_nivel.create_image(nivel.asteroide_2.posicion_x, nivel.asteroide_2.posicion_y, anchor = NW, image = nivel.asteroide_2.sprite)
                nivel.asteroide_2.canvas = asteroide2

                asteroide3 = canvas_nivel.create_image(nivel.asteroide_3.posicion_x, nivel.asteroide_3.posicion_y, anchor = NW, image = nivel.asteroide_3.sprite)
                nivel.asteroide_3.canvas = asteroide3
        
        # Renderización de las etiquetas que aparecerán en la pantalla de juego:
        if nivel.label_jugador == None and nivel.label_tiempo == None:
            # Etiqueta en la que se visualizará la vida y nombre del jugador:
            etiqueta_jugador = Label(canvas_nivel, text = "{}: {}".format(nivel.jugador.nombre_jugador, nivel.jugador.vidas), bg = "Black", fg = "White", font = ("Impact", 15))
            etiqueta_jugador.place(x = 20, y = 200)

            # Etiqueta en la que se visualizará el tiempo trasncurrido:
            etiqueta_tiempo = Label(canvas_nivel, text = "Tiempo transcurrido: {}".format(nivel.tiempo_de_inicio), bg = "Black", fg = "White", font = ("Impact", 15))
            etiqueta_tiempo.place(x = 20, y = 250)

            # Etiqueta en la que se visualizará el nivel
            etiqueta_nivel = Label(canvas_nivel, text = "Nivel: {}".format(nivel.nivel), bg = "Black", fg = "White", font = ("Impact", 15))
            etiqueta_nivel.place(x = 20, y = 300)

            # Agregar etiqueta de puntaje:

# Funciones del ciclo del juego: Prueba ----------------------------------------------------------------
# Movimiento asteroides:
def movimiento_asteroides(nivel, canvas_nivel, pantalla_nivel):
    if nivel.nivel == 1:
        # Asteroide 1:
        nivel.asteroide_1.posicion_x += (10 * nivel.asteroide_1.direccion_x)
        canvas_nivel.move(nivel.asteroide_1.canvas, 10 * nivel.asteroide_1.direccion_x, 0)

        if (nivel.asteroide_1.posicion_x >= 1238):
            golpe_sonido = mixer.Sound("golpe_asteroide.wav")
            golpe_sonido.play()
            nivel.asteroide_1.direccion_x = -1
            nivel.asteroide_1.direccion_y = random.randint(-1, 1)
        elif (nivel.asteroide_1.posicion_x <= 0):
            golpe_sonido = mixer.Sound("golpe_asteroide.wav")
            golpe_sonido.play()
            nivel.asteroide_1.direccion_x = 1
            nivel.asteroide_1.direccion_y = random.randint(-1, 1)

        nivel.asteroide_1.posicion_y += (10 * nivel.asteroide_1.direccion_y)
        canvas_nivel.move(nivel.asteroide_1.canvas, 0, 10 * nivel.asteroide_1.direccion_y)

        if (nivel.asteroide_1.posicion_y >= 640):
            golpe_sonido = mixer.Sound("golpe_asteroide.wav")
            golpe_sonido.play()
            nivel.asteroide_1.direccion_y = -1
            nivel.asteroide_1.direccion_x = random.randint(-1, 1)
        elif (nivel.asteroide_1.posicion_y <= 0):
            golpe_sonido = mixer.Sound("golpe_asteroide.wav")
            golpe_sonido.play()
            nivel.asteroide_1.direccion_y = 1
            nivel.asteroide_1.direccion_x = random.randint(-1, 1)

        # Asteroide 2:
        nivel.asteroide_2.posicion_x += (10 * nivel.asteroide_2.direccion_x)
        canvas_nivel.move(nivel.asteroide_2.canvas, 10 * nivel.asteroide_2.direccion_x, 0)

        if (nivel.asteroide_2.posicion_x >= 1238):
            golpe_sonido = mixer.Sound("golpe_asteroide.wav")
            golpe_sonido.play()
            nivel.asteroide_2.direccion_x = -1
            nivel.asteroide_2.direccion_y = random.randint(-1, 1)
        elif (nivel.asteroide_2.posicion_x <= 0):
            golpe_sonido = mixer.Sound("golpe_asteroide.wav")
            golpe_sonido.play()
            nivel.asteroide_2.direccion_x = 1
            nivel.asteroide_2.direccion_y = random.randint(-1, 1)

        nivel.asteroide_2.posicion_y += (10 * nivel.asteroide_2.direccion_y)
        canvas_nivel.move(nivel.asteroide_2.canvas, 0, 10 * nivel.asteroide_2.direccion_y)

        if (nivel.asteroide_2.posicion_y >= 640):
            golpe_sonido = mixer.Sound("golpe_asteroide.wav")
            golpe_sonido.play()
            nivel.asteroide_2.direccion_y = -1
            nivel.asteroide_2.direccion_x = random.randint(-1, 1)
        elif (nivel.asteroide_2.posicion_y <= 0):
            golpe_sonido = mixer.Sound("golpe_asteroide.wav")
            golpe_sonido.play()
            nivel.asteroide_2.direccion_y = 1
            nivel.asteroide_2.direccion_x = random.randint(-1, 1)

        # Asteroide 3:
        nivel.asteroide_3.posicion_x += (10 * nivel.asteroide_3.direccion_x)
        canvas_nivel.move(nivel.asteroide_3.canvas, 10 * nivel.asteroide_3.direccion_x, 0)

        if (nivel.asteroide_3.posicion_x >= 1238):
            golpe_sonido = mixer.Sound("golpe_asteroide.wav")
            golpe_sonido.play()
            nivel.asteroide_3.direccion_x = -1
            nivel.asteroide_3.direccion_y = random.randint(-1, 1)
        elif (nivel.asteroide_3.posicion_x <= 0):
            golpe_sonido = mixer.Sound("golpe_asteroide.wav")
            golpe_sonido.play()
            nivel.asteroide_3.direccion_x = 1
            nivel.asteroide_3.direccion_y = random.randint(-1, 1)

        nivel.asteroide_3.posicion_y += (10 * nivel.asteroide_3.direccion_y)
        canvas_nivel.move(nivel.asteroide_3.canvas, 0, 10 * nivel.asteroide_3.direccion_y)

        if (nivel.asteroide_3.posicion_y >= 640):
            golpe_sonido = mixer.Sound("golpe_asteroide.wav")
            golpe_sonido.play()
            nivel.asteroide_3.direccion_y = -1
            nivel.asteroide_3.direccion_x = random.randint(-1, 1)
        elif (nivel.asteroide_3.posicion_y <= 0):
            golpe_sonido = mixer.Sound("golpe_asteroide.wav")
            golpe_sonido.play()
            nivel.asteroide_3.direccion_y = 1
            nivel.asteroide_3.direccion_x = random.randint(-1, 1)
# Prueba -----------------------------------------------------------------------------

# Prueba, aún no sé si funcionará, ignorar por el momento ----------------------------------------------------------
# Función de detección de colisiones:
# Función de detección de colisiones, nivel 1:
def deteccion_colisiones_1(canvas_nivel, nave, obstaculo_1, obstaculo_2, obstaculo_3):
    # "Hitbox" de cada objeto (Bbox):
    nave_bbox = canvas_nivel.bbox(nave)

    obstaculo1_bbox = canvas_nivel.bbox(obstaculo_1)
    obstaculo2_bbox = canvas_nivel.bbox(obstaculo_2)
    obstaculo3_bbox = canvas_nivel.bbox(obstaculo_3)

    # Detección de la colisión:
    if nave_bbox[0] < obstaculo1_bbox[2] < nave_bbox[2] and nave_bbox[1] < obstaculo1_bbox[1] < nave_bbox[3] or nave_bbox[0] < obstaculo2_bbox[2] < nave_bbox[2] and nave_bbox[1] < obstaculo2_bbox[1] < nave_bbox[3] or nave_bbox[0] < obstaculo3_bbox[2] < nave_bbox[2] and nave_bbox[1] < obstaculo3_bbox[1] < nave_bbox[3]:
        return True
    elif nave_bbox[0] < obstaculo1_bbox[2] < nave_bbox[2] and nave_bbox[1] < obstaculo1_bbox[3] < nave_bbox[3] or nave_bbox[0] < obstaculo2_bbox[2] < nave_bbox[2] and nave_bbox[1] < obstaculo2_bbox[3] < nave_bbox[3] or nave_bbox[0] < obstaculo3_bbox[2] < nave_bbox[2] and nave_bbox[1] < obstaculo3_bbox[3] < nave_bbox[3]:
        return True
    elif nave_bbox[0] < obstaculo1_bbox[0] < nave_bbox[2] and nave_bbox[1] < obstaculo1_bbox[3] < nave_bbox[3] or nave_bbox[0] < obstaculo2_bbox[0] < nave_bbox[2] and nave_bbox[1] < obstaculo2_bbox[3] < nave_bbox[3] or nave_bbox[0] < obstaculo3_bbox[0] < nave_bbox[2] and nave_bbox[1] < obstaculo3_bbox[3] < nave_bbox[3]:
        return True
    elif nave_bbox[0] < obstaculo1_bbox[0] < nave_bbox[2] and nave_bbox[1] < obstaculo1_bbox[1] < nave_bbox[3] or nave_bbox[0] < obstaculo2_bbox[0] < nave_bbox[2] and nave_bbox[1] < obstaculo2_bbox[1] < nave_bbox[3] or nave_bbox[0] < obstaculo3_bbox[0] < nave_bbox[2] and nave_bbox[1] < obstaculo3_bbox[1] < nave_bbox[3]:
        return True
    else:
        return False

# Función de colisiones, nivel 2:
def deteccion_colisiones_2(canvas_nivel, nave, obstaculo_1, obstaculo_2, obstaculo_3, obstaculo_4):
    # "Hitbox" de cada objeto (Bbox):
    nave_bbox = canvas_nivel.bbox(nave)

    obstaculo1_bbox = canvas_nivel.bbox(obstaculo_1)
    obstaculo2_bbox = canvas_nivel.bbox(obstaculo_2)
    obstaculo3_bbox = canvas_nivel.bbox(obstaculo_3)
    obstaculo4_bbox = canvas_nivel.bbox(obstaculo_4)

    # Detección de la colisión:
    if nave_bbox[0] < obstaculo1_bbox[2] < nave_bbox[2] and nave_bbox[1] < obstaculo1_bbox[1] < nave_bbox[3] or nave_bbox[0] < obstaculo2_bbox[2] < nave_bbox[2] and nave_bbox[1] < obstaculo2_bbox[1] < nave_bbox[3] or nave_bbox[0] < obstaculo3_bbox[2] < nave_bbox[2] and nave_bbox[1] < obstaculo3_bbox[1] < nave_bbox[3] or nave_bbox[0] < obstaculo4_bbox[2] < nave_bbox[2] and nave_bbox[1] < obstaculo4_bbox[1] < nave_bbox[3]:
        return True
    elif nave_bbox[0] < obstaculo1_bbox[2] < nave_bbox[2] and nave_bbox[1] < obstaculo1_bbox[3] < nave_bbox[3] or nave_bbox[0] < obstaculo2_bbox[2] < nave_bbox[2] and nave_bbox[1] < obstaculo2_bbox[3] < nave_bbox[3] or nave_bbox[0] < obstaculo3_bbox[2] < nave_bbox[2] and nave_bbox[1] < obstaculo3_bbox[3] < nave_bbox[3] or nave_bbox[0] < obstaculo4_bbox[2] < nave_bbox[2] and nave_bbox[1] < obstaculo4_bbox[3] < nave_bbox[3]:
        return True
    elif nave_bbox[0] < obstaculo1_bbox[0] < nave_bbox[2] and nave_bbox[1] < obstaculo1_bbox[3] < nave_bbox[3] or nave_bbox[0] < obstaculo2_bbox[0] < nave_bbox[2] and nave_bbox[1] < obstaculo2_bbox[3] < nave_bbox[3] or nave_bbox[0] < obstaculo3_bbox[0] < nave_bbox[2] and nave_bbox[1] < obstaculo3_bbox[3] < nave_bbox[3] or nave_bbox[0] < obstaculo4_bbox[0] < nave_bbox[2] and nave_bbox[1] < obstaculo4_bbox[3] < nave_bbox[3]:
        return True
    elif nave_bbox[0] < obstaculo1_bbox[0] < nave_bbox[2] and nave_bbox[1] < obstaculo1_bbox[1] < nave_bbox[3] or nave_bbox[0] < obstaculo2_bbox[0] < nave_bbox[2] and nave_bbox[1] < obstaculo2_bbox[1] < nave_bbox[3] or nave_bbox[0] < obstaculo3_bbox[0] < nave_bbox[2] and nave_bbox[1] < obstaculo3_bbox[1] < nave_bbox[3] or nave_bbox[0] < obstaculo4_bbox[0] < nave_bbox[2] and nave_bbox[1] < obstaculo4_bbox[1] < nave_bbox[3]:
        return True
    else:
        return False

# Función de colisiones, nivel 3:
def deteccion_colisiones_3(canvas_nivel, nave, obstaculo_1, obstaculo_2, obstaculo_3, obstaculo_4, obstaculo_5):
    # "Hitbox" de cada objeto (Bbox):
    nave_bbox = canvas_nivel.bbox(nave)

    obstaculo1_bbox = canvas_nivel.bbox(obstaculo_1)
    obstaculo2_bbox = canvas_nivel.bbox(obstaculo_2)
    obstaculo3_bbox = canvas_nivel.bbox(obstaculo_3)
    obstaculo4_bbox = canvas_nivel.bbox(obstaculo_4)
    obstaculo5_bbox = canvas_nivel.bbox(obstaculo_5)

    # Detección de la colisión:
    if nave_bbox[0] < obstaculo1_bbox[2] < nave_bbox[2] and nave_bbox[1] < obstaculo1_bbox[1] < nave_bbox[3] or nave_bbox[0] < obstaculo2_bbox[2] < nave_bbox[2] and nave_bbox[1] < obstaculo2_bbox[1] < nave_bbox[3] or nave_bbox[0] < obstaculo3_bbox[2] < nave_bbox[2] and nave_bbox[1] < obstaculo3_bbox[1] < nave_bbox[3] or nave_bbox[0] < obstaculo4_bbox[2] < nave_bbox[2] and nave_bbox[1] < obstaculo4_bbox[1] < nave_bbox[3] or nave_bbox[0] < obstaculo5_bbox[2] < nave_bbox[2] and nave_bbox[1] < obstaculo5_bbox[1] < nave_bbox[3]:
        return True
    elif nave_bbox[0] < obstaculo1_bbox[2] < nave_bbox[2] and nave_bbox[1] < obstaculo1_bbox[3] < nave_bbox[3] or nave_bbox[0] < obstaculo2_bbox[2] < nave_bbox[2] and nave_bbox[1] < obstaculo2_bbox[3] < nave_bbox[3] or nave_bbox[0] < obstaculo3_bbox[2] < nave_bbox[2] and nave_bbox[1] < obstaculo3_bbox[3] < nave_bbox[3] or nave_bbox[0] < obstaculo4_bbox[2] < nave_bbox[2] and nave_bbox[1] < obstaculo4_bbox[3] < nave_bbox[3] or nave_bbox[0] < obstaculo5_bbox[2] < nave_bbox[2] and nave_bbox[1] < obstaculo5_bbox[3] < nave_bbox[3]:
        return True
    elif nave_bbox[0] < obstaculo1_bbox[0] < nave_bbox[2] and nave_bbox[1] < obstaculo1_bbox[3] < nave_bbox[3] or nave_bbox[0] < obstaculo2_bbox[0] < nave_bbox[2] and nave_bbox[1] < obstaculo2_bbox[3] < nave_bbox[3] or nave_bbox[0] < obstaculo3_bbox[0] < nave_bbox[2] and nave_bbox[1] < obstaculo3_bbox[3] < nave_bbox[3] or nave_bbox[0] < obstaculo4_bbox[0] < nave_bbox[2] and nave_bbox[1] < obstaculo4_bbox[3] < nave_bbox[3] or nave_bbox[0] < obstaculo5_bbox[0] < nave_bbox[2] and nave_bbox[1] < obstaculo5_bbox[3] < nave_bbox[3]:
        return True
    elif nave_bbox[0] < obstaculo1_bbox[0] < nave_bbox[2] and nave_bbox[1] < obstaculo1_bbox[1] < nave_bbox[3] or nave_bbox[0] < obstaculo2_bbox[0] < nave_bbox[2] and nave_bbox[1] < obstaculo2_bbox[1] < nave_bbox[3] or nave_bbox[0] < obstaculo3_bbox[0] < nave_bbox[2] and nave_bbox[1] < obstaculo3_bbox[1] < nave_bbox[3] or nave_bbox[0] < obstaculo4_bbox[0] < nave_bbox[2] and nave_bbox[1] < obstaculo4_bbox[1] < nave_bbox[3] or nave_bbox[0] < obstaculo5_bbox[0] < nave_bbox[2] and nave_bbox[1] < obstaculo5_bbox[1] < nave_bbox[3]:
        return True
    else:
        return False

# Función de colisiones, general:
def deteccion_colisiones_gen(nivel, canvas_nivel):

    if nivel.nivel == 1:
        return deteccion_colisiones_1(canvas_nivel, nivel.jugador, nivel.asteroide_1, nivel.asteroide_2, nivel.asteroide_3) # Se quitó parámetro nivel, evaluar si es útil.
    elif nivel.nivel == 2:
        return deteccion_colisiones_2(canvas_nivel, nivel.jugador, nivel.asteroide_1, nivel.asteroide_2, nivel.asteroide_3, nivel.asteroide_4)
    else:
        return deteccion_colisiones_3(canvas_nivel, nivel.jugador, nivel.asteroide_1, nivel.asteroide_2, nivel.asteroide_3, nivel.asteroide_4, nivel.asteroide_5)

# Función que quitará la vida de ser que hubo una colisión:
def asteroide_golpea_jugador(nivel, canvas_nivel):

    if deteccion_colisiones_gen(nivel, canvas_nivel) == True:
        nivel.jugador.vidas -= 1
# Prueba, aún no sé si funcionará, ignorar por el momento -----------------------------------------------

# Más pruebas: ----------------------------------------------------
# Función de actualización:
def actualizar_juego(nivel, canvas_nivel, pantalla_nivel):
    movimiento_asteroides(nivel, canvas_nivel, pantalla_nivel) # Hace falta agregar funciones, como la de colisión

# Función continua_juego (a esta haría falta agregarle la condición del tiempo, que sería la condición de victoria por supervivencia) y ciclo del juego:
def continua_juego(nivel):
    if nivel.jugador.vidas <= 0:
        return -1
    else:
        return 0

def ciclo_juego(nivel, canvas_nivel, pantalla_nivel): # Es probable que haga falta agregar una función, como de colisión.
    renderizacion(nivel, canvas_nivel, pantalla_nivel)
    actualizar_juego(nivel, canvas_nivel, pantalla_nivel)
    
    
    continuar = continua_juego(nivel)
    if continuar == 0:
        pantalla_nivel.after(100, ciclo_juego, nivel, canvas_nivel, pantalla_nivel) # Haría falta agregar las condiciones de victoria y de "game over"

# Prueba: ----------------------------------------------------

# Creamos la raíz sobre la que se desarrollará el videojuego. 
raiz_juego = Tk()

#Musica principal
pygame.init()
mixer.music.load("tema_principal.wav")
mixer.music.play(-1)

# Personalización de la raiz:
raiz_juego.title("Nombre del juego") 

raiz_juego.iconbitmap("Icono_proyecto2.ico")

raiz_juego.geometry("1366x768")

raiz_juego.config(cursor = "star")

# Canvas sobre el que se colocarán imágenes y demás widgets:
canvas_raiz = Canvas(raiz_juego, width = 1366, height = 768, bg = "Black") # Agregar fondo
canvas_raiz.pack()

# Labels de la raíz:
# Licencia:
Label(canvas_raiz, text = "©2021 TEC CR., LTD. All Rights Reserved.", bg = "Black", font = ("Impact", 15), fg = "White").place(x = 550, y = 650)

# Fondo de la raiz
bg_principal = PhotoImage(file ="bg_raiz.png")

# Fondo de la raiz
canvas_raiz.create_image(0, 0, anchor = NW, image = bg_principal)

# Fondos de los niveles
bg_nivel1 = PhotoImage(file ="bg_nivel1.png")

bg_nivel2 = PhotoImage(file ="bg_nivel2.png")

bg_nivel3 = PhotoImage(file ="bg_nivel3.png")

# Fondo puntajes
bg_puntajes = PhotoImage(file ="bg_raiz.png")

#Sprites
sprite_naveJugador = PhotoImage(file ="sprite_nave.png")

sprite_asteroides = PhotoImage(file ="sprite_asteroide.png")

# Botones de la raíz (Jugar y Cerrar):
# Funciones de los botones:
# Función del botón "Jugar"
def funcion_jugar():
    raiz_juego.deiconify()

    # Pantalla que se abre al tocar el botón "Jugar":
    pantalla_seleccion = Toplevel()
    pantalla_seleccion.geometry("1366x768")
    pantalla_seleccion.iconbitmap("Icono_proyecto2.ico")
    pantalla_seleccion.config(cursor = "star")

    # Canvas, pantalla de selección:
    canvas_seleccion = Canvas(pantalla_seleccion, width = 1366, height = 768, bg = "Black")
    canvas_seleccion.pack()

    # Fondo seleccion
    canvas_seleccion.create_image(0, 0, anchor=NW, image=bg_principal)

    # Funciones de los botones en pantalla de selección:
    # Función del botón "Atrás" de la pantalla de selección:
    def atras_seleccion():
        pantalla_seleccion.destroy()

    # Función del botón "About":
    def complementaria():
        pantalla_seleccion.deiconify()

        # Pantalla complementaria ("About"):
        pantalla_comp = Toplevel()
        pantalla_comp.geometry("1366x768")
        pantalla_comp.iconbitmap("Icono_proyecto2.ico")
        pantalla_comp.config(cursor = "star")

        # Canvas, pantalla complementaria:
        canvas_comp = Canvas(pantalla_comp, width = 1366, height = 768, bg = "Black")
        canvas_comp.pack()

        # Fondo complementaria
        canvas_comp.create_image(0, 0, anchor=NW, image=bg_principal)

        # Función del botón "Atras" de la pantalla complementaria:
        def atras_comp():
            pantalla_comp.destroy()

        # Función del botón "Ayuda" de la pantalla complementaria:
        def pantalla_ayuda():
            pantalla_comp.deiconify()

            # Pantalla "Ayuda":
            pantalla_de_ayuda = Toplevel()
            pantalla_de_ayuda.geometry("1366x768")
            pantalla_de_ayuda.iconbitmap("Icono_proyecto2.ico")
            pantalla_de_ayuda.config(cursor = "star")

            # Canvas pantalla "Ayuda":
            canvas_ayuda = Canvas(pantalla_de_ayuda, width = 1366, height = 768, bg = "Black")
            canvas_ayuda.pack()

            # Fondo ayuda
            canvas_ayuda.create_image(0, 0, anchor=NW, image=bg_principal)

            # Función del botón "Atrás" de la pantalla de ayuda:
            def atras_ayuda():
                pantalla_de_ayuda.destroy()
            
            # Botón "Atrás" de la pantalla de ayuda:
            Boton_atras_ayuda = Button(canvas_ayuda, text = "Atrás", padx = 10, pady = 5, font = "Impact", relief = "raised", bg = "Purple", command = atras_ayuda)
            Boton_atras_ayuda.place(x = 10, y = 655)

        # Botones de la pantalla complementaria:
        # Botón de la pantalla de ayuda:
        Boton_ayuda = Button(canvas_comp, text = "Ayuda", padx = 10, pady = 5, font = "Impact", relief = "raised", bg = "Purple", command = pantalla_ayuda)
        Boton_ayuda.place(x = 1288, y = 655)

        # Botón "Atrás" de la pantalla complementaria:
        Boton_atras_comp = Button(canvas_comp, text = "Atrás", padx = 10, pady = 5, font = "Impact", relief = "raised", bg = "Purple", command = atras_comp)
        Boton_atras_comp.place(x = 10, y = 655)
        
    # Función del botón "Puntajes"
    def mejores_puntajes():
        pantalla_seleccion.deiconify()

        # Pantalla de mejores puntajes:
        pantalla_puntajes = Toplevel()
        pantalla_puntajes.geometry("1366x768")
        pantalla_puntajes.iconbitmap("Icono_proyecto2.ico")
        pantalla_puntajes.config(cursor = "star")

        # Canvas, pantalla de mejores puntajes:
        canvas_puntajes = Canvas(pantalla_puntajes, width = 1366, height = 768, bg = "Black")
        canvas_puntajes.pack()

        # Fondo puntajes
        canvas_puntajes.create_image(0, 0, anchor=NW, image=bg_puntajes)

        # Función del botón "Atrás" de la pantalla de mejores puntajes:
        def atras_puntajes():
            pantalla_puntajes.destroy()
        
        # Botón "Atrás" de la pantalla de puntajes:
        Boton_atras_puntajes = Button(canvas_puntajes, text = "Atrás", padx = 10, pady = 5, font = "Impact", relief = "raised", bg = "Purple", command = atras_puntajes)
        Boton_atras_puntajes.place(x = 10, y = 655)
    
    # Función del botón "Niveles" (selección de niveles):
    def seleccion_niveles():
        pantalla_seleccion.deiconify()

        # Pantalla de selección de niveles:
        pantalla_niveles = Toplevel()
        pantalla_niveles.geometry("1366x768")
        pantalla_niveles.iconbitmap("Icono_proyecto2.ico")
        pantalla_niveles.config(cursor = "star")

        # Canvas, pantalla de mejores puntajes:
        canvas_niveles = Canvas(pantalla_niveles, width = 1366, height = 768, bg = "Black")
        canvas_niveles.pack()

        # Fondo niveles
        canvas_niveles.create_image(0, 0, anchor=NW, image=bg_principal)

        # Funciones de los botones de la pantalla de selección de niveles:
        # Botón "Atrás" de la pantalla de selección de niveles:
        def atras_niveles():
            pantalla_niveles.destroy()
        
        # Funciones de los botones "Nivel 1", "Nivel 2" y "Nivel 3":
        # Pantalla del primer nivel:
        def Nivel_1():
            # Personalización de la pantalla del primer nivel:
            pantalla_nivel_1 = Toplevel()
            pantalla_nivel_1.geometry("1366x768")
            pantalla_nivel_1.iconbitmap("Icono_proyecto2.ico")
            pantalla_nivel_1.config(cursor = "star")

            # Canvas del nivel 1 (sobre este se dibujarán los elementos que aparecerán en pantalla):
            canvas_nivel_1 = Canvas(pantalla_nivel_1, width = 1366, height = 768, bg = "Black")
            canvas_nivel_1.pack()

            # Escenario (fondo) del primer nivel:
            canvas_nivel_1.create_image(0, 0, anchor = NW, image = bg_nivel1)

            # Musica nivel
            mixer.music.stop()
            mixer.music.load("tema_nivel1.mp3")
            mixer.music.play(-1)

            # Parámetros para la creación de la partida/juego (Nivel 1):
            # Nombre jugador:
            nombre_de_jugador = nombre_jugador.get()
            
            # Prueba -------------------------------------------------------
            # Creación del jugador:
            jugador = Jugador(nombre_de_jugador, 3, sprite_naveJugador, 620, 585)

            # Creación asteroides:
            asteroide1 = Asteroides(sprite_asteroides, random.randint(0, 1238), -30)
            asteroide2 = Asteroides(sprite_asteroides, random.randint(0, 1238), -30)
            asteroide3 = Asteroides(sprite_asteroides, random.randint(0, 1238), -30)

            # Creación del nivel:
            primer_nivel = Nivel1(jugador, asteroide1, asteroide2, asteroide3, datetime.datetime.now())

            # Llamada para renderizar
            ciclo_juego(primer_nivel, canvas_nivel_1, pantalla_nivel_1)
            # Prueba ------------------------------------------------------------

            # Función del botón "Atrás" de la pantalla del nivel 1:
            def atras_nivel_1():
                pantalla_nivel_1.destroy()

                #Parar musica del nivel y repoducir tema principal
                mixer.music.stop()
                mixer.music.load("tema_principal.wav")
                mixer.music.play(-1)
            
            # Botón "Atrás" de la pantalla del nivel 1:
            atras_n1 = Button(canvas_nivel_1, text = "Atrás", padx = 10, pady = 5, font = "Impact", relief = "raised", bg = "Purple", command = atras_nivel_1)
            atras_n1.place(x = 10, y = 655)

        # Pantalla del segundo nivel:
        def Nivel_2():
            # Personalización de la pantalla del segundo nivel:
            pantalla_nivel_2 = Toplevel()
            pantalla_nivel_2.geometry("1366x768")
            pantalla_nivel_2.iconbitmap("Icono_proyecto2.ico")
            pantalla_nivel_2.config(cursor = "star")

            # Canvas del nivel 2 (sobre este se dibujarán los elementos que aparecerán en pantalla):
            canvas_nivel_2 = Canvas(pantalla_nivel_2, width = 1366, height = 768, bg = "Black")
            canvas_nivel_2.pack()

            # Escenario (fondo) del segundo nivel:
            canvas_nivel_2.create_image(0, 0, anchor = NW, image = bg_nivel2)

            # Parámetros para la creación de la partida/juego (Nivel 2):
            # Nombre jugador:
            # nombre_de_jugador = nombre_jugador.get()
            # print(nombre_de_jugador)

            # Función del botón "Atrás" de la pantalla del nivel 2:
            def atras_nivel_2():
                pantalla_nivel_2.destroy()

            # Botón "Atrás" de la pantalla del nivel 2:
            atras_n2 = Button(canvas_nivel_2, text = "Atrás", padx = 10, pady = 5, font = "Impact", relief = "raised", bg = "Purple", command = atras_nivel_2)
            atras_n2.place(x = 10, y = 655)

        # Pantalla del tercer nivel:
        def Nivel_3():
            # Personalización de la pantalla del tercer nivel:
            pantalla_nivel_3 = Toplevel()
            pantalla_nivel_3.geometry("1366x768")
            pantalla_nivel_3.iconbitmap("Icono_proyecto2.ico")
            pantalla_nivel_3.config(cursor = "star")

            # Canvas del nivel 3 (sobre este se dibujarán los elementos que aparecerán en pantalla):
            canvas_nivel_3 = Canvas(pantalla_nivel_3, width = 1366, height = 768, bg = "Black")
            canvas_nivel_3.pack()

            # Escenario (fondo) del tercer nivel:
            canvas_nivel_3.create_image(0, 0, anchor = NW, image = bg_nivel3)
    
            # Parámetros para la creación de la partida/juego (Nivel 1):
            # Nombre jugador:
            # nombre_de_jugador = nombre_jugador.get()
            # print(nombre_de_jugador)

            # Función del botón "Atrás" de la pantalla del nivel 3:
            def atras_nivel_3():
                pantalla_nivel_3.destroy()
            
            # Botón "Atrás" de la pantalla del nivel 1:
            atras_n3 = Button(canvas_nivel_3, text = "Atrás", padx = 10, pady = 5, font = "Impact", relief = "raised", bg = "Purple", command = atras_nivel_3)
            atras_n3.place(x = 10, y = 655)

        # Botones de la pantalla de selección de niveles:
        # Botón que dirige a la pantalla del primer nivel:
        Boton_nivel_1 = Button(canvas_niveles, text = "Nivel 1", padx = 10, pady = 5, font = "Impact", relief = "raised", bg = "Purple", command = Nivel_1)
        Boton_nivel_1.place(x = 550, y = 500)

        # Botón que dirige a la pantalla del segundo nivel:
        Boton_nivel_2 = Button(canvas_niveles, text = "Nivel 2", padx = 10, pady = 5, font = "Impact", relief = "raised", bg = "Purple", command = Nivel_2)
        Boton_nivel_2.place(x = 650, y = 500)

        # Botón que dirige a la pantalla del tercer nivel:
        Boton_nivel_3 = Button(canvas_niveles, text = "Nivel 3", padx = 10, pady = 5, font = "Impact", relief = "raised", bg = "Purple", command = Nivel_3)
        Boton_nivel_3.place(x = 750, y = 500)

        # Botón "Jugar" de la pantalla de selección (inicia el juego en el nivel 1):
        Boton_jugar_seleccion = Button(canvas_niveles, text = "Jugar", padx = 10, pady = 5, font = "Impact", relief = "raised", bg = "Purple", command = Nivel_1)
        Boton_jugar_seleccion.place(x = 1288, y = 655)

        # Botón "Atrás" de la pantalla de selección:
        Boton_atras_seleccion = Button(canvas_niveles, text = "Atrás", padx = 10, pady = 5, font = "Impact", relief = "raised", bg = "Purple", command = atras_niveles)
        Boton_atras_seleccion.place(x = 10, y = 655)

        # Entry para que el jugador introduzca su nombre:
        # Label (etiqueta) con el texto "Introduzca su nombre":
        Label(canvas_niveles, text = "Introduzca su nombre:", bg = "Black", fg = "White").place(x = 560, y = 600)
    
        # Entry sobre el que se digita el nombre:
        nombre_jugador = Entry(canvas_niveles, text = "Introduzca su nombre:", bg = "White")
        nombre_jugador.place(x = 690, y = 600) 

    # Botones de la pantalla de selección:
    # Botón de la pantalla complementaria:
    Boton_complemento = Button(canvas_seleccion, text = "About", padx = 10, pady = 5, font = "Impact", relief = "raised", bg = "Purple", command = complementaria)
    Boton_complemento.place(x = 550, y = 350)

    # Botón de la pantalla de mejores puntajes:
    Boton_puntajes = Button(canvas_seleccion, text = "Puntajes", padx = 10, pady = 5, font = "Impact", relief = "raised", bg = "Purple", command = mejores_puntajes)
    Boton_puntajes.place(x = 655, y = 350) 

    # Botón de la pantalla de selección de niveles:
    Boton_niveles = Button(canvas_seleccion, text = "Niveles", padx = 10, pady = 5, font = "Impact", relief = "raised", bg = "Purple", command = seleccion_niveles)
    Boton_niveles.place(x = 780, y = 350)

    # Botón para regresar a la pantalla de inicio:
    Boton_atras_seleccion = Button(canvas_seleccion, text = "Atrás", padx = 10, pady = 5, font = "Impact", relief = "raised", bg = "Purple", command = atras_seleccion)
    Boton_atras_seleccion.place(x = 10, y = 655)  
    
# Botón "Jugar" de la pantalla incial:
Boton_jugar = Button(canvas_raiz, text = "Jugar", padx = 10, pady = 5, font = "Impact", relief = "raised", bg = "Purple", command = funcion_jugar)
Boton_jugar.place(x = 550, y = 500)

# Función del botón "Salir" de la pantalla inicial:
def cerrar_juego():
    raiz_juego.destroy()

# Botón perteneciente a la función "cerrar_juego":

Boton_cerrar = Button(canvas_raiz, text = "Salir", padx = 10, pady = 5, font = "Impact", relief = "raised", bg = "Purple", command = cerrar_juego)
Boton_cerrar.place(x = 800, y = 500)

raiz_juego.mainloop()