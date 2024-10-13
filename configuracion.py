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

        #Asteroide
        self.asteroide_imagen01 = "files/pics/asteroide_01.bmp"
        self.asteroide_xvelocidad = range(-2, 2)
        self.asteroide_yvelocidad = range(1, 2)
        self.asteroide_xrango = range(0, self.pantalla_xancho)
        self.asteroide_yrango = range(0, self.pantalla_yalto)
        self.asteroide_angulo = range(0,360)
        self.asteroide_escala = [1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2,2.5,3]
        self.asteroide_xtamano_inicial = 50
        self.asteroide_ytamano_inicial = 50


