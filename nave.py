import pygame


class Nave:
    '''Esta clase gestiona la nave.'''

    def __init__(self, ai_game, configuracion):
        '''Inicializa la nave y la ubica en su posición inicial.'''

        self.configuracion = configuracion

        self.pantalla = ai_game.pantalla
        self.pantalla_rect = ai_game.pantalla_rect

        #Carga la nave.  # Coloca inicialmente cada nave nueva en el centro de la parte inferior.

        self._carga_nave()
        self.nave_rect.midbottom = self.pantalla_rect.midbottom
        self.posicion_inicial = self.configuracion.pantalla_yalto - self.configuracion.distancia_fondo
        self.nave_rect.y = self.posicion_inicial
        #Bandera de movimiento.

        self.movimiento_derecha = False
        self.movimiento_izquierda = False
        self.movimiento_arriba = False
        self.movimiento_abajo = False


        #Gruarda un valor decimal par al aposción horizontale exacta de la nave.
        self.x = float(self.nave_rect.x)
        self.y = float(self.nave_rect.y)

        

    def _carga_nave(self):

        #Carga la imagen de la nave y obtiene su rect.
        self.image = pygame.image.load(self.configuracion.imagen_nave)
        self.image = pygame.transform.scale(
            self.image, 
            (self.configuracion.nave_xancho, 
            self.configuracion.nave_yalto))
        
        self.nave_rect = self.image.get_rect()


    def dibuja_nave(self):
        '''Coloca y dibuja la nave en su ubicacion actual

        #Coloca inicialmente cada nave nueva en el centro de la parte inferior.
        self.rect.midbottom = self.pantalla_rect.midbottom
        self.rect.y = self.configuracion.pantalla_yalto - self.configuracion.distancia_fondo
        '''

        self.pantalla.blit(self.image, self.nave_rect)

    def actualizar(self):
        '''Actualiza la posición de la nave en función del estado de las banderas'''


        if self.movimiento_derecha == True and self.nave_rect.right < self.pantalla_rect.right:
            self.x += self.configuracion.velocidad_x_nave

        if self.movimiento_izquierda == True and self.nave_rect.left > self.pantalla_rect.left:
            self.x -= self.configuracion.velocidad_x_nave

        if self.movimiento_arriba == True and self.nave_rect.top > self.pantalla_rect.top:
            self.y -= self.configuracion.velocidad_y_nave

        if self.movimiento_abajo == True and self.nave_rect.bottom < self.pantalla_rect.bottom:
            self.y += self.configuracion.velocidad_y_nave

        if self.nave_rect.y < self.posicion_inicial:
            self.y += self.configuracion.velocidad_vuelta_y_nave




        self.nave_rect.x = self.x
        self.nave_rect.y = self.y





        