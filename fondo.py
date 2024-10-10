import pygame


class Fondo:

    def __init__(self, ai_game, configuracion):

        self.configuracion = configuracion

        self.pantalla = ai_game.pantalla
        self.pantalla_rect = ai_game.pantalla_rect


        self._carga_fondo()

        self.posicion_y = float(self.fondo_rect.y)


    def _carga_fondo(self):
        #Carga imagen de fondo y obtiene su rect.
        self.fondo = pygame.image.load(self.configuracion.background_imagen)
        self.fondo = pygame.transform.scale(
            self.fondo,
            (self.configuracion.fondo_xancho,
            self.configuracion.fondo_yalto))
        
        self.fondo_rect = self.fondo.get_rect()
        self.fondo_rect.midbottom = self.pantalla_rect.midbottom


    def dibuja_fondo(self):
        '''Coloca y dibuja el fondo '''
        self.pantalla.blit(self.fondo, self.fondo_rect)
        
    
    def fondo_avanza_automaticamente(self):

        if self.fondo_rect.midtop == self.pantalla_rect.midtop:
            self.fondo = pygame.transform.flip(self.fondo,True, True)
            
            self.fondo_rect.midbottom = self.pantalla_rect.midbottom
            self.posicion_y = float(self.fondo_rect.y)

        else:
            self.posicion_y += float(self.configuracion.velocidad_fondo)
            self.fondo_rect.y = int(self.posicion_y)
            

        '''
        if self.fondo_rect.y == 0:
            self.fondo_continuacion = pygame.image.load(self.configuracion.background_imagen)
            self.fondo_continuacion = pygame.transform.rotate(self.fondo, 180)
            self.fondo_continuacion = pygame.transform.flip(self.fondo, True, False)

            self.fondo_continuacion_rect = self.fondo_continuacion.get_rect()
            self.fondo_rect.midbottom = self.pantalla_rect.midtop
            self.pantalla.blit(self.fondo_continuacion, self.fondo_continuacion_rect)

        else:
            self.fondo_rect.y += 1

            if self.fondo_continuacion_rect:
                self.fondo_continuacion_rect.y += 1
        '''



            


