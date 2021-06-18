# Bibliotecas y módulos que se utilizarán:
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
            return 0 # Si se pasó del límite, retornará 0, es decir, la nave se moverá 0 pixeles.
    
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

        self.fuerza = 1 # La fuerza es un atributo que se podría ver como: "El asteroide quita" (1) o "el asteroide NO quita vida" (0)
        self.vida = 1 # La vida de los asteroides siempre será uno
        self.sprite = sprite
        self.canvas = ""
        self.posicion_x = posicion_x
        self.posicion_y = posicion_y
        self.direccion_x = 1 # Es un valor temporal, cuando el asteroide llegue a un límite, el valor cambiará si signo, cambiando así la trayectoria horizontal
        self.direccion_y = 1 # Es un valor temporal, cuando el asteroide llegue a un límite, el valor cambiará si signo, cambiando así la trayectoria vertical

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
        self.label_puntaje = None
        self.puntaje = 0 

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
        self.label_puntaje = None
        self.puntaje = 0

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
        self.label_puntaje = None
        self.puntaje = 0

# Funciones importantes (renderización, actualización, movimiento):
# Función para el tiempo. Será un cronómetro que mostrará el tiempo restante en la etiqueta de tiempo que aparece en la pantalla del nivel:
def cronometro(fecha_inicio):
    # Cada vez que se le haga una llamada a la función, se pedirá la fecha de ese momento.
    fecha_actual = datetime.datetime.now()

    # Se hará una diferencia entre la fecha actual y la fecha de inicio, siendo esta última la fecha en la que inició la partida.
    segundos = fecha_actual - fecha_inicio

    # A través de un método propio del módulo "Time", se retornará la diferencia entre ambas fechas en segundos.
    return segundos.seconds 
    
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

        # Asignación de teclas para el movimiento del jugador (eventos con los que las funciones anteriores son llamadas):
        pantalla_nivel.bind("<Right>", movimiento_hacia_derecha)
        pantalla_nivel.bind("<Left>", movimiento_hacia_izquierda)
        pantalla_nivel.bind("<Up>", movimiento_hacia_arriba)
        pantalla_nivel.bind("<Down>", movimiento_hacia_abajo)
        
        # Cargar y renderizar canvas de los asteroides en caso de que aún no se haya llevado este proceso a cabo:
        # Nivel 1:
        if nivel.nivel == 1:

            if nivel.asteroide_1.canvas == "" and nivel.asteroide_2.canvas == "" and nivel.asteroide_3.canvas == "":
                asteroide1 = canvas_nivel.create_image(nivel.asteroide_1.posicion_x, nivel.asteroide_1.posicion_y, anchor = NW, image = nivel.asteroide_1.sprite)
                nivel.asteroide_1.canvas = asteroide1

                asteroide2 = canvas_nivel.create_image(nivel.asteroide_2.posicion_x, nivel.asteroide_2.posicion_y, anchor = NW, image = nivel.asteroide_2.sprite)
                nivel.asteroide_2.canvas = asteroide2

                asteroide3 = canvas_nivel.create_image(nivel.asteroide_3.posicion_x, nivel.asteroide_3.posicion_y, anchor = NW, image = nivel.asteroide_3.sprite)
                nivel.asteroide_3.canvas = asteroide3

        # Nivel 2:
        if nivel.nivel == 2:

            if nivel.asteroide_1.canvas == "" and nivel.asteroide_2.canvas == "" and nivel.asteroide_3.canvas == "" and nivel.asteroide_4.canvas == "":
                asteroide1 = canvas_nivel.create_image(nivel.asteroide_1.posicion_x, nivel.asteroide_1.posicion_y, anchor = NW, image = nivel.asteroide_1.sprite)
                nivel.asteroide_1.canvas = asteroide1

                asteroide2 = canvas_nivel.create_image(nivel.asteroide_2.posicion_x, nivel.asteroide_2.posicion_y, anchor = NW, image = nivel.asteroide_2.sprite)
                nivel.asteroide_2.canvas = asteroide2

                asteroide3 = canvas_nivel.create_image(nivel.asteroide_3.posicion_x, nivel.asteroide_3.posicion_y, anchor = NW, image = nivel.asteroide_3.sprite)
                nivel.asteroide_3.canvas = asteroide3

                asteroide4 = canvas_nivel.create_image(nivel.asteroide_4.posicion_x, nivel.asteroide_4.posicion_y, anchor=NW, image=nivel.asteroide_4.sprite)
                nivel.asteroide_4.canvas = asteroide4

        # Nivel 3:
        if nivel.nivel == 3:

            if nivel.asteroide_1.canvas == "" and nivel.asteroide_2.canvas == "" and nivel.asteroide_3.canvas == "" and nivel.asteroide_4.canvas == "" and nivel.asteroide_5.canvas == "":
                asteroide1 = canvas_nivel.create_image(nivel.asteroide_1.posicion_x, nivel.asteroide_1.posicion_y, anchor = NW, image = nivel.asteroide_1.sprite)
                nivel.asteroide_1.canvas = asteroide1

                asteroide2 = canvas_nivel.create_image(nivel.asteroide_2.posicion_x, nivel.asteroide_2.posicion_y, anchor = NW, image = nivel.asteroide_2.sprite)
                nivel.asteroide_2.canvas = asteroide2

                asteroide3 = canvas_nivel.create_image(nivel.asteroide_3.posicion_x, nivel.asteroide_3.posicion_y, anchor = NW, image = nivel.asteroide_3.sprite)
                nivel.asteroide_3.canvas = asteroide3

                asteroide4 = canvas_nivel.create_image(nivel.asteroide_4.posicion_x, nivel.asteroide_4.posicion_y, anchor=NW, image=nivel.asteroide_4.sprite)
                nivel.asteroide_4.canvas = asteroide4

                asteroide5 = canvas_nivel.create_image(nivel.asteroide_5.posicion_x, nivel.asteroide_5.posicion_y, anchor=NW, image=nivel.asteroide_5.sprite)
                nivel.asteroide_5.canvas = asteroide5
        
        # Renderización de las etiquetas que aparecerán en la pantalla de juego:
        if nivel.label_jugador == None and nivel.label_tiempo == None:

            # Etiqueta en la que se visualizará la vida y nombre del jugador:
            etiqueta_jugador = Label(canvas_nivel, text = "{}: {}".format(nivel.jugador.nombre_jugador, nivel.jugador.vidas), bg = "Black", fg = "White", font = ("Impact", 15))
            etiqueta_jugador.place(x = 20, y = 200)
            nivel.label_jugador = etiqueta_jugador 

            # Etiqueta en la que se visualizará el tiempo trasncurrido:
            etiqueta_tiempo = Label(canvas_nivel, text = "Tiempo restante: {}".format(60 - cronometro(nivel.tiempo_de_inicio)), bg = "Black", fg = "White", font = ("Impact", 15))
            etiqueta_tiempo.place(x = 20, y = 250)
            nivel.label_tiempo = etiqueta_tiempo

            # Etiqueta en la que se visualizará el nivel
            etiqueta_nivel = Label(canvas_nivel, text = "Nivel: {}".format(nivel.nivel), bg = "Black", fg = "White", font = ("Impact", 15))
            etiqueta_nivel.place(x = 20, y = 300)


            # Agregar etiqueta de puntaje:
            etiqueta_puntuacion = Label(canvas_nivel, text = "Puntaje: {}".format(nivel.puntaje), bg = "Black", fg = "White", font = ("Impact", 15))
            etiqueta_puntuacion.place(x = 20, y = 350)
            nivel.label_puntaje = etiqueta_puntuacion

        # Note que siempre que se renderiza algo, ya sea un sprite o un label, este se carga en el atributo de la clase respectivo para que no vuelva a entrar en las condiciones de renderización.

