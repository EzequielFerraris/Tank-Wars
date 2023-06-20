import pygame
import sys
import scores
import sonidos
from pantalla_puntajes import pantalla_puntajes

pygame.init()

FUENTE_RESULTADO = pygame.font.Font('Fonts/Trade Gothic LT Bold Condensed No. 20.ttf', 100)
FUENTE_CIERRE_JUEGO = pygame.font.SysFont('Fonts/Trade Gothic LT Bold Condensed No. 20.ttf', 50)
FUENTE_SCORE = pygame.font.SysFont('Fonts/Trade Gothic LT Bold Condensed No. 20.ttf', 50)
AMARILLO = (255,255,0)
ROJO = (255,0,0)

def pantalla_de_cierre(resultado:str, pantalla:object, contador:object)->None:
    lapso = True
    pantalla.fill((0, 0, 0))
    pygame.display.update()
    #INSERTO PUNTAJE EN TABLA
    scores.insertar_puntajes(contador.nombre, contador.puntaje)

    #MUSICA DE FONDO
    if resultado == 'victoria':
        pygame.mixer.music.load('Sonidos/Victoria.mp3')
    else:
        pygame.mixer.music.load('Sonidos/Game_over.mp3')

    pygame.mixer.music.play()

    #MAIN LOOP
    while lapso == True:
        pygame.time.delay(10)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                lapso = False
                pygame.quit() 
                sys.exit()

        #MENSAJE PRINCIPAL
        if resultado == 'victoria':
            text = FUENTE_RESULTADO.render('VICTORY', 1, AMARILLO)
        else:
            text = FUENTE_RESULTADO.render('GAME OVER', 1, AMARILLO)

        #MENSAJE PUNTAJE
        text2 = FUENTE_SCORE.render(f'{contador.nombre}, your score was: {contador.puntaje}', 1, ROJO)
        #MENSAJE TECLA PARA IR A PUNTAJES MAS ALTOS
        texto_cierre_juego = FUENTE_CIERRE_JUEGO.render('Press ENTER', 1, AMARILLO)
        
        pantalla.blit(text, (64*9 - (text.get_width()/2),200))
        pantalla.blit(text2, (64*9 - (text2.get_width()/2),400))
        pantalla.blit(texto_cierre_juego, (64*9 - (texto_cierre_juego.get_width()/2),600))
        pygame.display.update()

        enter_button = pygame.key.get_pressed()
        if enter_button[pygame.K_RETURN]:
            sonidos.confirmacion.play()
            sonidos.confirmacion.set_volume(0.05)
            lapso = False
            pygame.mixer.music.fadeout(500)
            pantalla_puntajes(pantalla, contador)
            break

    
    
