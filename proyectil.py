import pygame

class Proyectil():
        
    def __init__(self, tanque:object, velocidad=17):

        self.__visible = 1
        self.__ancho = 64
        self.__alto = 64
        self.__imagen = pygame.image.load("Imagenes/Balas/Exhaust_Fire.png").convert_alpha()
        self.__imagen_arriba = pygame.image.load("Imagenes/Balas/Exhaust_Fire.png").convert_alpha()
        self.__imagen_abajo = pygame.transform.rotate(self.imagen, 180)
        self.__imagen_derecha = pygame.transform.rotate(self.imagen, 270)
        self.__imagen_izquierda = pygame.transform.rotate(self.imagen, 90)

        #SETTEANDO LA POSICION DE LA BALA Y SU DIRECCION
        self.__direccion = tanque.direccion 
        #X Y DE LA IMAGEN
        if self.direccion == 'arriba' or self.direccion == 'abajo':
            self.__eje = 'y'
            self.__x = tanque.x 
            if self.direccion == 'arriba':
                self.__y = tanque.y - 32
            else:
                self.__y = round(tanque.y + 32)
        else:
            self.__eje = 'x'
            self.__y = tanque.y
            if self.direccion == 'izquierda':
                self.__x = tanque.x -32
            else:
                self.__x = tanque.x + 32

        if self.direccion == 'arriba' or self.direccion == 'izquierda':
            self.__velocidad = velocidad * -1
        else:
            self.__velocidad = velocidad 

        ###### RECTANGULO PARA COLISIONES
        self.__x_rect = self.x + 26
        self.__y_rect = self.y + 26
            

        self.__rect = pygame.Rect(self.x_rect, self.y_rect, 12, 12)
        
    #SETTERS Y GETTERS
    @property
    def x(self)->int:
        return self.__x

    @x.setter
    def x(self, nueva_x:int)->None:
        self.__x = nueva_x

    @property
    def y(self)->int:
        return self.__y

    @y.setter
    def y(self, nueva_y:int)->None:
        self.__y = nueva_y
        
    ########
    @property
    def x_rect(self)->int:
        return self.__x_rect

    @x_rect.setter
    def x_rect(self, nueva_x_rect:int)->None:
        self.__x_rect = nueva_x_rect

    @property
    def y_rect(self)->int:
        return self.__y_rect

    @y_rect.setter
    def y_rect(self, nueva_y_rect:int)->None:
        self.__y_rect = nueva_y_rect

    ########
    @property
    def rect(self)->object:
        return self.__rect

    @rect.setter
    def rect(self, nuevo_rect:int)->None:
        self.__rect = nuevo_rect
    
    @property
    def ancho(self)->tuple:
        return self.__ancho

    @ancho.setter
    def ancho(self, nuevo_ancho:tuple)->None:
        self.__ancho = nuevo_ancho

    @property
    def alto(self)->tuple:
        return self.__alto

    @alto.setter
    def alto(self, nuevo_alto:tuple)->None:
        self.__alto = nuevo_alto
        
    @property
    def direccion(self)->str:
        return self.__direccion

    @property
    def eje(self)->str:
        return self.__eje
    
    @eje.setter
    def eje(self, nuevo_eje):
        self.__eje = nuevo_eje


    @property
    def velocidad(self)->int:
        return self.__velocidad

    @velocidad.setter
    def velocidad(self, nueva_velocidad:int)->None:
        self.__velocidad = nueva_velocidad

    @property
    def visible(self)->int:
        return self.__visible

    @visible.setter
    def visible(self, nuevo_visible:int)->None:
        self.__visible = nuevo_visible

    @property
    def imagen(self)->int:
        return self.__imagen
    
    @imagen.setter
    def imagen(self, nueva_imagen:int)->None:
        self.__imagen = nueva_imagen
    
    ###### IMAGENES
    @property
    def imagen_arriba(self):
        return self.__imagen_arriba

    @imagen_arriba.setter
    def imagen_arriba(self, nueva_imagen_arriba)->None:
        self.__imagen_arriba = nueva_imagen_arriba

    @property
    def imagen_abajo(self):
        return self.__imagen_abajo

    @imagen_abajo.setter
    def imagen_abajo(self, nueva_imagen_abajo)->None:
        self.__imagen_abajo = nueva_imagen_abajo

    @property
    def imagen_derecha(self):
        return self.__imagen_derecha

    @imagen_derecha.setter
    def imagen_derecha(self, nueva_imagen_derecha)->None:
        self.__imagen_derecha = nueva_imagen_derecha

    @property
    def imagen_izquierda(self):
        return self.__imagen_izquierda

    @imagen_izquierda.setter
    def imagen_izquierda(self, nueva_imagen_izquierda)->None:
        self.__imagen_izquierda = nueva_imagen_izquierda

    ######

    #METODOS
    def dibujar(self, pantalla): #DIBUJA EL PROYECTIL
        if self.visible > 0:
            if self.direccion == 'abajo':
                self.imagen = self.imagen_abajo
            elif self.direccion == 'derecha':
                self.imagen = self.imagen_derecha
            elif self.direccion == 'izquierda':
                self.imagen = self.imagen_izquierda
            else:
                self.imagen_arriba

            self.imagen = pygame.transform.scale(self.imagen, (self.ancho,self.alto))

            pantalla.blit(self.imagen, (self.x, self.y)) 
            self.rect = pygame.Rect(self.x_rect, self.y_rect, 12, 12)
            #DIBUJA EL RECTANGULO DE LA BALA
            #pygame.draw.rect(pantalla, (255,0,0), self.rect, 2)