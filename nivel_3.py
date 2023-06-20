import pygame
import sys
import random as rd
from enemigo import Enemigo
from proyectil import Proyectil
from jugador import Jugador
from muro import Muro
from bosque import Bosque
from agua import Agua
from pantalla_inicio import pantalla_inicio
import acciones
import sonidos

def crear_obstaculos(lista_obstaculos:list)->list:
    for obstaculo in range(18):
        if obstaculo < 3 or (obstaculo > 4 and obstaculo < 8) or (obstaculo > 9 and obstaculo < 13) or (obstaculo > 14):
            continue
        else:
            muro = Muro(64 * obstaculo, 500)
            lista_obstaculos.append(muro)
    
    for obstaculo in range(18):
        costa = Agua(64 * obstaculo, 64*13)
        lista_obstaculos.append(costa)
        costa2 = Agua(64 * obstaculo, 64*12)
        lista_obstaculos.append(costa2)

    costa3 = Agua(0, 64*11)
    lista_obstaculos.append(costa3)
    costa4 = Agua(64*17, 64*11)
    lista_obstaculos.append(costa4)

    for obstaculo in range(8):
        bosque = Bosque((64*5 + obstaculo*64), 0*64)
        bosque1 = Bosque((64*5 + obstaculo*64), 1*64)
        bosque2 = Bosque((64*5 + obstaculo*64), 2*64)
        bosque3 = Bosque((64*5 + obstaculo*64), 3*64)
        lista_obstaculos.append(bosque)
        lista_obstaculos.append(bosque1)
        lista_obstaculos.append(bosque2)
        lista_obstaculos.append(bosque3)
    
    for obstaculo in range(6):
        bosque = Bosque(0*64, (4*64+ obstaculo*64))
        bosque1 = Bosque(1*64, (4*64+ obstaculo*64))
        bosque2 = Bosque(16*64, (4*64+ obstaculo*64))
        bosque3 = Bosque(17*64, (4*64+ obstaculo*64))
        lista_obstaculos.append(bosque)
        lista_obstaculos.append(bosque1)
        lista_obstaculos.append(bosque2)
        lista_obstaculos.append(bosque3)

def nivel_3(pantalla_del_juego:object, contador:object)->None:
    #CREO AL JUGADOR, LOS ENEMIGOS 
    jugador_1 = Jugador(64*8.5, 64*11, 'jugador_1', 'arriba', contador.puntaje) #Crea al jugador
    enemigo_1 = Enemigo((64*3.5), (2*64), 'enemigo_1', 'abajo', 20)
    enemigo_2 = Enemigo((64*7), (4*64), 'enemigo_2', 'abajo', 20)
    enemigo_3 = Enemigo((64*10.5), (4*64), 'enemigo_3', 'abajo', 20)
    enemigo_4 = Enemigo((64*15), (2*64), 'enemigo_3', 'abajo', 20)

    #CREO LOS OBSTACULOS
    lista_obstaculos = []
    crear_obstaculos(lista_obstaculos)
    
    #LISTAS
    lista_de_enemigos = [enemigo_1, enemigo_2, enemigo_3, enemigo_4]
    lista_de_objetos_chocables = [enemigo_1, enemigo_2, enemigo_3, enemigo_4, jugador_1] + lista_obstaculos

    #TIEMPO
    RELOJ = pygame.time.Clock() 
    tiempo_actual = 0
    inicio_del_nivel = 0

    #CONDICION DEL LOOP
    nivel_3 = True

    #LOOP PRINCIPAL
    while nivel_3:
        pygame.time.delay(100) 

        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                nivel_3 = False
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
        nivel_3 = acciones.chequeo_final(jugador_1, lista_de_enemigos, pantalla_del_juego, contador)
