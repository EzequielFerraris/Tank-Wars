import pygame

class Obstaculo(): #CLASE 1
    def __init__(self, x, y, nombre)->None:

        #NOMBRE Y COORDENADAS
        self.__nombre = nombre
        self.__tipo = 'obstaculo'
        self.__x = x 
        self.__y = y 
        self.__ancho = 64
        self.__alto = 64
        self.__rect_principal = pygame.Rect(self.x-2, self.y-2, 68, 68) 

        #IMAGENES:
        self.__imagen_mostrada = ''

        #VIDAS, PUNTAJE
        self.__vidas = 3
        self.__visible = 1

    @property
    def nombre(self)->str:
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre:str)->None:
        self.__nombre = nuevo_nombre

    @property
    def tipo(self)->str:
        return self.__tipo

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
    def ancho(self)->int:
        return self.__ancho

    @ancho.setter
    def ancho(self, nuevo_ancho:int)->None:
        self.__ancho = nuevo_ancho

    @property
    def alto(self)->int:
        return self.__alto

    @alto.setter
    def alto(self, nuevo_alto:int)->None:
        self.__alto = nuevo_alto

    @property
    def vidas(self)->int:
        return self.__vidas
    
    @vidas.setter
    def vidas(self, nuevas_vidas:int)->None:
        self.__vidas = nuevas_vidas

    @property
    def visible(self)->int:
        return self.__visible

    @visible.setter
    def visible(self, nuevo_visible:int)->int:
        self.__visible = nuevo_visible

    #RECTANGULOS -------------------
    @property
    def rect_principal(self)->object:
        return self.__rect_principal

    @rect_principal.setter
    def rect_principal(self, nuevo_rect_principal:object)->None:
        self.__rect_principal = nuevo_rect_principal

    #IMAGENES -----            
    @property
    def imagen_mostrada(self):
        return self.__imagen_mostrada

    @imagen_mostrada.setter
    def imagen_mostrada(self, nueva_imagen_mostrada)->None:
        self.__imagen_mostrada = nueva_imagen_mostrada
    
    #METODOS ------------------
    #DIBUJA EL OBSTACULO
    def dibujar(self, pantalla): 
        pantalla.blit(self.imagen_mostrada, (self.x, self.y))

    #ALCANZADO POR UN PROYECTIL
    def recibir_impacto(self):
        if self.nombre != 'muro':    
            self.vidas -= 1
            if self.vidas == 0:
                self.visible = 0