# Función que actualiza labels:
# Función encargada de actualizar el puntaje que se lleva. Como este puntaje es equivalente al tiempo trasncurrido, entonces se le hace una llamada a la función "cronómetro".
def actualiza_puntaje(nivel):
    if nivel.nivel == 1:
        nivel.puntaje = cronometro(nivel.tiempo_de_inicio)

    if nivel.nivel == 2:
        nivel.puntaje = int(cronometro(nivel.tiempo_de_inicio)) * 3

    if nivel.nivel == 3:
        nivel.puntaje = int(cronometro(nivel.tiempo_de_inicio)) * 5

# Función encargada de actualizar, visualmente, la información de los labels:
def actualiza_labels(nivel):

    nivel.label_jugador["text"] = "{}: {}".format(nivel.jugador.nombre_jugador, nivel.jugador.vidas)

    # Esta resta se hace para que el tiempo vaya de 60 a 0 segundos y no de 0 a 60 segundos.
    tiempo = 60 - cronometro(nivel.tiempo_de_inicio)
    nivel.label_tiempo["text"] = "Tiempo restante: {}".format(tiempo)

    nivel.label_puntaje["text"] = "Puntaje: {}".format(nivel.puntaje)

# Movimiento asteroides:
def movimiento_asteroides(nivel, canvas_nivel, pantalla_nivel):

    if nivel.nivel == 1 or nivel.nivel == 2 or nivel.nivel == 3:
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

    # Asteroide 4:
    if nivel.nivel == 2 or nivel.nivel == 3:
        nivel.asteroide_4.posicion_x += (10 * nivel.asteroide_4.direccion_x)
        canvas_nivel.move(nivel.asteroide_4.canvas, 10 * nivel.asteroide_4.direccion_x, 0)

        if (nivel.asteroide_4.posicion_x >= 1238):
            golpe_sonido = mixer.Sound("golpe_asteroide.wav")
            golpe_sonido.play()
            nivel.asteroide_4.direccion_x = -1
            nivel.asteroide_4.direccion_y = random.randint(-1, 1)
        elif (nivel.asteroide_4.posicion_x <= 0):
            golpe_sonido = mixer.Sound("golpe_asteroide.wav")
            golpe_sonido.play()
            nivel.asteroide_4.direccion_x = 1
            nivel.asteroide_4.direccion_y = random.randint(-1, 1)

        nivel.asteroide_4.posicion_y += (10 * nivel.asteroide_4.direccion_y)
        canvas_nivel.move(nivel.asteroide_4.canvas, 0, 10 * nivel.asteroide_4.direccion_y)

        if (nivel.asteroide_4.posicion_y >= 640):
            golpe_sonido = mixer.Sound("golpe_asteroide.wav")
            golpe_sonido.play()
            nivel.asteroide_4.direccion_y = -1
            nivel.asteroide_4.direccion_x = random.randint(-1, 1)
        elif (nivel.asteroide_4.posicion_y <= 0):
            golpe_sonido = mixer.Sound("golpe_asteroide.wav")
            golpe_sonido.play()
            nivel.asteroide_4.direccion_y = 1
            nivel.asteroide_4.direccion_x = random.randint(-1, 1)


    # Asteroide 5:
    if nivel.nivel == 3:
        nivel.asteroide_5.posicion_x += (10 * nivel.asteroide_5.direccion_x)
        canvas_nivel.move(nivel.asteroide_5.canvas, 10 * nivel.asteroide_5.direccion_x, 0)

        if (nivel.asteroide_5.posicion_x >= 1238):
            golpe_sonido = mixer.Sound("golpe_asteroide.wav")
            golpe_sonido.play()
            nivel.asteroide_5.direccion_x = -1
            nivel.asteroide_5.direccion_y = random.randint(-1, 1)
        elif (nivel.asteroide_5.posicion_x <= 0):
            golpe_sonido = mixer.Sound("golpe_asteroide.wav")
            golpe_sonido.play()
            nivel.asteroide_5.direccion_x = 1
            nivel.asteroide_5.direccion_y = random.randint(-1, 1)

        nivel.asteroide_5.posicion_y += (10 * nivel.asteroide_5.direccion_y)
        canvas_nivel.move(nivel.asteroide_5.canvas, 0, 10 * nivel.asteroide_5.direccion_y)

        if (nivel.asteroide_5.posicion_y >= 640):
            golpe_sonido = mixer.Sound("golpe_asteroide.wav")
            golpe_sonido.play()
            nivel.asteroide_5.direccion_y = -1
            nivel.asteroide_5.direccion_x = random.randint(-1, 1)
        elif (nivel.asteroide_5.posicion_y <= 0):
            golpe_sonido = mixer.Sound("golpe_asteroide.wav")
            golpe_sonido.play()
            nivel.asteroide_5.direccion_y = 1
            nivel.asteroide_5.direccion_x = random.randint(-1, 1)

