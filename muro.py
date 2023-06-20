from obstaculo import Obstaculo
import pygame
import random as rd

lista_de_paths = ['Imagenes/Muros/muro_1.jpg', 'Imagenes/Muros/muro_2.jpg', 'Imagenes/Muros/muro_3.jpg', 'Imagenes/Muros/muro_4.jpg']
lista_de_muros = []

for elemento in lista_de_paths:
    imagen_a_mostrar = pygame.image.load(elemento)
    imagen_a_mostrar = pygame.transform.scale(imagen_a_mostrar, (64,64))
    lista_de_muros.append(imagen_a_mostrar)


class Muro(Obstaculo):
    def __init__(self, x, y, nombre='muro')->None:
        super().__init__(x, y, nombre)

        self.__numero = rd.randint(0, 3)
        self.imagen_mostrada = lista_de_muros[self.numero].convert_alpha()

    @property
    def numero(self)->int:
        return self.__numero