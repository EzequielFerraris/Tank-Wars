import pygame

COLOR_BALAS_AMARILLO_POR_DEFECTO = (255,255,0)
COLOR_BALAS_BLANCAS = (255,255,255)

class Proyectil():
        
    def __init__(self, tanque:object, color=COLOR_BALAS_AMARILLO_POR_DEFECTO, radio=6, velocidad=15):

        self.__visible = 1
        self.__color = color
        self.__radio = radio 
        
        #SETTEANDO LA POSICION DE LA BALA Y SU DIRECCION
        self.__direccion = tanque.direccion 

        if self.direccion == 'arriba' or self.direccion == 'abajo':
            self.__eje = 'y'
            self.__x = round(tanque.x + tanque.ancho // 2) #HACE QUE LA BALA SALGA DE LA MITAD DEL TANQUE
            if self.direccion == 'arriba':
                self.__y = tanque.y
            else:
                self.__y = round(tanque.y + tanque.alto)
        else:
            self.__eje = 'x'
            self.__y = round(tanque.y) + tanque.alto // 2
            if self.direccion == 'izquierda':
                self.__x = round(tanque.x)
            else:
                self.__x = tanque.x + tanque.ancho

        if self.direccion == 'arriba' or self.direccion == 'izquierda':
            self.__velocidad = velocidad * -1
        else:
            self.__velocidad = velocidad 

        self.__rect = pygame.Rect(self.x, self.y, self.radio * 2, self.radio * 2)

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

    @property
    def radio(self)->int:
        return self.__radio

    @radio.setter
    def radio(self, nueva_radio:int)->None:
        self.__radio = nueva_radio

    @property
    def rect(self)->object:
        return self.__rect

    @rect.setter
    def rect(self, nuevo_rect:int)->None:
        self.__rect = nuevo_rect

    @property
    def color(self)->tuple:
        return self.__color

    @color.setter
    def color(self, nuevo_color:tuple)->None:
        self.__color = nuevo_color
    
    @property
    def direccion(self)->str:
        return self.__direccion

    @property
    def eje(self)->str:
        return self.__eje

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

    #METODOS
    def dibujar(self, pantalla): #DIBUJA EL PROYECTIL
        if self.visible > 0:
            pygame.draw.circle(pantalla, self.color, (self.x, self.y), self.radio)
            self.rect = pygame.Rect(self.x - self.radio, self.y - self.radio, self.radio * 2, self.radio * 2)
            #pygame.draw.rect(pantalla, (255,0,0), self.rect, 2)