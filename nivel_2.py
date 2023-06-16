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

def nivel_2(pantalla_del_juego:object, contador:object)->None:
    #CREO AL JUGADOR, LOS ENEMIGOS Y LA FUENTE DEL REGISTRO DE VIDAS Y PUNTOS
    jugador_1 = Jugador(64*8, 64*9, 'jugador_1', 'arriba', contador.puntaje) #Crea al jugador
    enemigo_1 = Enemigo((rd.randint(1, 64*4)), (rd.randint(20, 270)), 'enemigo_1', 'abajo', 18)
    enemigo_2 = Enemigo((rd.randint(64*6, 64*10)), (rd.randint(20, 270)), 'enemigo_2', 'abajo', 18)
    enemigo_3 = Enemigo((rd.randint(64*12, 64*16)), (rd.randint(20, 270)), 'enemigo_3', 'abajo', 18)

    lista_obstaculos = []

    for obstaculo in range(17):
        ladrillo = Ladrillo(64 * obstaculo, 300)
        lista_obstaculos.append(ladrillo)

    for obstaculo in range(17): #Crea ladrillos y agua
        if obstaculo < 2 or (obstaculo > 4 and obstaculo < 7) or (obstaculo > 9 and obstaculo < 12) or (obstaculo > 14):
            ladrillo = Ladrillo(64 * obstaculo, 400)
            lista_obstaculos.append(ladrillo)
        else:
            agua = Agua(64 * obstaculo, 400)
            lista_obstaculos.append(agua)
    
    for obstaculo in range(5):
        if obstaculo != 2 and obstaculo !=3:
            ladrillo = Ladrillo(5*64, 64 * obstaculo)
            ladrillo2 = Ladrillo(11*64, 64 * obstaculo)
            lista_obstaculos.append(ladrillo)
            lista_obstaculos.append(ladrillo2)
        else: 
            muro = Muro(5*64, 64 * obstaculo)
            muro2 = Muro(11*64, 64 * obstaculo)
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
        bosque4 = Bosque(13*64, obstaculo*64)
        bosque5 = Bosque(14*64, obstaculo*64)
        bosque6 = Bosque(15*64, obstaculo*64)
        bosque7 = Bosque(16*64, obstaculo*64)
        lista_obstaculos.append(bosque4)
        lista_obstaculos.append(bosque5)
        lista_obstaculos.append(bosque6)
        lista_obstaculos.append(bosque7)

    lista_de_enemigos = [enemigo_1, enemigo_2, enemigo_3]
    lista_de_objetos_chocables = [enemigo_1, enemigo_2, enemigo_3, jugador_1] + lista_obstaculos

    nivel_2 = True

    #LOOP PRINCIPAL
    while nivel_2:
        pygame.time.delay(100) 

        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                nivel_2 = False
                pygame.quit()
                sys.exit()

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
            
        if keys[pygame.K_RIGHT] and jugador_1.x < (64*17) - jugador_1.ancho - jugador_1.velocidad and not jugador_1.chocar('derecha'):
            jugador_1.direccion = 'derecha'
            jugador_1.x += jugador_1.velocidad
            
        if keys[pygame.K_UP] and jugador_1.y > jugador_1.velocidad + 25 and not jugador_1.chocar('arriba'):
            jugador_1.direccion = 'arriba'
            jugador_1.y -= jugador_1.velocidad
            
        if keys[pygame.K_DOWN] and jugador_1.y < (64*11) - jugador_1.alto - jugador_1.velocidad and not jugador_1.chocar('abajo'):
            jugador_1.direccion = 'abajo'
            jugador_1.y += jugador_1.velocidad
        
        if keys[pygame.K_SPACE] and len(jugador_1.proyectiles) < jugador_1.maximo_proyectiles_simultaneos: 
            jugador_1.proyectiles = Proyectil(jugador_1)
    
        acciones.dibujar(pantalla_del_juego, jugador_1, lista_de_enemigos, contador, lista_obstaculos)
        nivel_2 = acciones.chequeo_final(jugador_1, lista_de_enemigos, pantalla_del_juego, contador) #CHEQUEA CONDICIONES DE TERMINACION DEL JUEGO
    