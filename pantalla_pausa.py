import pygame
import sys
import sonidos

pygame.init()

FUENTE_PRINCIPAL = pygame.font.Font('Fonts/Trade Gothic LT Bold Condensed No. 20.ttf', 100)
FUENTE_SECUNDARIA = pygame.font.Font('Fonts/Trade Gothic LT Bold Condensed No. 20.ttf', 50)
AMARILLO = (255,255,0)
ROJO = (255,0,0)

def pantalla_pausa(pantalla:object, contador:object)->None:
    lapso = True
    pantalla.fill((0, 0, 0))
    pygame.display.update()

    #TIEMPO
    inicio_pausa = 0
    tiempo_en_pausa = 0
    
    #MUSICA
    pygame.mixer.music.load('Sonidos/pausa.mp3')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    while lapso == True:
        pygame.time.delay(100)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                lapso = False
                pygame.quit() 
                sys.exit()

        #TIEMPO DEL JUEGO
        if inicio_pausa == 0:
            inicio_pausa = pygame.time.get_ticks()

        tiempo_actual = pygame.time.get_ticks()
        tiempo_en_pausa = tiempo_actual - inicio_pausa

        text = FUENTE_PRINCIPAL.render(f'PAUSE', 1, AMARILLO)

        pantalla.blit(text, (64*9 - (text.get_width()/2),64*5))
        
        pygame.display.update()

        enter = pygame.key.get_pressed()
        if enter[pygame.K_RETURN]:
            contador.tiempo_maximo += (tiempo_en_pausa // 1000) 
            sonidos.confirmacion.play()
            sonidos.confirmacion.set_volume(0.05)
            pygame.mixer.music.stop()
            lapso = False

        
            