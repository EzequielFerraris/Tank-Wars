import pygame
import sys

pygame.init()

FUENTE_PRINCIPAL = pygame.font.SysFont('Arial', 100)
FUENTE_SECUNDARIA = pygame.font.SysFont('Arial', 50, True)
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

        text = FUENTE_PRINCIPAL.render(f'NIVEL {contador.nivel}', 1, AMARILLO)
        
        #text2 = FUENTE_SECUNDARIA.render(f'', 1, ROJO)

        pantalla.blit(text, (64*8.5 - (text.get_width()/2),200))
        #pantalla.blit(text2, (64*8.5 - (text2.get_width()/2),350))
        if tiempo_mostrado > 3000:
            lapso = False

        RELOJ.tick(60)
        
        pygame.display.update()

        

    
    
