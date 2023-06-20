from obstaculo import Obstaculo
import pygame
import random as rd

lista_de_paths = ['Imagenes/agua/agua_1.png', 'Imagenes/agua/agua_2.png', 'Imagenes/agua/agua_3.png', 'Imagenes/agua/agua_4.png']
lista_de_aguas = []

for elemento in lista_de_paths:
    imagen_a_mostrar = pygame.image.load(elemento)
    imagen_a_mostrar = pygame.transform.scale(imagen_a_mostrar, (64,64))
    lista_de_aguas.append(imagen_a_mostrar)


class Agua(Obstaculo):
    def __init__(self, x, y, nombre='agua')->None:
        super().__init__(x, y, nombre)
        self.__numero = rd.randint(0, 3)
        self.imagen_mostrada = lista_de_aguas[self.numero].convert_alpha()

    @property
    def numero(self)->int:
        return self.__numero
