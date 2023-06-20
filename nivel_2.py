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
from pantalla_inicio import pantalla_inicio
import acciones
import sonidos

#DISEÑO DE LOS OBSTACULOS DEL NIVEL
def crear_obstaculos(lista_obstaculos:list)->list:
    for obstaculo in range(17):
        ladrillo = Ladrillo(64 * obstaculo, 300)
        lista_obstaculos.append(ladrillo)

    for obstaculo in range(18):
        ladrillo = Ladrillo(64 * obstaculo, 300)
        lista_obstaculos.append(ladrillo)
        if obstaculo < 3 or (obstaculo > 4 and obstaculo < 7) or (obstaculo > 10 and obstaculo < 13) or (obstaculo > 14):
            ladrillo2 = Ladrillo(64 * obstaculo, 400)
            lista_obstaculos.append(ladrillo2)
        else:
            agua = Agua(64 * obstaculo, 400)
            lista_obstaculos.append(agua)
    
    for obstaculo in range(5):
        if obstaculo != 2 and obstaculo !=3:
            ladrillo = Ladrillo(5*64, 64 * obstaculo)
            ladrillo2 = Ladrillo(12*64, 64 * obstaculo)
            lista_obstaculos.append(ladrillo)
            lista_obstaculos.append(ladrillo2)
        else: 
            muro = Muro(5*64, 64 * obstaculo)
            muro2 = Muro(12*64, 64 * obstaculo)
            lista_obstaculos.append(muro)
            lista_obstaculos.append(muro2)

    for obstaculo in range(4):
        bosque = Bosque(0, obstaculo*64)
        bosque1 = Bosque(1*64, obstaculo*64)
        bosque2 = Bosque(2*64, obstaculo*64)
        bosque3 = Bosque(3*64, obstaculo*64)
        lista_obstaculos.append(bosque)
        lista_obstaculos.append(bosque1)
        lista_obstaculos.append(bosque2)
        lista_obstaculos.append(bosque3)
        bosque4 = Bosque(14*64, obstaculo*64)
        bosque5 = Bosque(15*64, obstaculo*64)
        bosque6 = Bosque(16*64, obstaculo*64)
        bosque7 = Bosque(17*64, obstaculo*64)
        lista_obstaculos.append(bosque4)
        lista_obstaculos.append(bosque5)
        lista_obstaculos.append(bosque6)
        lista_obstaculos.append(bosque7)

    for obstaculo in range(6):
        ladrillo = Ladrillo(0*64, obstaculo*64 + 464)
        agua1 = Agua(1*64, obstaculo*64 + 464)
        agua2 = Agua(2*64, obstaculo*64 + 464)
        ladrillo3 = Ladrillo(3*64, obstaculo*64 + 464)
        ladrillo4 = Ladrillo(4*64, obstaculo*64 + 464)

        lista_obstaculos.append(ladrillo)
        lista_obstaculos.append(agua1)
        lista_obstaculos.append(agua2)
        lista_obstaculos.append(ladrillo3)
        lista_obstaculos.append(ladrillo4)
        
        ladrillo5 = Ladrillo(13*64, obstaculo*64 + 464)
        ladrillo6 = Ladrillo(14*64, obstaculo*64 + 464)
        agua7 = Agua(15*64, obstaculo*64 + 464)
        agua8 = Agua(16*64, obstaculo*64 + 464)
        ladrillo9 = Ladrillo(17*64, obstaculo*64 + 464)
       
        lista_obstaculos.append(ladrillo5)
        lista_obstaculos.append(ladrillo6)
        lista_obstaculos.append(agua7)
        lista_obstaculos.append(agua8)
        lista_obstaculos.append(ladrillo9)

    for obstaculo in range(6):
        agua = Agua(64 * 4, 64*(9+obstaculo))
        agua2 = Agua(64 * 13, 64*(9+obstaculo))
        lista_obstaculos.append(agua)
        lista_obstaculos.append(agua2)


def nivel_2(pantalla_del_juego:object, contador:object)->None:
    #CREO AL JUGADOR, LOS ENEMIGOS Y LA FUENTE DEL REGISTRO DE VIDAS Y PUNTOS
    jugador_1 = Jugador(64*8.5, 64*11, 'jugador_1', 'arriba', contador.puntaje) #Crea al jugador
    enemigo_1 = Enemigo(2*64, 180, 'enemigo_1', 'abajo', 18)
    enemigo_2 = Enemigo(9*64, 180, 'enemigo_2', 'abajo', 18)
    enemigo_3 = Enemigo(15*64, 180, 'enemigo_3', 'abajo', 18)

    #CREO LOS OBSTACULOS
    lista_obstaculos = []
    crear_obstaculos(lista_obstaculos)

    #LISTAS  
    lista_de_enemigos = [enemigo_1, enemigo_2, enemigo_3]
    lista_de_objetos_chocables = [enemigo_1, enemigo_2, enemigo_3, jugador_1] + lista_obstaculos

    #TIEMPO
    RELOJ = pygame.time.Clock() 
    tiempo_actual = 0
    inicio_del_nivel = 0

    #CONDICION DEL LOOP
    nivel_2 = True

    #LOOP PRINCIPAL
    while nivel_2:
        pygame.time.delay(100) 

        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                nivel_2 = False
                pygame.quit()
                sys.exit()

        #TIEMPO DEL JUEGO
        if inicio_del_nivel == 0:
            inicio_del_nivel = pygame.time.get_ticks()

        tiempo_actual = pygame.time.get_ticks()
        tiempo_mostrado = tiempo_actual - inicio_del_nivel
        contador.tiempo = tiempo_mostrado

        for elemento in lista_de_objetos_chocables:
            elemento.lista_otros_objetos = lista_de_objetos_chocables

        acciones.comportamiento_enemigos(lista_de_enemigos) #HACE QUE LOS ENEMIGOS REALICEN SUS ACCIONES
        acciones.comportamiento_jugador(jugador_1) #HACE QUE EL JUGADOR REALICE SUS ACCIONES
        acciones.comportamiento_obstaculos(lista_obstaculos)
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
    
        acciones.dibujar(pantalla_del_juego, jugador_1, lista_de_enemigos, contador, lista_obstaculos)

        RELOJ.tick(60)
        #CHEQUEA CONDICIONES DE TERMINACION DEL JUEGO
        nivel_2 = acciones.chequeo_final(jugador_1, lista_de_enemigos, pantalla_del_juego, contador) 
    