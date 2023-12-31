import pygame

class Contador():
    def __init__(self, vidas:int, puntaje:int, nombre:str, tiempo_maximo:int=300)->None:
        self.__x= 0
        self.__y= 0
        self.__nombre = nombre
        self.__tiempo_maximo = tiempo_maximo
        self.__tiempo = 0
        self.__nivel = 1
        self.__fuente_amarillo= tuple((255,255,0))
        self.__fuente_rojo= tuple((255,0,0))
        self.__fondo_color= tuple((51,51,51))
        self.__rect= pygame.Rect(0, 0, 18*64, 23)
        self.__vidas = 0 + vidas
        self.__puntaje = puntaje
        self.__fuente = pygame.font.Font("Fonts/Trade Gothic LT Bold Condensed No. 20.ttf", 20)
        self.__spawneo = 1

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
    def nivel(self)->object:
        return self.__nivel
    
    @nivel.setter
    def nivel(self, nuevo_nivel)->None:
        self.__nivel = nuevo_nivel

    @property
    def tiempo_maximo(self)->object:
        return self.__tiempo_maximo

    @tiempo_maximo.setter
    def tiempo_maximo(self, nuevo_maximo:float)->None:
        self.__tiempo_maximo = nuevo_maximo

    @property
    def tiempo(self)->object:
        return self.__tiempo
    
    @tiempo.setter
    def tiempo(self, nuevo_tiempo:int)->None:
        nuevo_tiempo = nuevo_tiempo // 1000
        nuevo_tiempo = self.tiempo_maximo - nuevo_tiempo 
        self.__tiempo = nuevo_tiempo
        
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
    
    @property
    def spawneo(self)->object:
        return self.__spawneo
    
    @spawneo.setter
    def spawneo(self, nuevo_spawneo)->None:
        self.__spawneo = nuevo_spawneo

    def dibujar(self, pantalla:object)->None:
        #FONDO DEL CONTADOR        
        pygame.draw.rect(pantalla, self.__fondo_color, self.rect)
        #NOMBRE DEL JUGADOR
        nombre = self.fuente.render(f'{self.nombre}', 1, self.fuente_rojo)
        #VIDAS Y PUNTOS
        vidas_y_puntos = self.fuente.render(f'Lives: {self.vidas}   Score: {self.puntaje}', 1, self.fuente_amarillo)
        #TIEMPO RESTANTE. ROJO SI QUEDA MENOS DE UN MINUTO
        if self.tiempo > 60:
            tiempo = self.fuente.render(f'Time left: {str(self.tiempo//60)}:{str(self.tiempo%60).zfill(2)}', 1, self.fuente_amarillo)
        else:
            tiempo = self.fuente.render(f'Time left: {self.tiempo}', 1, self.fuente_rojo)
        #FUSIONAMOS CON EL FONDO
        pantalla.blit(vidas_y_puntos, (950, 1))
        pantalla.blit(nombre, (10, 1))
        pantalla.blit(tiempo, (64*9 - (tiempo.get_width()/2), 1))
    
        
            
        