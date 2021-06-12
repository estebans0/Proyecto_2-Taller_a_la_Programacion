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

fondo_raiz = PhotoImage(file = "fondo_raiz.png")

# Canvas sobre el que se colocarán imágenes y demás widgets:
canvas_raiz = Canvas(raiz_juego, width = 1366, height = 768, bg = "Black") # Agregar fondo
canvas_raiz.pack()

# Fondo de la raiz
canvas_raiz.create_image(0, 0, anchor = NW, image = fondo_raiz)

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

    # Canvas, pantalla de selección:
    canvas_seleccion = Canvas(pantalla_seleccion, width = 1366, height = 768, bg = "Black")
    canvas_seleccion.pack()

    # Fondo
    canvas_seleccion.create_image(0, 0, anchor=NW, image=fondo_raiz)

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
            # canvas_nivel_1.create_image(0, 0, anchor = NW, image = bg_level1)

            # Parámetros para la creación de la partida/juego (Nivel 1):
            # Nombre jugador:
            # nombre_de_jugador = nombre_jugador.get()
            # print(nombre_de_jugador)

            # Función del botón "Atrás" de la pantalla del nivel 1:
            def atras_nivel_1():
                pantalla_nivel_1.destroy()
            
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
            # canvas_nivel_2.create_image(0, 0, anchor = NW, image = bg_level1)

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
            # canvas_nivel_3.create_image(0, 0, anchor = NW, image = bg_level1)
    
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