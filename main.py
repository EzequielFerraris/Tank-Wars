import pygame
import scores
from pantalla_inicio import pantalla_inicio
from pantalla_ingreso_nombre import pantalla_ingreso_nombre
from nivel_1 import nivel_1
from nivel_2 import nivel_2
from nivel_3 import nivel_3
from contador_vidas import Contador
from pantalla_cierre import pantalla_de_cierre

pygame.init()
#CREO LA BASE DE DATOS SI NO EXISTE
scores.crear_bd_puntajes()
#DECLARO LA PANTALLA PRINCIPAL
#Crea la pantalla en múltiplos de 64, el tamaño de los bloques
pantalla_del_juego = pygame.display.set_mode((17*64, 11*64))

#Leyenda en la ventana de la aplicación
pygame.display.set_caption('Tank Wars') 

nombre_jugador = 'Jugador_1'

#PANTALLA DE INICIO
pantalla_inicio(pantalla_del_juego)
nombre_jugador = pantalla_ingreso_nombre(pantalla_del_juego)

#Creo el contador de vidas y puntos
contador = Contador(3, 0, nombre_jugador, 60000*5)

#NIVELES
nivel_1(pantalla_del_juego, contador)
#nivel_2(pantalla_del_juego, contador)
#nivel_3(pantalla_del_juego, contador)

#INSERTO PUNTAJE EN TABLA
scores.insertar_puntajes(contador.nombre, contador.puntaje)

#PANTALLA FINAL
pantalla_de_cierre('victoria', pantalla_del_juego, contador)
