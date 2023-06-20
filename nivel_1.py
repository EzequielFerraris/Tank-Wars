import pygame
import sys
import random as rd
from enemigo import Enemigo
from proyectil import Proyectil
from jugador import Jugador
from ladrillo import Ladrillo
from agua import Agua
from muro import Muro
from bosque import Bosque
import acciones
import sonidos

#DISEÑO DE LOS OBSTACULOS DEL NIVEL
def crear_obstaculos(lista_obstaculos:list)->list:
    for obstaculo in range(18):
        ladrillo = Ladrillo(64 * obstaculo, 300)
        lista_obstaculos.append(ladrillo)
        if obstaculo < 3 or (obstaculo > 4 and obstaculo < 8) or (obstaculo > 9 and obstaculo < 13) or (obstaculo > 14):
            ladrillo2 = Ladrillo(64 * obstaculo, 400)
            lista_obstaculos.append(ladrillo2)
        else:
            agua = Agua(64 * obstaculo, 400)
            lista_obstaculos.append(agua)
    
    for obstaculo in range(17):
        muro = Muro(64 * obstaculo, 0)
        lista_obstaculos.append(muro)

    for obstaculo in range(7):
        muro1 = Muro(0, (obstaculo*64))
        muro2 = Muro(17*64, (obstaculo*64))
        lista_obstaculos.append(muro1)
        lista_obstaculos.append(muro2)

    for obstaculo in range(5):
        ladrillo = Ladrillo(7.5*64, 64 * obstaculo)
        ladrillo2 = Ladrillo(9.5*64, 64 * obstaculo)
        lista_obstaculos.append(ladrillo)
        lista_obstaculos.append(ladrillo2)

    for obstaculo in range(6):
        bosque = Bosque(0, obstaculo*64 + 464)
        bosque1 = Bosque(1*64, obstaculo*64 + 464)
        bosque2 = Bosque(2*64, obstaculo*64 + 464)
        bosque3 = Bosque(3*64, obstaculo*64 + 464)
        bosque4= Bosque(4*64, obstaculo*64 + 464)

        lista_obstaculos.append(bosque)
        lista_obstaculos.append(bosque1)
        lista_obstaculos.append(bosque2)
        lista_obstaculos.append(bosque3)
        lista_obstaculos.append(bosque4)
        
        bosque5 = Bosque(13*64, obstaculo*64 + 464)
        bosque6 = Bosque(14*64, obstaculo*64 + 464)
        bosque7 = Bosque(15*64, obstaculo*64 + 464)
        bosque8 = Bosque(16*64, obstaculo*64 + 464)
        bosque9 = Bosque(17*64, obstaculo*64 + 464)
       
        lista_obstaculos.append(bosque5)
        lista_obstaculos.append(bosque6)
        lista_obstaculos.append(bosque7)
        lista_obstaculos.append(bosque8)
        lista_obstaculos.append(bosque9)

#NIVEL
def nivel_1(pantalla_del_juego:object, contador:object)->None:
    #CREO AL JUGADOR Y LOS ENEMIGOS 
    jugador_1 = Jugador(64*8.5, 64*11, 'jugador_1', 'arriba', contador.puntaje) #Crea al jugador
    enemigo_1 = Enemigo(4.5*64, 180, 'enemigo_1', 'abajo')
    enemigo_2 = Enemigo(13.5*64, 180, 'enemigo_2', 'abajo')

    #CREO LOS OBSTACULOS
    lista_obstaculos = []
    crear_obstaculos(lista_obstaculos)

    #LISTAS
    lista_de_enemigos = [enemigo_1, enemigo_2]
    lista_de_objetos_chocables = [enemigo_1, enemigo_2, jugador_1] + lista_obstaculos

    #TIEMPO
    RELOJ = pygame.time.Clock() 
    tiempo_actual = 0
    inicio_del_nivel = 0

    #CONDICION DEL LOOP
    nivel_1 = True

    #LOOP PRINCIPAL
    while nivel_1:
        pygame.time.delay(100) 

        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                nivel_1 = False
                pygame.quit()
                sys.exit()
        
        #TIEMPO DEL JUEGO
        if inicio_del_nivel == 0:
            inicio_del_nivel = pygame.time.get_ticks()

        tiempo_actual = pygame.time.get_ticks()
        tiempo_mostrado = tiempo_actual - inicio_del_nivel
        contador.tiempo = tiempo_mostrado
        
        #MANTENER LAS LISTAS ACTUALIZADAS (PARA LAS COLISIONES)
        for elemento in lista_de_objetos_chocables:
            elemento.lista_otros_objetos = lista_de_objetos_chocables

        #COMPORTAMIENTOS
        acciones.comportamiento_enemigos(lista_de_enemigos) #HACE QUE LOS ENEMIGOS REALICEN SUS ACCIONES
        acciones.comportamiento_jugador(jugador_1) #HACE QUE EL JUGADOR REALICE SUS ACCIONES
        acciones.comportamiento_obstaculos(lista_obstaculos) #OBSTACULOS
        acciones.comportamiento_contador(contador, jugador_1) #SINCRONIZA EL CONTADOR CON EL JUGADOR

        #KEYS
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT] and jugador_1.x > jugador_1.velocidad and not jugador_1.chocar('izquierda'):
            jugador_1.direccion = 'izquierda'
            jugador_1.x -= jugador_1.velocidad
            
        if keys[pygame.K_RIGHT] and jugador_1.x < (64*18) - jugador_1.ancho - jugador_1.velocidad and not jugador_1.chocar('derecha'):
            jugador_1.direccion = 'derecha'
            jugador_1.x += jugador_1.velocidad
            
        if keys[pygame.K_UP] and jugador_1.y > jugador_1.velocidad + 25 and not jugador_1.chocar('arriba'):
            jugador_1.direccion = 'arriba'
            jugador_1.y -= jugador_1.velocidad
            
        if keys[pygame.K_DOWN] and jugador_1.y < (64*13) - jugador_1.alto - jugador_1.velocidad and not jugador_1.chocar('abajo'):
            jugador_1.direccion = 'abajo'
            jugador_1.y += jugador_1.velocidad
        
        if keys[pygame.K_SPACE] and len(jugador_1.proyectiles) < jugador_1.maximo_proyectiles_simultaneos: 
            jugador_1.proyectiles = Proyectil(jugador_1)
            sonidos.disparo_p1.play()
            

    
        #DIBUJAR PANTALLA Y OBJETOS
        acciones.dibujar(pantalla_del_juego, jugador_1, lista_de_enemigos, contador, lista_obstaculos)
       

        RELOJ.tick(60)

        #CHEQUEA CONDICIONES DE TERMINACION DEL JUEGO
        nivel_1 = acciones.chequeo_final(jugador_1, lista_de_enemigos, pantalla_del_juego, contador) 
