import pygame
pygame.init()

disparo_p1 = pygame.mixer.Sound('Sonidos/Disparo_2.mp3')
disparo_enemigo = pygame.mixer.Sound('Sonidos/disparo_enemigo.wav')
disparo_boss= pygame.mixer.Sound('Sonidos/Disparo_1.mp3')

explosion_tanque = pygame.mixer.Sound('Sonidos/Explosion.wav')
destruccion_muro = pygame.mixer.Sound('Sonidos/muro_destruido.mp3')

confirmacion = pygame.mixer.Sound('Sonidos/Confirmacion.wav')

impacto_muro = pygame.mixer.Sound('Sonidos/Impacto_muro.wav')
impacto_tanque = pygame.mixer.Sound('Sonidos/Impacto_tanque.wav')
impacto_muro_reforzado = pygame.mixer.Sound('Sonidos/colision_muro_reforzado.wav')
