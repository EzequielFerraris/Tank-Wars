import pygame
import sys
pygame.init()

FUENTE_COMIENZO_JUEGO = pygame.font.SysFont('Arial', 80, True)
FUENTE_START = pygame.font.SysFont('Arial', 25, True)
AMARILLO = (255,255,0)


#PANTALLA DE COMIENZO DEL JUEGO
def pantalla_inicio(pantalla:object)->None: 
    intro = True
    while intro == True:

        pantalla.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT: #Permite cerrar el juego
                intro = False
                pygame.quit()
                sys.exit()

        titulo = FUENTE_COMIENZO_JUEGO.render('Tank Wars', 1, AMARILLO)
        pantalla.blit(titulo, (64*8.5 - (titulo.get_width()/2), 200))

        subtexto = FUENTE_START.render('Press enter to start', 1, AMARILLO)
        pantalla.blit(subtexto, (64*8.5 - (subtexto.get_width()/2), 500))
        pygame.display.update()

        enter = pygame.key.get_pressed()
        if enter[pygame.K_RETURN]:
            intro = False
        