# Función de detección de colisiones que detectará, a través de las "bboxes" de los objetos, si hubo algún choque entre la nave y el asteroide enviado como argumento:
def detect_colisiones(jugador, asteroide):

    if jugador[0] < asteroide[2] < jugador[2] and jugador[1] < asteroide[1] < jugador[3]:
        colision_sonido = mixer.Sound("explosion_asteroide.wav")
        colision_sonido.play()
        return True

    elif jugador[0] < asteroide[2] < jugador[2] and jugador[1] < asteroide[3] < jugador[3]:
        colision_sonido = mixer.Sound("explosion_asteroide.wav")
        colision_sonido.play()
        return True

    elif jugador[0] < asteroide[0] < jugador[2] and jugador[1] < asteroide[3] < jugador[3]:
        colision_sonido = mixer.Sound("explosion_asteroide.wav")
        colision_sonido.play()
        return True

    elif jugador[0] < asteroide[0] < jugador[2] and jugador[1] < asteroide[1] < jugador[3]:
        colision_sonido = mixer.Sound("explosion_asteroide.wav")
        colision_sonido.play()
        return True
        
    else:
        return False

# Función de detección de colisiones para el nivel 1:
def deteccion_colisiones_1(canvas_nivel, nave, obstaculo_1, obstaculo_2, obstaculo_3):
    # "Hitbox" de cada objeto ("Bbox"):
    # "Bbox" de la nave:
    nave_bbox = canvas_nivel.bbox(nave.canvas)

    # "Bbox" de cada asteroide del nivel:
    obstaculo1_bbox = canvas_nivel.bbox(obstaculo_1.canvas)
    obstaculo2_bbox = canvas_nivel.bbox(obstaculo_2.canvas)
    obstaculo3_bbox = canvas_nivel.bbox(obstaculo_3.canvas)

    # Estas variables almacenarán los valores booleanos de colisión para cada asteroide (True: Hubo colisión, False: No hubo colisión):
    colision1 = detect_colisiones(nave_bbox, obstaculo1_bbox) # Función evalúa si hubo una colisión entre la nave y el asteroide 1
    colision2 = detect_colisiones(nave_bbox, obstaculo2_bbox) # Función evalúa si hubo una colisión entre la nave y el asteroide 2
    colision3 = detect_colisiones(nave_bbox, obstaculo3_bbox) # Función evalúa si hubo una colisión entre la nave y el asteroide 3

    # Serán las variables que la función retornrá. Dependiendo del valor booleano que alguno de los resultados almacene, se quitará un punto de vida (si es True, se quitará ese punto de vida) 
    resultado1 = False
    resultado2 = False
    resultado3 = False

    # Asteroide 1
    if colision1 == True:

        if obstaculo_1.fuerza == 1:
            resultado1 = True # Si hubo colisión y la fuerza (que se puede ver como un "modo daño" del asteroide) estaba en 1, entonces el valor que retornará la función será "True" por lo que al evaluarse en la función "asteroide_golpea_jugador" al jugador se le disminuirá una vida.
            obstaculo_1.fuerza = 0 # La fuerza se pone en cero porque habrá unos pocos milisegundos en los que la nave seguirá chocando con el asteroide, por lo que para que la función no siga detectando eso como una colisión y no siga bajando de vida, entonces la fuerza se pone en cero para que en la próxima evaluación no entre en la condición que pone a "resultado1" en "True" para que así, no se le siga quitando vida al jugador.

    else:
        obstaculo_1.fuerza = 1 # La fuerza se vuelve a poner en uno una vez el asteroide y la nave no están chocando para que la próxima vez que colisionen, sí se quite el punto de vida del jugador.
    
    # Asteroide 2
    if colision2 == True:

        if obstaculo_2.fuerza == 1:
            resultado2 = True
            obstaculo_2.fuerza = 0

    else:
        obstaculo_2.fuerza = 1
    
    # Asteroide 3
    if colision3 == True:

        if obstaculo_3.fuerza == 1:
            resultado3 = True
            obstaculo_3.fuerza = 0

    else:
        obstaculo_3.fuerza = 1
    
    # Basta con que uno de los resultados sea "True" para que la función retorne "True"
    return resultado1 or resultado2 or resultado3 

