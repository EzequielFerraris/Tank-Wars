from obstaculo import Obstaculo
import pygame
import random as rd

lista_de_paths = ['Imagenes/Bosques/bosque_1.jpeg', 'Imagenes/Bosques/bosque.png']
lista_de_bosques = []

for elemento in lista_de_paths:
    imagen_a_mostrar = pygame.image.load(elemento)
    imagen_a_mostrar = pygame.transform.scale(imagen_a_mostrar, (64,64))
    lista_de_bosques.append(imagen_a_mostrar)


class Bosque(Obstaculo):
    def __init__(self, x, y, nombre='bosque')->None:
        super().__init__(x, y, nombre)

        self.__numero = rd.randint(0, 1)
        self.imagen_mostrada = lista_de_bosques[self.numero].convert_alpha()
        self.rect_principal = pygame.Rect(self.x-2, self.y-2, 0, 0) 

    @property
    def numero(self)->int:
        return self.__numero