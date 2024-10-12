import pygame
from pygame.sprite import Sprite


class Bala(Sprite):

    def __init__(self, ai_game):

        super().__init__()

        self.pantalla = ai_game.pantalla
        self.configuracion = ai_game.configuracion
        self.bala_color = self.configuracion.balas_color

        #Crea rectángulo para la bala (0,0) y luego establece la posición correcta.
        self.bala_rect = pygame.Rect(0,0,
            self.configuracion.balas_ancho, self.configuracion.balas_alto)
        
        self.bala_rect.midtop = ai_game.nave.nave_rect.midtop

        #Guarda la posición de la bala como flotante.
        #self.y = float(self.bala_rect.y)



    def dibuja_bala(self):
        '''Dibuja la bala en la pantalla'''

        pygame.draw.rect(self.pantalla, self.bala_color, self.bala_rect)

            

    def actualiza_bala(self):

        #Mueve la bala hacia arriba de la pantalla. 
        self.bala_rect.y -= self.configuracion.bala_velocidad

    def elimina_bala(self):

        #Marca la bala que ha salido de la pantalla
        if self.bala_rect.bottom == self.pantalla_rect.top:
            return True