# Función de detección de colisiones para el nivel 2 (funciona igual que la función de detección de colisiones del nivel 1, solo que implementa un cuarto asteroide):
def deteccion_colisiones_2(canvas_nivel, nave, obstaculo_1, obstaculo_2, obstaculo_3, obstaculo_4):
    # "Hitbox" de cada objeto (Bbox):
    # "Bbox" de la nave:
    nave_bbox = canvas_nivel.bbox(nave.canvas)

    # "Bbox" de cada asteroide del nivel:
    obstaculo1_bbox = canvas_nivel.bbox(obstaculo_1.canvas)
    obstaculo2_bbox = canvas_nivel.bbox(obstaculo_2.canvas)
    obstaculo3_bbox = canvas_nivel.bbox(obstaculo_3.canvas)
    obstaculo4_bbox = canvas_nivel.bbox(obstaculo_4.canvas)

    colision1 = detect_colisiones(nave_bbox, obstaculo1_bbox)
    colision2 = detect_colisiones(nave_bbox, obstaculo2_bbox)
    colision3 = detect_colisiones(nave_bbox, obstaculo3_bbox)
    colision4 = detect_colisiones(nave_bbox, obstaculo4_bbox)

    resultado1 = False
    resultado2 = False
    resultado3 = False
    resultado4 = False

    # Asteroide 1
    if colision1 == True:

        if obstaculo_1.fuerza == 1:
            resultado1 = True
            obstaculo_1.fuerza = 0

    else:
        obstaculo_1.fuerza = 1
    
    # Asteroide 2
    if colision2 == True:

        if obstaculo_2.fuerza == 1:
            resultado2 = True
            obstaculo_2.fuerza = 0

    else:
        obstaculo_2.fuerza = 1
    
    # Asteroide 3
    if colision3 == True:

        if obstaculo_3.fuerza == 1:
            resultado3 = True
            obstaculo_3.fuerza = 0

    else:
        obstaculo_3.fuerza = 1
    
    # Asteroide 4
    if colision4 == True:

        if obstaculo_4.fuerza == 1:
            resultado4 = True
            obstaculo_4.fuerza = 0

    else:
        obstaculo_4.fuerza = 1
    
    return resultado1 or resultado2 or resultado3 or resultado4

