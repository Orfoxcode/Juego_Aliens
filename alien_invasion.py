import sys
import pygame

import asteroides
import configuracion

from configuracion import Configuracion
from nave import Nave
from fondo import Fondo
from balas import Bala
from asteroides import Asteroide


class AlienInvasion:
    '''Clase general del juego. Gestiona los recursos y su comportamiento.'''

    def __init__(self):
        '''Inicializa el juego y crea recursos.'''

        pygame.init()
        self.reloj = pygame.time.Clock()
    
        #Clase 'Configuración'.
        self.configuracion = Configuracion()

        #Pantalla.
        self.pantalla = pygame.display.set_mode(
            (self.configuracion.pantalla_xancho, 
            self.configuracion.pantalla_yalto))

        self.pantalla_rect = self.pantalla.get_rect()
        pygame.display.set_caption(self.configuracion.nombre_pantalla)

        #Clase 'Nave'.
        self.nave = Nave(self, self.configuracion)

        #Clase 'Fondo'
        self.fondo = Fondo(self, self.configuracion)

        #Grupo 'Balas'
        self.balas = pygame.sprite.Group()

        #Asteroide
        self.asteroides = pygame.sprite.Group()




    def run_game(self):
        '''Inicia el bucle principal para el juego.'''

        while True:
            self._revisa_eventos()
            self.balas.update()
            
            self._actualiza_pantalla()

            self.reloj.tick(self.configuracion.fps)


    def _revisa_eventos(self):
    #Busca eventos de teclado y ratón. Responde a las pulsacione sdel usuario.
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._comprobar_keydown_eventos(event)
            
            elif event.type == pygame.KEYUP:
                self._comprobar_keyup_eventos(event)

    def _comprobar_keydown_eventos(self, event):
        if event.key == pygame.K_RIGHT:
            self.nave.movimiento_derecha = True       
        elif event.key == pygame.K_LEFT:
            self.nave.movimiento_izquierda = True
        elif event.key == pygame.K_UP:
            self.nave.movimiento_arriba = True        
        elif event.key == pygame.K_DOWN:
            self.nave.movimiento_abajo = True   
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._disparar_balas()

    def _comprobar_keyup_eventos(self, event):
        if event.key == pygame.K_RIGHT:
            self.nave.movimiento_derecha = False     
        elif event.key == pygame.K_LEFT:
            self.nave.movimiento_izquierda = False
        elif event.key == pygame.K_UP:
            self.nave.movimiento_arriba = False        
        elif event.key == pygame.K_DOWN:
            self.nave.movimiento_abajo = False

    def _disparar_balas(self):
        '''Crea una nueva bala y la añade al grupo de balas'''

        nueva_bala = Bala(self)
        self.balas.add(nueva_bala)

    def _crea_asteroide(self):
        '''Crea un nuevo asteroide y lo añade al grupo de asteroides'''

        #Dibuja un asteroide.

        #nuevo_asteroide.dibuja_asteroide()

        
        if len(self.asteroides) <= 21:
            nuevo_asteroide = Asteroide(self)
            self.asteroides.add(nuevo_asteroide)
            

    def _actualiza_pantalla(self):
            
        #Asigna color a la ventana.
        self.pantalla.fill(self.configuracion.backgorund_color)

        #Redibuja el fondo y gestiona su movimiento automático:
        self.fondo.dibuja_fondo()
        self.fondo.fondo_avanza_automaticamente()

        #Redibuja la nave en su posición inicial.
        #self.nave._carga_nave()
        self.nave.dibuja_nave()
        self.nave.actualizar()


        #Dibuja asteroide.
        self._crea_asteroide()  
        
        for asteroide in self.asteroides.sprites():
            asteroide.dibuja_asteroide()
            asteroide.actualiza_asteroide()
            
            if asteroide.asteroide_rect.top >= self.configuracion.pantalla_yalto:
                self.asteroides.remove(asteroide)
            else:
                asteroide.asteroide_rect.y += asteroide.velocidady

            #if asteroide.asteroide_rect.left <= 0 or asteroide.asteroide_rect.right >= self.configuracion.pantalla_xancho:
            #    asteroide.asteroide_rect.x = asteroide.asteroide_rect.x * (-1)
            

        #  asteroide.asteroide_rect.y += asteroide.velocidady
        #  asteroide.asteroide_rect.x += asteroide.velocidadx    


        #Dibuja las balas.
        for bala in self.balas.sprites():
            bala.dibuja_bala()
        
        for bala in self.balas.sprites():
            if bala.bala_rect.bottom <= 0:  # Si la bala sale por la parte superior
                self.balas.remove(bala)
            else:
                bala.bala_rect.y -= 10



        #Hace visible la última pantalla dibujada.
        pygame.display.flip()



if __name__ == "__main__":
    #Hace una instancia del juego y lo ejecuta.
    ai = AlienInvasion()
    ai.run_game()   




