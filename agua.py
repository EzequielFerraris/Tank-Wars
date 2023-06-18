from obstaculo import Obstaculo
import pygame

class Agua(Obstaculo):
    def __init__(self, x, y, nombre='agua')->None:
        super().__init__(x, y, nombre)

        self.imagen_mostrada = pygame.image.load('Imagenes/agua.png').convert_alpha()