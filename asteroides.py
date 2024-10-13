import pygame
from pygame.sprite import Sprite
from random import choice

import configuracion


class Asteroide(Sprite):

    def __init__(self, ai_game):

        super().__init__()

        self.juego = ai_game
        self.pantalla = ai_game.pantalla
        self.pantalla_rect = ai_game.pantalla_rect
        self.configuracion = ai_game.configuracion

        #Crea un asteroide y le asigna; escala, ángulo y posición aleatoria.
        self.asteroide_imagen = pygame.image.load(self.configuracion.asteroide_imagen01)
        self.asteroide_imagen = pygame.transform.scale(self.asteroide_imagen, (self.configuracion.asteroide_xtamano_inicial * choice(self.configuracion.asteroide_escala), self.configuracion.asteroide_ytamano_inicial * choice(self.configuracion.asteroide_escala)))
        self.asteroide_imagen = pygame.transform.rotate(self.asteroide_imagen, choice(self.configuracion.asteroide_angulo))

        self.asteroide_rect = self.asteroide_imagen.get_rect()

        self.velocidadx = choice(self.configuracion.asteroide_xvelocidad)
        self.velocidady = choice(self.configuracion.asteroide_yvelocidad)

        self.asteroide_rect.x = choice(self.configuracion.asteroide_xrango)
        self.asteroide_rect.y = choice(self.configuracion.asteroide_yrango) - self.configuracion.pantalla_yalto


    def dibuja_asteroide(self):

        #Posición       
        self.pantalla.blit(self.asteroide_imagen, self.asteroide_rect)


    def actualiza_asteroide(self):

        self.asteroide_rect.y += self.velocidady

        if self.asteroide_rect.x <= 0:
            self.velocidadx *= (-1)
            self.asteroide_rect.x += self.velocidadx
        else:
            self.asteroide_rect.x += self.velocidadx

        if self.asteroide_rect.right >= self.configuracion.pantalla_xancho:
            self.velocidadx *= (-1)
            self.asteroide_rect.x += self.velocidadx   
        else:
            self.asteroide_rect.x += self.velocidadx
        

        





