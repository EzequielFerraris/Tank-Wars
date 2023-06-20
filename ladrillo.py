from obstaculo import Obstaculo
import pygame
import random as rd

lista_de_paths = ['Imagenes/Ladrillos/ladrillos_1.png', 'Imagenes/Ladrillos/ladrillos_2.png', 'Imagenes/Ladrillos/ladrillos_3.png', 'Imagenes/Ladrillos/ladrillos_4.png']
lista_de_ladrillos = []

for elemento in lista_de_paths:
    imagen_a_mostrar = pygame.image.load(elemento)
    imagen_a_mostrar = pygame.transform.scale(imagen_a_mostrar, (64,64))
    lista_de_ladrillos.append(imagen_a_mostrar)

class Ladrillo(Obstaculo):
    def __init__(self, x, y, nombre='ladrillo')->None:
        super().__init__(x, y, nombre)
        self.__numero = rd.randint(0, 3)
        self.imagen_mostrada = lista_de_ladrillos[self.numero].convert_alpha()

    @property
    def numero(self)->int:
        return self.__numero