import pygame
import sys

pygame.init()

FUENTE_PRINCIPAL = pygame.font.Font('Fonts/Trade Gothic LT Bold Condensed No. 20.ttf', 100)
FUENTE_SECUNDARIA = pygame.font.Font('Fonts/Trade Gothic LT Bold Condensed No. 20.ttf', 50)
AMARILLO = (255,255,0)
ROJO = (255,0,0)

def pantalla_entre_niveles(pantalla:object, contador:object)->None:
    lapso = True
    pantalla.fill((0, 0, 0))
    pygame.display.update()

    #TIEMPO
    RELOJ = pygame.time.Clock() 
    tiempo_actual = 0
    inicio_del_nivel = 0
    
    #MUSICA
    pygame.mixer.music.load('Sonidos/Pantalla_entre_niveles.mp3')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play()

    while lapso == True:
        pygame.time.delay(10)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                lapso = False
                pygame.quit() 
                sys.exit()

         #TIEMPO DEL JUEGO
        if inicio_del_nivel == 0:
            inicio_del_nivel = pygame.time.get_ticks()

        tiempo_actual = pygame.time.get_ticks()
        tiempo_mostrado = tiempo_actual - inicio_del_nivel

        if contador.nivel < 4:
            text = FUENTE_PRINCIPAL.render(f'LEVEL {contador.nivel}', 1, AMARILLO)
        else:
            text = FUENTE_PRINCIPAL.render('FINAL BOSS', 1, AMARILLO)
        
        #text2 = FUENTE_SECUNDARIA.render(f'', 1, ROJO)

        pantalla.blit(text, (64*9 - (text.get_width()/2),64*5))
        #pantalla.blit(text2, (64*8.5 - (text2.get_width()/2),350))
        
        RELOJ.tick(60)
        pygame.display.update()
        
        if tiempo_mostrado > 3000:
            break
            

        

        

    
    
