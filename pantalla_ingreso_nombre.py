import pygame
import sys
from acciones import dibujar_ingreso_nombre
from acciones import validar_string_alfanumérico
pygame.init()

#PANTALLA DE COMIENZO DEL JUEGO
def pantalla_ingreso_nombre(pantalla:object)->None: 
    
    nuevo_nombre = ''
    ingreso_nombre = True
    while ingreso_nombre == True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #Permite cerrar el juego
                ingreso_nombre = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    nuevo_nombre = nuevo_nombre[:-1]
                elif event.key == pygame.K_RETURN and len(nuevo_nombre) > 0:
                    ingreso_nombre = False
                    return nuevo_nombre
                elif event.key == pygame.K_SPACE:
                    nuevo_nombre += '_'
                else:
                    letra = event.unicode
                    if validar_string_alfanumérico(letra) and len(nuevo_nombre) < 8:
                        nuevo_nombre += letra
            
        dibujar_ingreso_nombre(pantalla, nuevo_nombre)

        