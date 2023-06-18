import pygame
import sys
import scores
from pantalla_puntajes import pantalla_puntajes

pygame.init()

FUENTE_RESULTADO = pygame.font.SysFont('Arial', 100)
FUENTE_CIERRE_JUEGO = pygame.font.SysFont('Arial', 25, True)
FUENTE_SCORE = pygame.font.SysFont('Arial', 50, True)
AMARILLO = (255,255,0)
ROJO = (255,0,0)

def pantalla_de_cierre(resultado:str, pantalla:object, contador:object)->None:
    lapso = True
    pantalla.fill((0, 0, 0))
    pygame.display.update()
    #INSERTO PUNTAJE EN TABLA
    scores.insertar_puntajes(contador.nombre, contador.puntaje)
    while lapso == True:
        pygame.time.delay(10)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                lapso = False
                pygame.quit() 
                sys.exit()

        if resultado == 'victoria':
            text = FUENTE_RESULTADO.render('VICTORY', 1, AMARILLO)
        else:
            text = FUENTE_RESULTADO.render('GAME OVER', 1, AMARILLO)

        text2 = FUENTE_SCORE.render(f'{contador.nombre}, your score was: {contador.puntaje}', 1, ROJO)

        texto_cierre_juego = FUENTE_CIERRE_JUEGO.render('Press ENTER', 1, AMARILLO)
        
        pantalla.blit(text, (64*8.5 - (text.get_width()/2),200))
        pantalla.blit(text2, (64*8.5 - (text2.get_width()/2),350))
        pantalla.blit(texto_cierre_juego, (64*8.5 - (texto_cierre_juego.get_width()/2),500))

        pygame.display.update()

        enter_button = pygame.key.get_pressed()
        if enter_button[pygame.K_RETURN]:
            lapso = False
            pantalla_puntajes(pantalla, contador)
            break

    
    
