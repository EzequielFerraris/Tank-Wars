import pygame
import sys
import scores
pygame.init()

FUENTE_SCORE = pygame.font.SysFont('Arial', 30, True)
FUENTE_TITULO_SCORE = pygame.font.SysFont('Arial', 45, True)
AMARILLO = (255,255,0)
ROJO = (255,0,0)

def pantalla_puntajes(pantalla:object, contador:object):
    lapso_scores = True
    pantalla.fill((0, 0, 0))

    #SOLICITO LOS PUNTAJES A MOSTRAR
    lista_puntajes = scores.pedir_top_puntajes()

    while lapso_scores == True:
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                lapso_scores = False
                pygame.quit() 
                sys.exit()
        
        titulo = FUENTE_TITULO_SCORE.render('TOP PLAYERS', 1, AMARILLO)
        pantalla.blit(titulo, ((64*8.5 - (titulo.get_width()/2)), 50))

        for index,resultado in enumerate(lista_puntajes):
            text = FUENTE_SCORE.render(f'#{index+1}-{resultado[1]}..........{resultado[2]}', 1, ROJO)
            pantalla.blit(text, (64*6, 50*index + 150))
        
        pygame.display.update()

        pygame.time.delay(200)

        escape_button = pygame.key.get_pressed()
        if escape_button[pygame.K_ESCAPE]:
            lapso_scores = False
            pygame.quit()
            sys.exit
