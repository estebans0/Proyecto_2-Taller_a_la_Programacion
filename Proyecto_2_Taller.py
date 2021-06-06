from tkinter import *
import datetime
import random

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

        if (self.posicion_x + pixeles < 1000): # Marca un límite, si el jugador se pasa del mismo, no se moverá más
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

        if (self.posicion_y - pixeles > 400):
            self.posicion_y = self.posicion_y - pixeles
            return pixeles
        else:
            return 0
    
    def movimiento_abajo(self, pixeles):

        if (self.posicion_y + pixeles < 700):
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
        self.direccion = 1 # Es un valor temporal, cuando el asteroide llegue a un límite, el valor cambiará si signo, cambiando así la trayectoria horizontal

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

# Creamos la raíz sobre la que se desarrollará el videojuego. 
raiz_juego = Tk()

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

# Botón perteneciente a la función "funcion_jugar":

Boton_jugar = Button(canvas_raiz, text = "Jugar", padx = 10, pady = 5, font = "Impact", relief = "raised", bg = "Purple", command = funcion_jugar)
Boton_jugar.place(x = 550, y = 500)

# Función del botón "Salir":
def cerrar_juego():
    raiz_juego.destroy()

# Botón perteneciente a la función "cerrar_juego":

Boton_cerrar = Button(canvas_raiz, text = "Salir", padx = 10, pady = 5, font = "Impact", relief = "raised", bg = "Purple", command = cerrar_juego)
Boton_cerrar.place(x = 800, y = 500)

raiz_juego.mainloop()