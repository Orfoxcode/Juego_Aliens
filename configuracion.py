import pygame

'''Módulo con los ajustes y configuración.'''

class Configuracion:

    def __init__(self):

        #Configuración de pantalla.

        self.pantalla_yalto = 700
        self.pantalla_xancho = 1000
        self.backgorund_color = (254, 249, 231)
        self.nombre_pantalla = "JUEGO DE ALIENS"

        #Configuracioin fondo.
        self.background_imagen = "files/pics/fondo.bmp"
        self.fondo_xancho = self.pantalla_xancho
        self.fondo_yalto = 1400
        self.velocidad_fondo = 0.5
        

        #Configuracion tiempo.
        self.fps = 60

        #Parámetros de la nave.
        self.imagen_nave = "files/pics/nave_espacial.bmp"
        self.nave_xancho  = 85
        self.nave_yalto = 70
        self.distancia_fondo = 100
        self.velocidad_y_nave = 8
        self.velocidad_x_nave = 8
        self.velocidad_vuelta_y_nave = 2


        #Balas.
        self.balas_velocidad = 10
        self.balas_ancho = 3
        self.balas_alto = 15
        self.balas_color = (230,239,239)