# Función de detección de colisiones para el nivel 3 (funciona igual que la función de detección de colisiones del nivel 1, solo que implementa un quinto asteroide):
def deteccion_colisiones_3(canvas_nivel, nave, obstaculo_1, obstaculo_2, obstaculo_3, obstaculo_4, obstaculo_5):
    # "Hitbox" de cada objeto (Bbox):
    # "Bbox" de la nave:
    nave_bbox = canvas_nivel.bbox(nave.canvas)

    # "Bbox" de cada asteroide del nivel:
    obstaculo1_bbox = canvas_nivel.bbox(obstaculo_1.canvas)
    obstaculo2_bbox = canvas_nivel.bbox(obstaculo_2.canvas)
    obstaculo3_bbox = canvas_nivel.bbox(obstaculo_3.canvas)
    obstaculo4_bbox = canvas_nivel.bbox(obstaculo_4.canvas)
    obstaculo5_bbox = canvas_nivel.bbox(obstaculo_5.canvas)

    colision1 = detect_colisiones(nave_bbox, obstaculo1_bbox)
    colision2 = detect_colisiones(nave_bbox, obstaculo2_bbox)
    colision3 = detect_colisiones(nave_bbox, obstaculo3_bbox)
    colision4 = detect_colisiones(nave_bbox, obstaculo4_bbox)
    colision5 = detect_colisiones(nave_bbox, obstaculo5_bbox)

    resultado1 = False
    resultado2 = False
    resultado3 = False
    resultado4 = False
    resultado5 = False

    # Asteroide 1
    if colision1 == True:

        if obstaculo_1.fuerza == 1:
            resultado1 = True
            obstaculo_1.fuerza = 0

    else:
        obstaculo_1.fuerza = 1
    
    # Asteroide 2
    if colision2 == True:

        if obstaculo_2.fuerza == 1:
            resultado2 = True
            obstaculo_2.fuerza = 0

    else:
        obstaculo_2.fuerza = 1
    
    # Asteroide 3
    if colision3 == True:

        if obstaculo_3.fuerza == 1:
            resultado3 = True
            obstaculo_3.fuerza = 0

    else:
        obstaculo_3.fuerza = 1
    
    # Asteroide 4
    if colision4 == True:

        if obstaculo_4.fuerza == 1:
            resultado4 = True
            obstaculo_4.fuerza = 0

    else:
        obstaculo_4.fuerza = 1

    # Asteroide 5
    if colision5 == True:

        if obstaculo_5.fuerza == 1:
            resultado5 = True
            obstaculo_5.fuerza = 0

    else:
        obstaculo_5.fuerza = 1
    
    return resultado1 or resultado2 or resultado3 or resultado4 or resultado5

# Función de colisiones, general (evaluará el nivel en el que se está para llamar a una u otra función de colisiones):
def deteccion_colisiones_gen(nivel, canvas_nivel):

    if nivel.nivel == 1:
        return deteccion_colisiones_1(canvas_nivel, nivel.jugador, nivel.asteroide_1, nivel.asteroide_2, nivel.asteroide_3)
    elif nivel.nivel == 2:
        return deteccion_colisiones_2(canvas_nivel, nivel.jugador, nivel.asteroide_1, nivel.asteroide_2, nivel.asteroide_3, nivel.asteroide_4)
    else:
        return deteccion_colisiones_3(canvas_nivel, nivel.jugador, nivel.asteroide_1, nivel.asteroide_2, nivel.asteroide_3, nivel.asteroide_4, nivel.asteroide_5)

# Función que quitará la vida en caso de que, en efecto, se haya dado una colisión:
def asteroide_golpea_jugador(nivel, canvas_nivel):

    if deteccion_colisiones_gen(nivel, canvas_nivel) == True:
        nivel.jugador.vidas -= 1

# Función de actualización (toda la información que conforme avanza la partida se va actualizando, va en esta función):
def actualizar_juego(nivel, canvas_nivel, pantalla_nivel):

    movimiento_asteroides(nivel, canvas_nivel, pantalla_nivel)
    asteroide_golpea_jugador(nivel, canvas_nivel)
    actualiza_puntaje(nivel)
    actualiza_labels(nivel)

# Función continua_juego (evalua si el juego continua o no, dependiendo de si se ganó o se perdió):
def continua_juego(nivel):
    # Si la vida es igual o menor a 0, indicará que el jugador perdió, por lo que retornará -1
    if nivel.jugador.vidas <= 0:
        return -1
    # Si el cronómetro llega a ser igual a 60 segundos (cada nivel dura un minuto) indicará que la partida terminó y que el jugador sobrevivió, retornrá 1
    elif cronometro(nivel.tiempo_de_inicio) == 60:
        return 1
    # Si ninguna de las dos condiciones anteriores se cumplió, indicará que la partida puede continuar con normalidad, retornará un 0
    else:
        return 0

# Creamos la raíz sobre la que se desarrollará el videojuego. 
raiz_juego = Tk()

#Musica principal
pygame.init()
mixer.music.load("tema_principal.wav")
mixer.music.play(-1)

# Personalización de la raiz:
raiz_juego.title("Starscape") 

raiz_juego.iconbitmap("Icono_proyecto2.ico")

raiz_juego.geometry("1366x768")

raiz_juego.config(cursor = "star")

# Canvas sobre el que se colocarán imágenes y demás widgets:
canvas_raiz = Canvas(raiz_juego, width = 1366, height = 768, bg = "Black") # Agregar fondo
canvas_raiz.pack()

# Labels de la raíz:
# Licencia:
Label(canvas_raiz, text = "©2021 TEC CR., LTD. All Rights Reserved.", bg = "#0e212e", font = ("Impact", 15), fg = "#807e7e").place(x = 550, y = 650)

# Fondo de la raiz
bg_principal = PhotoImage(file ="bg_raiz.png")

# Fondo de la raiz
canvas_raiz.create_image(0, 0, anchor = NW, image = bg_principal)

# Fondos de los niveles
bg_nivel1 = PhotoImage(file ="bg_nivel1.png")

bg_nivel2 = PhotoImage(file ="bg_nivel2.png")

bg_nivel3 = PhotoImage(file ="bg_nivel3.png")

