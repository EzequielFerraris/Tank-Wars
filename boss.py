import pygame
import sonidos
import random as rd
from super_proyectil import Super_proyectil

class Boss():
    def __init__(self, x, y, nombre, direccion_original)->None:

        #NOMBRE Y COORDENADAS
        self.__nombre = nombre
        self.__tipo = 'boss'
        self.__x = x 
        self.__y = y 
        self.__ancho = 186
        self.__alto = 255
        self.__velocidad = 10
        self.__direccion = direccion_original
        self.__valor_random = 0
        self.__cambiar_direccion = 0
        self.__contador_de_pasos = 0

        #COLISIONES
        self.__lista_otros_objetos = []

        #IMAGENES:
        self.__imagen_mostrada = pygame.image.load('Imagenes/Boss/Boss_abajo.png').convert_alpha()

        self.__imagen_arriba = pygame.image.load('Imagenes/Boss/Boss_arriba.png').convert_alpha()
        self.__imagen_abajo = pygame.image.load('Imagenes/Boss/Boss_abajo.png').convert_alpha()
        self.__imagen_derecha = pygame.image.load('Imagenes/Boss/Boss_derecha.png').convert_alpha()
        self.__imagen_izquierda = pygame.image.load('Imagenes/Boss/Boss_izquierda.png').convert_alpha()

        #RECTANGULOS
        self.__rect_principal = pygame.Rect(self.x+36, self.y, self.ancho, self.alto)                    
        self.__rect_arriba = pygame.Rect(self.x + 36, self.y, self.ancho, 1)
        self.__rect_abajo = pygame.Rect(self.x+36, self.y+self.alto, self.ancho, 1)
        self.__rect_derecha = pygame.Rect(self.x + self.alto, self.y+36, 1, self.alto)
        self.__rect_izquierda = pygame.Rect(self.x, self.y+36, 1, self.ancho)

        #VIDAS, PUNTAJE
        self.__vidas = 10
        self.__visible = 1

        #PROYECTILES
        self.__maximo_proyectiles_simultaneos = 100
        self.__proyectiles = []
    
        #EXPLOSION
        self.__contador = 0 
        self.__indice = 0
        self.__explosion = []
        self.__imagenes_explosion =["Imagenes/Explosion_tanque/exp_1.png", "Imagenes/Explosion_tanque/exp_2.png", "Imagenes/Explosion_tanque/exp_3.png", "Imagenes/Explosion_tanque/exp_4.png", "Imagenes/Explosion_tanque/exp_5.png"]
        
        for imagen in self.imagenes_explosion:
            nueva_imagen = pygame.image.load(imagen).convert_alpha()
            nueva_imagen = pygame.transform.scale(nueva_imagen, (256, 256))
            self.explosion.append(nueva_imagen)

    #SETTERS Y GETTERS
    #NOMBRE Y COORDENADAS
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
    def direccion(self)->str:
        return self.__direccion

    @direccion.setter
    def direccion(self, nueva_direccion:str)->None:
        self.__direccion = nueva_direccion
        
    @property
    def velocidad(self)->int:
        return self.__velocidad
    
    @velocidad.setter
    def velocidad(self, nueva_velocidad:int)->None:
        self.__velocidad = nueva_velocidad

    #VIDAS
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

    #MOVIMIENTO ----------------------
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
        

    #COLISIONES ----------------------
    @property
    def lista_otros_objetos(self)->list:
        return self.__lista_otros_objetos

    @lista_otros_objetos.setter
    def lista_otros_objetos(self, lista:list)->None:
        for elemento in lista:
            if elemento.nombre != self.nombre and elemento not in self.lista_otros_objetos:
                self.lista_otros_objetos.append(elemento)

    #PROYECTILES -------------------
    
    @property
    def proyectiles(self)->list:
        return self.__proyectiles

    @proyectiles.setter
    def proyectiles(self, proyectil:object)->None:
        self.proyectiles.append(proyectil)

    @property
    def maximo_proyectiles_simultaneos(self)->int:
        return self.__maximo_proyectiles_simultaneos

    @maximo_proyectiles_simultaneos.setter
    def maximo_proyectiles_simultaneos(self, nueva_maximo_proyectiles_simultaneos:int)->None:
        self.__maximo_proyectiles_simultaneos = nueva_maximo_proyectiles_simultaneos

    #RECTANGULOS -------------------
    @property
    def rect_principal(self)->object:
        return self.__rect_principal

    @rect_principal.setter
    def rect_principal(self, nuevo_rect_principal:object)->None:
        self.__rect_principal = nuevo_rect_principal
    
    @property
    def rect_arriba(self)->object:
        return self.__rect_arriba

    @rect_arriba.setter
    def rect_arriba(self, nuevo_rect_arriba:object)->None:
        self.__rect_arriba = nuevo_rect_arriba
        
    @property
    def rect_abajo(self)->object:
        return self.__rect_abajo

    @rect_abajo.setter
    def rect_abajo(self, nuevo_rect_abajo:object)->None:
        self.__rect_abajo = nuevo_rect_abajo

    @property
    def rect_derecha(self)->object:
        return self.__rect_derecha

    @rect_derecha.setter
    def rect_derecha(self, nuevo_rect_derecha:object)->None:
        self.__rect_derecha = nuevo_rect_derecha

    @property
    def rect_izquierda(self)->object:
        return self.__rect_izquierda

    @rect_izquierda.setter
    def rect_izquierda(self, nuevo_rect_izquierda:object)->None:
        self.__rect_izquierda = nuevo_rect_izquierda

    #IMAGENES -----            
    @property
    def imagen_mostrada(self):
        return self.__imagen_mostrada

    @imagen_mostrada.setter
    def imagen_mostrada(self, nueva_imagen_mostrada)->None:
        self.__imagen_mostrada = nueva_imagen_mostrada

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
    #DIBUJA EL TANQUE
    def dibujar(self, pantalla):
        #SI LAS VIDAS SON MAYORES A 0, DIBUJA EL TANQUE Y ACTUALIZA EL RECTANGULO
        if self.vidas > 0: 
            if self.direccion == 'arriba':
                self.imagen_mostrada = self.imagen_arriba
            elif self.direccion == 'abajo':
                self.imagen_mostrada = self.imagen_abajo
            elif self.direccion == 'derecha':
                self.imagen_mostrada = self.imagen_derecha
            elif self.direccion == 'izquierda':
                self.imagen_mostrada = self.imagen_izquierda

            pantalla.blit(self.imagen_mostrada, (self.x, self.y))
            
            #MARCA Y CREA EL AREA DONDE PUEDE SER ATACADO
            if self.direccion == 'arriba' or self.direccion == 'abajo':

                self.rect_principal = pygame.Rect(self.x+36, self.y, self.ancho, self.alto) 
                #pygame.draw.rect(pantalla, (255,0,0), self.rect_principal, 2)                    
                self.rect_arriba = pygame.Rect(self.x + 36, self.y, self.ancho, 1)
                #pygame.draw.rect(pantalla, (255,0,0), self.rect_arriba, 2)
                self.rect_abajo = pygame.Rect(self.x+36, self.y+self.alto, self.ancho, 1)
                #pygame.draw.rect(pantalla, (255,0,0), self.rect_abajo, 2)
                self.rect_derecha = pygame.Rect(self.x+self.ancho+36, self.y, 1, self.alto)
                #pygame.draw.rect(pantalla, (255,0,0), self.rect_derecha, 2)
                self.rect_izquierda = pygame.Rect(self.x+36, self.y, 1, self.alto)
                #pygame.draw.rect(pantalla, (255,0,0), self.rect_izquierda, 2)      

            else:
                self.rect_principal = pygame.Rect(self.x, self.y+36, self.alto, self.ancho) 
                #pygame.draw.rect(pantalla, (255,0,0), self.rect_principal, 2)
                self.rect_arriba = pygame.Rect(self.x, self.y + 36, self.alto, 1)
                #pygame.draw.rect(pantalla, (255,0,0), self.rect_arriba, 2)
                self.rect_abajo = pygame.Rect(self.x, self.y+36+ self.ancho, self.alto, 1)
                #pygame.draw.rect(pantalla, (255,0,0), self.rect_abajo, 2)
                self.rect_derecha = pygame.Rect(self.x + self.alto, self.y+36, 1, self.__ancho)
                #pygame.draw.rect(pantalla, (255,0,0), self.rect_derecha, 2)
                self.rect_izquierda = pygame.Rect(self.x, self.y+36, 1, self.ancho)
                #pygame.draw.rect(pantalla, (255,0,0), self.rect_izquierda, 2)
        #SI LAS VIDAS SON MENORES A 0, EXPLOSION        
        else:
            sonidos.explosion_tanque.play()
            sonidos.explosion_tanque.set_volume(0.2)
            velocidad_explosion = 1
            self.contador += 1
            if self.contador >= velocidad_explosion and self.indice < len(self.explosion) - 1:
                self.contador = 0
                self.indice += 1
                self.imagen_mostrada = self.explosion[self.indice]
                pantalla.blit(self.imagen_mostrada, (self.x, self.y))
            if self.indice >= len(self.explosion) - 1 and self.contador >= velocidad_explosion:
                self.visible = 0

    #CHEQUEA SI CHOCA
    def chocar(self, direccion:str)->bool:
        for elemento in self.lista_otros_objetos:
            if elemento.visible != 0:
                if direccion == 'arriba':
                    if self.rect_arriba.colliderect(elemento.rect_principal):
                        return True
                elif direccion == 'abajo':
                    if self.rect_abajo.colliderect(elemento.rect_principal):
                        return True
                elif direccion == 'derecha':
                    if self.rect_derecha.colliderect(elemento.rect_principal):
                        return True
                elif direccion == 'izquierda':
                    if self.rect_izquierda.colliderect(elemento.rect_principal):
                        return True
        return False
    
    #ALCANZADO POR UN PROYECTIL
    def recibir_impacto(self):
        self.vidas -= 1
        if self.vidas < 1:
            self.rect_principal = pygame.Rect(self.x + 10, self.y, 0, 0)
        else:
            sonidos.impacto_tanque.play()

    #DISPARAR
    def disparar(self):

        for proyectil in self.proyectiles: 
            for elemento in self.lista_otros_objetos:
                if elemento.nombre != 'agua' and elemento.visible == 1 and proyectil.rect.colliderect(elemento.rect_principal):
                    elemento.recibir_impacto()
                    if proyectil in self.proyectiles:
                        self.proyectiles.pop(self.proyectiles.index(proyectil))    
       
            if proyectil.eje == 'x':
                if proyectil.x_rect < (64*18) and proyectil.x_rect > 0:
                    proyectil.x_rect += proyectil.velocidad
                    proyectil.x += proyectil.velocidad  #MUEVE EL PROYECTIL A SU VELOCIDAD EN EL EJE X
                else:
                    self.proyectiles.pop(self.proyectiles.index(proyectil))  #LO REMUEVE SI SALE DE LA PANTALLA
            else:
                if proyectil.y_rect < (64*13) and proyectil.y_rect > 0:
                    proyectil.y_rect += proyectil.velocidad  #MUEVE EL PROYECTIL A SU VELOCIDAD EN EL EJE Y
                    proyectil.y += proyectil.velocidad 
                else:
                    self.proyectiles.pop(self.proyectiles.index(proyectil))  #LO REMUEVE SI SALE DE LA PANTALLA
    
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
        if self.vidas > 0:
            if self.cambiar_direccion > 5:
                self.movimiento_aleatorio()
            if self.contador_de_pasos > 6:
                self.generador_de_proyectiles()
                self.contador_de_pasos = 0

            if self.direccion == 'abajo' and not self.chocar('abajo'):
                if (self.y + self.alto) < (64*13) : #EVITA QUE SE VAYA DE LA PANTALLA HACIA ABAJO
                    self.y += self.velocidad
            elif self.direccion == 'arriba' and not self.chocar('arriba'):
                if self.y > 20: #EVITA QUE SE VAYA DE LA PANTALLA HACIA ARRIBA
                    self.y -= self.velocidad
            elif self.direccion == 'derecha' and not self.chocar('derecha'):
                if (self.x + self.alto) < (64*18): #EVITA QUE SE VAYA DE LA PANTALLA HACIA LA DERECHA
                    self.x += self.velocidad
            elif self.direccion == 'izquierda' and not self.chocar('izquierda'):
                if self.x > 15: #EVITA QUE SE VAYA DE LA PANTALLA HACIA LA IZQUIERDA
                    self.x -= self.velocidad

            self.cambiar_direccion += 1
            self.contador_de_pasos += 1
              
    def generador_de_proyectiles(self):
        if self.vidas > 0 and len(self.proyectiles) < self.maximo_proyectiles_simultaneos:
            #sonidos.disparo_enemigo.play()
            #sonidos.disparo_enemigo.set_volume(0.0078)
            self.proyectiles = Super_proyectil(self, 30, 1)
            self.proyectiles = Super_proyectil(self, 35 , 2)
            self.proyectiles = Super_proyectil(self, 30, 3)