from obstaculo import Obstaculo
import pygame

class Muro(Obstaculo):
    def __init__(self, x, y, nombre='muro')->None:
        super().__init__(x, y, nombre)

        self.imagen_mostrada = pygame.image.load('Imagenes/muro.png')