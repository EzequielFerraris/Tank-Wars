import pygame
import re
from enemigo import Enemigo
from pantalla_cierre import pantalla_de_cierre

pygame.init()
AMARILLO = (255,255,0)
ROJO = (255,0,0)

#DIBUJAR PROYECTILES
def dibujar_proyectiles(tanque:object, pantalla:object):
    for proyectil in tanque.proyectiles:
        proyectil.dibujar(pantalla)

#FUNCION DIBUJAR
def dibujar(pantalla:object, jugador:object, lista_de_enemigos:object, contador:object, lista_obstaculos:list)->None:

    #pantalla.fill((0,0,0))

    if contador.nivel == 1:
        pantalla.fill((128, 128, 128))
    elif contador.nivel == 2:
        pantalla.fill((48,178,48))
    elif contador.nivel == 3:
        pantalla.fill((249,229,149))
    else:
        pantalla.fill((232,142,9))

    jugador.dibujar(pantalla)

    for enemigo in lista_de_enemigos:
        enemigo.dibujar(pantalla)

    for obstaculo in lista_obstaculos:
        obstaculo.dibujar(pantalla)

    dibujar_proyectiles(jugador, pantalla)

    for enemigo in lista_de_enemigos:
        dibujar_proyectiles(enemigo, pantalla)

    contador.dibujar(pantalla)

    pygame.display.flip()

#FUNCION COMPORTAMIENTO ENEMIGO
def comportamiento_enemigos(lista_enemigos:list)->None:
    for enemigo in lista_enemigos:
        if enemigo.visible == 0:
            lista_enemigos.pop(lista_enemigos.index(enemigo))
        enemigo.mover()
        enemigo.disparar()
            
        
#FUNCION COMPORTAMIENTO JUGADOR:
def comportamiento_jugador(jugador):
    jugador.disparar()

#FUNCION COMPORTAMIENTO OBSTACULOS
def comportamiento_obstaculos(lista_obstaculos:list)->None:
    for obstaculo in lista_obstaculos:
        if obstaculo.vidas == 0:
            obstaculo.rect_principal = pygame.Rect(obstaculo.x-2, obstaculo.y-2, 0, 0)
        if obstaculo.visible == 0:
            lista_obstaculos.pop(lista_obstaculos.index(obstaculo))

#FUNCION COMPORTAMIENTO CONTADOR:
def comportamiento_contador(contador:object, jugador:object)->None:
    contador.vidas = jugador.vidas
    contador.puntaje = jugador.puntaje

#CHEQUEAR SI SE DAN LAS CONDICIONES DE FINALIZACION
def chequeo_final(jugador:object, lista_enemigos:list, pantalla:object, contador:object)->bool:
    if jugador.visible < 1 or contador.tiempo < 1:
        #PANTALLA FINAL
        pantalla_de_cierre('derrota', pantalla, contador)    
        return False
    elif len(lista_enemigos) < 1:
        contador.nivel += 1
        return False
    else:
        return True


#DIBUJAR LA PANTALLA DE INGRESO DEL NOMBRE
def dibujar_ingreso_nombre(pantalla:object, nuevo_nombre:str):
    FUENTE_CONSIGNA = pygame.font.Font('Fonts/Trade Gothic LT Bold Condensed No. 20.ttf', 35)
    pantalla.fill((0, 0, 0))
    rectangulo_ingreso_nombre = pygame.Rect(64*7, 350, 64*4, 64*1)
    texto = FUENTE_CONSIGNA.render('Enter your name, captain!', 1, AMARILLO)
    if len(nuevo_nombre) == 8:
        nuevo_nombre += ' (MAX)'
    texto2 = FUENTE_CONSIGNA.render(nuevo_nombre, 1, ROJO)
    texto3 = FUENTE_CONSIGNA.render('Then press ENTER', 1, AMARILLO)
    pygame.draw.rect(pantalla, (255,255,0), rectangulo_ingreso_nombre, 2)  
    pantalla.blit(texto, (64*9 - (texto.get_width()/2), 200))
    pantalla.blit(texto2, (64*9 - (texto2.get_width()/2), 360))
    pantalla.blit(texto3, (64*9 - (texto3.get_width()/2), 500))
    
    
    pygame.display.update()

#VALIDA UN CARACTER ALFANUMERICO Y GUIONES

def validar_string_alfanumérico(cadena:str)->bool:
    if type(cadena) == str:
        if re.search('[^a-zA-Z0-9_\-]', cadena):
            resultado = False
        else:
            resultado = True
    else: 
        resultado = False
    return resultado