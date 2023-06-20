import pygame
from tanque import Tanque

class Jugador(Tanque):
    def __init__(self, x, y, nombre, direccion_original, puntaje)->None:
        super().__init__(x, y, nombre, direccion_original, puntaje)

        self.maximo_proyectiles_simultaneos = 5
        
    #IMAGENES:
        self.imagen_arriba = pygame.image.load('Imagenes/Jugador/Tanke_arriba.png').convert_alpha()
        self.imagen_abajo = pygame.image.load('Imagenes/Jugador/Tanke_abajo.png').convert_alpha()
        self.imagen_derecha = pygame.image.load('Imagenes/Jugador/Tanke_der.png').convert_alpha()
        self.imagen_izquierda = pygame.image.load('Imagenes/Jugador/Tanke_izq.png').convert_alpha()


