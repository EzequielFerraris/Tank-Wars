import pygame
from proyectil import Proyectil

class Super_proyectil(Proyectil):
    def __init__(self, tanque:object, velocidad:int, numero:int):
        super().__init__(tanque, velocidad)
        self.__numero = numero
        self.imagen = pygame.image.load("Imagenes/Balas/bala_azul.png").convert_alpha()
        self.imagen_arriba = pygame.image.load("Imagenes/Balas/bala_azul.png").convert_alpha()
        self.imagen_abajo = pygame.transform.rotate(self.imagen, 180)
        self.imagen_derecha = pygame.transform.rotate(self.imagen, 270)
        self.imagen_izquierda = pygame.transform.rotate(self.imagen, 90)
        self.velocidad = tanque.velocidad

        #X Y DE LA IMAGEN
        if self.direccion == 'arriba' or self.direccion == 'abajo':
            self.eje = 'y'
            if self.numero == 1:
                self.x = tanque.x+41
            elif self.numero == 2:
                self.x = tanque.x + 64+34
            else:
                self.x = tanque.x + 128+20

            if self.direccion == 'arriba':
                if self.numero == 2:
                    self.y = tanque.y-2
                else:
                    self.y = tanque.y 
            else:
                if self.numero == 2:
                    self.y = round(tanque.y + tanque.alto -32)
                else:
                    self.y = round(tanque.y + tanque.alto -36)

        else:
            self.eje = 'x'
            if self.numero == 1:
                self.y = tanque.y+42
            elif self.numero == 2:
                self.y = tanque.y+33+64
            else:
                self.y = tanque.y +20+ 128
            
            if self.direccion == 'izquierda':
                if self.numero == 2:
                    self.x = tanque.x
                else:
                    self.x = tanque.x +4
            else:
                if self.numero == 2:
                    self.x = tanque.x + tanque.alto - 32
                else:
                    self.x = tanque.x + tanque.alto - 36

        if self.direccion == 'arriba' or self.direccion == 'izquierda':
            self.velocidad = velocidad * -1
        else:
            self.velocidad = velocidad 
        
        ###### RECTANGULO PARA COLISIONES
        self.x_rect = self.x + 26
        self.y_rect = self.y + 26
            

        self.rect = pygame.Rect(self.x_rect, self.y_rect, 12, 12)

    #GETTERS Y SETTER

    @property
    def numero(self)->int:
        return self.__numero
    


