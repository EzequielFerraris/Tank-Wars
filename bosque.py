from obstaculo import Obstaculo
import pygame

class Bosque(Obstaculo):
    def __init__(self, x, y, nombre='bosque')->None:
        super().__init__(x, y, nombre)

        self.imagen_mostrada = pygame.image.load('Imagenes/bosque.png').convert_alpha()
        self.rect_principal = pygame.Rect(self.x-2, self.y-2, 0, 0) 