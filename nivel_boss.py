import pygame
import sys
import random as rd
from boss import Boss
from proyectil import Proyectil
from jugador import Jugador
from enemigo import Enemigo
from muro import Muro
from ladrillo import Ladrillo
from bosque import Bosque
from pantalla_pausa import pantalla_pausa
import acciones
import sonidos

#DISEÑO DE LOS OBSTACULOS DEL NIVEL
def crear_obstaculos(lista_obstaculos:list)->list:
    for obstaculo in range(17):
        if obstaculo < 3 or (obstaculo > 4 and obstaculo < 8) or (obstaculo > 9 and obstaculo < 13) or (obstaculo > 14):
            continue
        else:
            ladrillo = Ladrillo(64 * obstaculo, 64*9)
            lista_obstaculos.append(ladrillo)

    for obstaculo in range(13):
        bosque = Bosque(0*64, (obstaculo*64))
        bosque1 = Bosque(1*64, (obstaculo*64))
        bosque2 = Bosque(16*64, (obstaculo*64))
        bosque3 = Bosque(17*64, (obstaculo*64))
        lista_obstaculos.append(bosque)
        lista_obstaculos.append(bosque1)
        lista_obstaculos.append(bosque2)
        lista_obstaculos.append(bosque3)

def nivel_boss(pantalla_del_juego:object, contador:object)->None:
    #CREO AL JUGADOR, LOS ENEMIGOS Y LA FUENTE DEL REGISTRO DE VIDAS Y PUNTOS
    jugador_1 = Jugador(64*8.5, 64*11, 'jugador_1', 'arriba', contador.puntaje) #Crea al jugador
    boss_final = Boss((64*6.5), (1*64), 'Boss', 'abajo')
    contador_minions = 0 

    #CREO LOS OBSTACULOS
    lista_obstaculos = []
    crear_obstaculos(lista_obstaculos)

    #LISTAS
    lista_de_enemigos = [boss_final]
    lista_de_objetos_chocables = [boss_final, jugador_1] + lista_obstaculos

    #TIEMPO
    RELOJ = pygame.time.Clock()
    contador.tiempo_maximo = 120 
    tiempo_actual = 0
    inicio_del_nivel = 0

    #MUSICA
    pygame.mixer.music.load('Sonidos/Boss1.mp3')
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)

    #CONDICION DEL LOOP
    nivel_boss = True

    #LOOP PRINCIPAL
    while nivel_boss:
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

        #VELOCIDAD BOSS
        if tiempo_mostrado > 3000:
            boss_final.velocidad = boss_final.velocidad + (tiempo_mostrado * 0.00001)

        #ACTUALIZAR LISTA DE CHOCABLES
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

        if keys[pygame.K_RETURN]:
            sonidos.confirmacion.play()
            sonidos.confirmacion.set_volume(0.05)
            pygame.mixer.music.stop()
            pantalla_pausa(pantalla_del_juego, contador)
    
        acciones.dibujar(pantalla_del_juego, jugador_1, lista_de_enemigos, contador, lista_obstaculos)
        RELOJ.tick(60)
        #CHEQUEA CONDICIONES DE TERMINACION DEL JUEGO
        nivel_boss = acciones.chequeo_final(jugador_1, lista_de_enemigos, pantalla_del_juego, contador)
