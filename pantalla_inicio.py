import pygame
import sys
import sonidos
pygame.init()

FUENTE_COMIENZO_JUEGO = pygame.font.Font('Fonts/Starjedi.ttf', 100)
FUENTE_START = pygame.font.Font('Fonts/Starjhol.ttf', 50)
AMARILLO = (255,255,0)


#PANTALLA DE COMIENZO DEL JUEGO
def pantalla_inicio(pantalla:object)->None: 

    #MUSICA
    pygame.mixer.music.load('Sonidos/Introduccion.mp3')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    intro = True
    while intro == True:

        pantalla.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT: #Permite cerrar el juego
                intro = False
                pygame.quit()
                sys.exit()

        titulo = FUENTE_COMIENZO_JUEGO.render('Tank Wars', 1, AMARILLO)
        pantalla.blit(titulo, (64*9 - (titulo.get_width()/2), 200))

        subtexto = FUENTE_START.render('Press enter to start', 1, AMARILLO)
        pantalla.blit(subtexto, (64*9 - (subtexto.get_width()/2), 500))
        pygame.display.update()

        enter = pygame.key.get_pressed()
        if enter[pygame.K_RETURN]:
            sonidos.confirmacion.play()
            sonidos.confirmacion.set_volume(0.05)
            pygame.mixer.music.fadeout(500)
            intro = False
        