# Fondo puntajes
bg_puntajes = PhotoImage(file ="bg_puntajes.png")

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

        # Frame sobre el que los textos irán:
        frame_complemento = Frame(canvas_comp, width = 780, height = 500)

        frame_complemento.place(x = 312, y = 140)

        frame_complemento.config(bg = "#0e212e")

        frame_complemento.config(bd = 10)

        frame_complemento.config(relief = "groove")

        # Textos pertenecientes a la pantalla about (etiquetas de texto):
        Label(frame_complemento, text = "Hecho en:", bg = "#0e212e", font = ("Impact", 12), fg = "Light grey").place(x = 10, y = 1)

        Label(frame_complemento, text = "Costa Rica", bg = "#0e212e", font = ("Impact", 12), fg = "#807e7e").place(x = 10, y = 21)

        Label(frame_complemento, text = "Universidad:", bg = "#0e212e", font = ("Impact", 12), fg = "Light grey").place(x = 10, y = 60)

        Label(frame_complemento, text = "Instituto Tecnológico de Costa Rica", bg = "#0e212e", font = ("Impact", 12), fg = "#807e7e").place(x = 10, y = 80)

        Label(frame_complemento, text = "Carerra:", bg = "#0e212e", font = ("Impact", 12), fg = "Light grey").place(x = 10, y = 120)

        Label(frame_complemento, text = "Ingeniería en Computadores", bg = "#0e212e", font = ("Impact", 12), fg = "#807e7e").place(x = 10, y = 140)

        Label(frame_complemento, text = "Curso:", bg = "#0e212e", font = ("Impact", 12), fg = "Light grey").place(x = 10, y = 180)

        Label(frame_complemento, text = "Taller a la programación (CE1102), 2021, groupo #4", bg = "#0e212e", font = ("Impact", 12), fg = "#807e7e").place(x = 10, y = 200)

        Label(frame_complemento, text = "Profesor:", bg = "#0e212e", font = ("Impact", 12), fg = "Light grey").place(x = 10, y = 240)

        Label(frame_complemento, text = "Leonardo Araya Martínez", bg = "#0e212e", font = ("Impact", 12), fg = "#807e7e").place(x = 10, y = 260)

        Label(frame_complemento, text = "Versión:", bg = "#0e212e", font = ("Impact", 12), fg = "Light grey").place(x = 10, y = 300)

        Label(frame_complemento, text = "1.0", bg = "#0e212e", font = ("Impact", 12), fg = "#807e7e").place(x = 65, y = 300)

        Label(frame_complemento, text = "Autores:", bg = "#0e212e", font = ("Impact", 12), fg = "Light grey").place(x = 10, y = 340)

        Label(frame_complemento, text = "Esteban Josué Solano Araya y Luis Felipe Brenes Ramírez", bg = "#0e212e", font = ("Impact", 12), fg = "#807e7e").place(x = 10, y = 360)

        Label(frame_complemento, text = "Bibliotecas usadas:", bg = "#0e212e", font = ("Impact", 12), fg = "Light grey").place(x = 10, y = 400)

        Label(frame_complemento, text = "Tkinter (Fredrik Lundh), Pygame (Lenard Lindstrom, René Dudfield, Pete Shinners, Nicholas Dudfield, Thomas Kluyver", bg = "#0e212e", font = ("Impact", 12), fg = "#807e7e").place(x = 10, y = 420)

        Label(frame_complemento, text = "y otros), Datetime y Random", bg = "#0e212e", font = ("Impact", 12), fg = "#807e7e").place(x = 10, y = 445)
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

            # Frame sobre el que irán las instrucciones (labels de texto):
            frame_instrucciones = Frame(canvas_ayuda, width = 780, height = 500)

            frame_instrucciones.place(x = 312, y = 140)

            frame_instrucciones.config(bg = "#0e212e")

            frame_instrucciones.config(bd = 10)

            frame_instrucciones.config(relief = "groove")

            # Instrucciones que irán sobre el frame (etiquetas de texto):
            Label(frame_instrucciones, text = "Instrucciones:", bg = "#0e212e", font = ("Impact", 12), fg = "Light grey").place(x = 345, y = 1)

            Label(frame_instrucciones, text = "1.", bg = "#0e212e", font = ("Impact", 12), fg = "Light grey").place(x = 10, y = 51)

            Label(frame_instrucciones, text = "Usa las flechas de tu teclado para esquivar los asteroides.", bg = "#0e212e", font = ("Impact", 12), fg = "#807e7e").place(x = 35, y = 51)

            Label(frame_instrucciones, text = "2.", bg = "#0e212e", font = ("Impact", 12), fg = "Light grey").place(x = 10, y = 111)

            Label(frame_instrucciones, text = "Sobrevive por un minuto para pasar al siguiente nivel.", bg = "#0e212e", font = ("Impact", 12), fg = "#807e7e").place(x = 35, y = 111)

            Label(frame_instrucciones, text = "3.", bg = "#0e212e", font = ("Impact", 12), fg = "Light grey").place(x = 10, y = 161)

            Label(frame_instrucciones, text = "No dejes que los asteroides te toquen, te quitarán vidas (cuentas con tres vidas).", bg = "#0e212e", font = ("Impact", 12), fg = "#807e7e").place(x = 35, y = 161)

            Label(frame_instrucciones, text = "4.", bg = "#0e212e", font = ("Impact", 12), fg = "Light grey").place(x = 10, y = 221)

            Label(frame_instrucciones, text = "¡Diviértete!", bg = "#0e212e", font = ("Impact", 12), fg = "#807e7e").place(x = 35, y = 221)

            Label(frame_instrucciones, text = "¡Gracias por jugar :D!", bg = "#0e212e", font = ("Impact", 12), fg = "Light grey").place(x = 325, y = 281)

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

        # Frame sobre el que irá el texto: "Elige un nivel":
        frame_niveles = Frame(canvas_niveles, width = 500, height = 150)

        frame_niveles.place(x = 450, y = 300)

        frame_niveles.config(bg = "#0e212e")

        frame_niveles.config(bd = 10)

        frame_niveles.config(relief = "groove")

        # Etiqueta con el texto "Elige un nivel":
        Label(frame_niveles, text = "Elige un nivel:", bg = "#0e212e", font = ("Impact", 35), fg = "#807e7e").place(x = 110, y = 25)

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

            # Musica nivel
            mixer.music.stop()

            mixer.music.load("tema_nivel2.wav")

            mixer.music.play(-1)

            # Parámetros para la creación de la partida/juego (Nivel 1):
            # Nombre jugador:
            nombre_de_jugador = nombre_jugador.get()

            # Creación del jugador:
            jugador = Jugador(nombre_de_jugador, 3, sprite_naveJugador, 620, 585)

            # Creación asteroides:
            asteroide1 = Asteroides(sprite_asteroides, random.randint(0, 1238), -30)

            asteroide2 = Asteroides(sprite_asteroides, random.randint(0, 1238), -30)

            asteroide3 = Asteroides(sprite_asteroides, random.randint(0, 1238), -30)

            asteroide4 = Asteroides(sprite_asteroides, random.randint(0, 1238), -30)

            # Creación del nivel:
            segundo_nivel = Nivel2(jugador, asteroide1, asteroide2, asteroide3, asteroide4, datetime.datetime.now())

            # Llamada para renderizar
            ciclo_juego(segundo_nivel, canvas_nivel_2, pantalla_nivel_2)

            # Función del botón "Atrás" de la pantalla del nivel 2:
            def atras_nivel_2():
                pantalla_nivel_2.destroy()

                # Parar musica del nivel y reproducir tema principal
                mixer.music.stop()

                mixer.music.load("tema_principal.wav")

                mixer.music.play(-1)

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

            # Musica nivel
            mixer.music.stop()

            mixer.music.load("tema_nivel3.wav")

            mixer.music.play(-1)

            # Parámetros para la creación de la partida/juego (Nivel 1):
            # Nombre jugador:
            nombre_de_jugador = nombre_jugador.get()

            # Creación del jugador:
            jugador = Jugador(nombre_de_jugador, 3, sprite_naveJugador, 620, 585)

            # Creación asteroides:
            asteroide1 = Asteroides(sprite_asteroides, random.randint(0, 1238), -30)

            asteroide2 = Asteroides(sprite_asteroides, random.randint(0, 1238), -30)

            asteroide3 = Asteroides(sprite_asteroides, random.randint(0, 1238), -30)

            asteroide4 = Asteroides(sprite_asteroides, random.randint(0, 1238), -30)

            asteroide5 = Asteroides(sprite_asteroides, random.randint(0, 1238), -30)

            # Creación del nivel:
            tercer_nivel = Nivel3(jugador, asteroide1, asteroide2, asteroide3, asteroide4, asteroide5, datetime.datetime.now())

            # Llamada para renderizar
            ciclo_juego(tercer_nivel, canvas_nivel_3, pantalla_nivel_3)

            # Función del botón "Atrás" de la pantalla del nivel 3:
            def atras_nivel_3():
                pantalla_nivel_3.destroy()

                # Parar musica del nivel y repoducir tema principal
                mixer.music.stop()

                mixer.music.load("tema_principal.wav")

                mixer.music.play(-1)
            
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
        Label(canvas_niveles, text = "Introduzca su nombre:", bg = "#0e212e", fg = "#807e7e").place(x = 560, y = 600)
    
        # Entry sobre el que se digita el nombre:
        nombre_jugador = Entry(canvas_niveles, text = "Introduzca su nombre:", bg = "White")

        nombre_jugador.place(x = 690, y = 600)

        # Frames que aparecerán en la pantalla de nivel después de cierto evento (perder o ganar la partida):
        # Frame de victoria (será el cuadro que aparece al ganar la partida):
        def frame_de_victoria(nivel, canvas_nivel, pantalla_nivel):
            
            # Dependiendo del nivel en el que se esté, se mostrará un "frame" de victoria u otro. La única diferencia es que en el "frame" de victoria del nivel 3 solo hay un botón para ir hacia a atrás, pues no hay más niveles después del tercero.
            if nivel.nivel == 1 or nivel.nivel == 2:
                frame_victoria = Frame(canvas_nivel, width = 680, height = 400)
                frame_victoria.place(x = 340, y = 180)

                frame_victoria.config(bg = "#0e212e")
                frame_victoria.config(bd = 10)
                frame_victoria.config(relief = "groove")

                Label(canvas_nivel, text = "¡Victoria!", bg = "#0e212e", fg = "White", font = ("Impact", 25)).place(x = 615, y = 250)

                # Funciones asignadas a los botones:
                def siguiente_nivel():
                    pantalla_nivel.destroy()
                    if nivel.nivel == 1:
                        Nivel_2()
                    elif nivel.nivel == 2:
                        Nivel_3()
                def atras():
                    pantalla_nivel.destroy()

                    # Parar musica del nivel y repoducir tema principal
                    mixer.music.stop()

                    mixer.music.load("tema_principal.wav")

                    mixer.music.play(-1)

                # Botones del frame:
                boton_siguiente = Button(frame_victoria, text = "Siguiente nivel", padx = 10, pady = 5, font = "Impact", relief = "raised", bg = "Purple", command = siguiente_nivel)
                boton_siguiente.place(x = 335, y = 280)

                boton_atras = Button(frame_victoria, text = "Atrás", padx = 10, pady = 5, font = "Impact", relief = "raised", bg = "Purple", command = atras)
                boton_atras.place(x = 245, y = 280)
            
            # Frame de victoria del nivel 3:
            else:
                frame_victoria = Frame(canvas_nivel, width = 680, height = 400)
                frame_victoria.place(x = 340, y = 180)

                frame_victoria.config(bg = "#0e212e")
                frame_victoria.config(bd = 10)
                frame_victoria.config(relief = "groove")

                Label(canvas_nivel, text = "¡Victoria!", bg = "#0e212e", fg = "White", font = ("Impact", 25)).place(x = 615, y = 250)

                # Función del botón "Atrás"
                def atras():
                    pantalla_nivel.destroy()

                    # Parar musica del nivel y repoducir tema principal
                    mixer.music.stop()

                    mixer.music.load("tema_principal.wav")

                    mixer.music.play(-1)
        
                # Botón "Atrás":
                boton_atras = Button(frame_victoria, text = "Atrás", padx = 10, pady = 5, font = "Impact", relief = "raised", bg = "Purple", command = atras)
                boton_atras.place(x = 295, y = 280)
        
        # Pantalla que se muestra al perder el juego:
        def frame_perdiste(nivel, canvas_nivel, pantalla_nivel):
            frame_perder = Frame(canvas_nivel, width = 680, height = 400)
            frame_perder.place(x = 340, y = 180)

            frame_perder.config(bg = "#0e212e")
            frame_perder.config(bd = 10)
            frame_perder.config(relief = "groove")

            Label(canvas_nivel, text = "¡Has perdido!", bg = "#0e212e", fg = "White", font = ("Impact", 25)).place(x = 615, y = 250)

            # Funciones de los botones del "frame" que se muestra al perder:
            def intentar_de_nuevo():
                pantalla_nivel.destroy()
                if nivel.nivel == 1:
                    Nivel_1()

                elif nivel.nivel == 2:
                    Nivel_2()

                elif nivel.nivel == 3:
                    Nivel_3()

            def atras():
                pantalla_nivel.destroy()

                # Parar musica del nivel y repoducir tema principal
                mixer.music.stop()

                mixer.music.load("tema_principal.wav")

                mixer.music.play(-1)

            # Botones del frame que se muestra al perder el nivel:
            Intentar_de_nuevo_boton = Button(frame_perder, text = "Intentar de nuevo", padx = 10, pady = 5, font = "Impact", relief = "raised", bg = "Purple", command = intentar_de_nuevo)
            Intentar_de_nuevo_boton.place(x = 335, y = 280)

            boton_atras = Button(frame_perder, text = "Atrás", padx = 10, pady = 5, font = "Impact", relief = "raised", bg = "Purple", command = atras)
            boton_atras.place(x = 245, y = 280)

        # Esta es la función que llevará el ciclo del juego, mientras el estado del juego sea 0, la función se seguirá ejecutando.
        # Mientras la partida siga en pie, la función del ciclo del juego se seguirá llamando, y con ello, las funciones que en esta función se llaman también seguirán llamándose y cumpliendo con sus respectivas tareas.
        def ciclo_juego(nivel, canvas_nivel, pantalla_nivel):

            renderizacion(nivel, canvas_nivel, pantalla_nivel)

            actualizar_juego(nivel, canvas_nivel, pantalla_nivel)
    
            continuar = continua_juego(nivel)

            # La función continuará llamándose
            if continuar == 0:
                pantalla_nivel.after(100, ciclo_juego, nivel, canvas_nivel, pantalla_nivel)

            # Indicará que el jugador ha perdido, por lo que se mostrará el "frame_perdiste"
            elif continuar == -1:
                frame_perdiste(nivel, canvas_nivel, pantalla_nivel)

            # Indicará que el jugador sobrevivió los 60 segundos que dura el nivel, por lo que el "frame_de_victoria" se mostrará
            else:
                frame_de_victoria(nivel, canvas_nivel, pantalla_nivel)

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

# Loop que mantendrá la aplicación abierta en todo momento.
raiz_juego.mainloop()