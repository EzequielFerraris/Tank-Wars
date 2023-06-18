from obstaculo import Obstaculo
import pygame

class Ladrillo(Obstaculo):
    def __init__(self, x, y, nombre='ladrillo')->None:
        super().__init__(x, y, nombre)

        self.imagen_mostrada = pygame.image.load('Imagenes/ladrillos.png').convert_alpha()