import pygame

class Contador():
    def __init__(self, vidas:int, puntaje:int, nombre:str, tiempo:int)->None:
        self.__x= 0
        self.__y= 0
        self.__nombre = nombre
        self.__fuente_amarillo= tuple((255,255,0))
        self.__fuente_rojo= tuple((255,0,0))
        self.__fondo_color= tuple((51,51,51))
        self.__rect= pygame.Rect(0, 0, 17*64, 21)
        self.__vidas = 0 + vidas
        self.__puntaje = puntaje
        self.__fuente = pygame.font.SysFont("Arial", 17, True)

    @property
    def vidas(self)->object:
        return self.__vidas
    
    @vidas.setter
    def vidas(self, nuevas_vidas)->None:
        self.__vidas = nuevas_vidas

    @property
    def puntaje(self)->object:
        return self.__puntaje
    
    @puntaje.setter
    def puntaje(self, nuevo_puntaje)->None:
        self.__puntaje = nuevo_puntaje

    @property
    def nombre(self)->str:
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre)->None:
        self.__nombre = nuevo_nombre

    @property
    def rect(self)->object:
        return self.__rect
    
    @property
    def fondo_color(self)->object:
        return self.__fondo_color
    
    @property
    def fuente_amarillo(self)->object:
        return self.__fuente_amarillo
    
    @property
    def fuente_rojo(self)->object:
        return self.__fuente_rojo

    @property
    def fuente(self)->object:
        return self.__fuente
    
    def dibujar(self, pantalla:object)->None:
        pygame.draw.rect(pantalla, self.__fondo_color, self.rect)
        nombre = self.fuente.render(f'{self.nombre}', 1, self.fuente_rojo)
        vidas_y_puntos = self.fuente.render(f'Vidas: {self.vidas}   Puntos: {self.puntaje}', 1, self.fuente_amarillo)
        pantalla.blit(vidas_y_puntos, (900, 1))
        pantalla.blit(nombre, (10, 1))
        