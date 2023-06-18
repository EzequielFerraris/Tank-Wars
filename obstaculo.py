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

        #EXPLOSION
        self.__contador = 0 
        self.__indice = 0
        self.__explosion = []
        self.__imagenes_explosion =["Imagenes/Explosion_obstaculo/Explosion_A.png", "Imagenes/Explosion_obstaculo/Explosion_B.png", "Imagenes/Explosion_obstaculo/Explosion_C.png", "Imagenes/Explosion_obstaculo/Explosion_D.png", "Imagenes/Explosion_obstaculo/Explosion_E.png", "Imagenes/Explosion_obstaculo/Explosion_F.png", "Imagenes/Explosion_obstaculo/Explosion_G.png", "Imagenes/Explosion_obstaculo/Explosion_H.png"]
        
        for imagen in self.imagenes_explosion:
            nueva_imagen = pygame.image.load(imagen).convert_alpha()
            nueva_imagen = pygame.transform.scale(nueva_imagen, (64,64))
            self.explosion.append(nueva_imagen)

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
    
    #EXPLOSIONES
    @property
    def contador(self)->int:
        return self.__contador

    @contador.setter
    def contador(self, nuevo_contador:int)->None:
        self.__contador = nuevo_contador

    @property
    def indice(self)->int:
        return self.__indice

    @indice.setter
    def indice(self, nuevo_indice:int)->None:
        self.__indice = nuevo_indice

    @property
    def explosion(self)->int:
        return self.__explosion

    @explosion.setter
    def explosion(self, nueva_explosion:int)->None:
        self.__explosion = nueva_explosion

    @property
    def imagenes_explosion(self)->int:
        return self.__imagenes_explosion
 
    #METODOS ------------------
    #DIBUJA EL OBSTACULO
    def dibujar(self, pantalla): 
        if self.vidas > 0:
            pantalla.blit(self.imagen_mostrada, (self.x, self.y))
        else:
            velocidad_explosion = 1
            self.contador += 1
            if self.contador >= velocidad_explosion and self.indice < len(self.explosion) - 1:
                self.contador = 0
                self.indice += 1
                self.imagen_mostrada = self.explosion[self.indice]
                pantalla.blit(self.imagen_mostrada, (self.x, self.y))
            if self.indice >= len(self.explosion) - 1 and self.contador >= velocidad_explosion:
                self.visible = 0
    
    #ALCANZADO POR UN PROYECTIL
    def recibir_impacto(self):
        if self.nombre != 'muro':    
            self.vidas -= 1
                


