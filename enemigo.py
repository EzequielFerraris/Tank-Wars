import random as rd
import pygame
from tanque import Tanque
from proyectil import Proyectil

class Enemigo(Tanque):
    def __init__(self, x, y, nombre, direccion_original, velocidad=16)->None:
        super().__init__(x, y, nombre, direccion_original)
    
        self.__valor_random = 0
        self.__cambiar_direccion = 0
        self.__contador_de_pasos = 0
        self.velocidad = velocidad

    #IMAGENES:
        self.imagen_arriba = pygame.image.load('Imagenes/Enemigo_arriba.png').convert_alpha()
        self.imagen_abajo = pygame.image.load('Imagenes/Enemigo_abajo.png').convert_alpha()
        self.imagen_derecha = pygame.image.load('Imagenes/Enemigo_derecha.png').convert_alpha()
        self.imagen_izquierda = pygame.image.load('Imagenes/Enemigo_izquierda.png').convert_alpha()

    @property
    def valor_random(self)->int:
        return self.__valor_random

    @valor_random.setter
    def valor_random(self, nuevo_valor_random:int)->int:
        self.__valor_random = nuevo_valor_random

    @property
    def cambiar_direccion(self)->int:
        return self.__cambiar_direccion

    @cambiar_direccion.setter
    def cambiar_direccion(self, nueva_cambiar_direccion:int)->int:
        self.__cambiar_direccion = nueva_cambiar_direccion

    @property
    def contador_de_pasos(self)->int:
        return self.__contador_de_pasos

    @contador_de_pasos.setter
    def contador_de_pasos(self, nueva_contador_de_pasos:int)->int:
        self.__contador_de_pasos = nueva_contador_de_pasos
        
    def movimiento_aleatorio(self)->None:    
        self.valor_random = rd.randint(1, 4)
        if self.valor_random == 1:
            self.direccion = 'abajo'
        elif self.valor_random == 2:
            self.direccion = 'arriba'
        elif self.valor_random == 3:
            self.direccion = 'derecha'
        elif self.valor_random == 4:
            self.direccion = 'izquierda'
             
        self.cambiar_direccion = 0
        self.valor_random = 0
 
    def mover(self)->None:
        if self.cambiar_direccion >= 6:
            self.movimiento_aleatorio()
        if self.contador_de_pasos >= 5:
            self.generador_de_proyectiles()
            self.contador_de_pasos = 0

        if self.direccion == 'abajo' and not self.chocar('abajo'):
            if (self.y + self.alto) < (64*10) : #EVITA QUE SE VAYA DE LA PANTALLA HACIA ABAJO
                self.y += self.velocidad
        elif self.direccion == 'arriba' and not self.chocar('arriba'):
            if self.y > 40: #EVITA QUE SE VAYA DE LA PANTALLA HACIA ARRIBA
                self.y -= self.velocidad
        elif self.direccion == 'derecha' and not self.chocar('derecha'):
            if (self.x + self.ancho) < (64*16): #EVITA QUE SE VAYA DE LA PANTALLA HACIA LA DERECHA
                self.x += self.velocidad
        elif self.direccion == 'izquierda' and not self.chocar('izquierda'):
            if self.x > 10: #EVITA QUE SE VAYA DE LA PANTALLA HACIA LA IZQUIERDA
                self.x -= self.velocidad

        self.cambiar_direccion += 1
        self.contador_de_pasos += 1
                
    def generador_de_proyectiles(self):
        if len(self.proyectiles) < self.maximo_proyectiles_simultaneos:
            self.proyectiles = Proyectil(self)