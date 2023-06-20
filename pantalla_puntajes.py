import pygame
import sys
import scores
pygame.init()

FUENTE_SCORE = pygame.font.Font('Fonts/Trade Gothic LT Bold Condensed No. 20.ttf', 25)
FUENTE_TITULO_SCORE = pygame.font.Font('Fonts/Trade Gothic LT Bold Condensed No. 20.ttf', 60)
FUENTE_EXIT = pygame.font.Font('Fonts/Trade Gothic LT Bold Condensed No. 20.ttf', 50)
AMARILLO = (255,255,0)
ROJO = (255,0,0)

def pantalla_puntajes(pantalla:object, contador:object):
    lapso_scores = True
    pantalla.fill((0, 0, 0))

    #MUSICA
    pygame.mixer.music.load('Sonidos/Puntajes.wav')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    #SOLICITO LOS PUNTAJES A MOSTRAR
    lista_puntajes = scores.pedir_top_puntajes()

    while lapso_scores == True:
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                lapso_scores = False
                pygame.quit() 
                sys.exit()
        
        titulo = FUENTE_TITULO_SCORE.render('TOP PLAYERS', 1, AMARILLO)
        pantalla.blit(titulo, ((64*9 - (titulo.get_width()/2)), 50))

        rectangulo_scores = pygame.Rect(64*6, 160, 64*6, 64*7.5)
        pygame.draw.rect(pantalla, (255,255,0), rectangulo_scores, 2)  

        for index,resultado in enumerate(lista_puntajes):
            lugar_y_nombre = f'#{str(index+1).zfill(2)}-{resultado[1]}'
            resultado_final = f'{resultado[2]}'
            texto_a_mostrar = lugar_y_nombre.ljust(15,"_") +  resultado_final.rjust(10,"_")
            text = FUENTE_SCORE.render(texto_a_mostrar, 1, ROJO)
            pantalla.blit(text, ((64*9 - (text.get_width()/2)), 40*index + 200))
        

        titulo2 = FUENTE_TITULO_SCORE.render('PRESS ESCAPE TO EXIT', 1, AMARILLO)
        pantalla.blit(titulo2, ((64*9 - (titulo2.get_width()/2)), 64*11))

        pygame.display.update()
        
        escape_button = pygame.key.get_pressed()
        if escape_button[pygame.K_ESCAPE]:
            pygame.mixer.music.stop()
            lapso_scores = False
            pygame.quit()
            sys.exit
