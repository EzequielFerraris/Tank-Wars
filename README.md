# Segundo parcial Laboratorio I
## Tecnicatura Universitaria en Programación - UTN

## Autor: [Ferraris Ezequiel Manuel](https://github.com/EzequielFerraris)
# Videojuego estilo Arcade utilizando Pygame - 'Tank Wars'

![Proyecto](https://github.com/EzequielFerraris/Tank-Wars/blob/master/Imagenes%20README/Pantalla_inicio.png)

## Descripción
Este proyecto fue desarrollado en base a las consignas provistas por la cátedra de Laboratorio I de la Tecnicatura Universitaria en Programación, para la promoción del segundo parcial. 

Las mismas establecían que debía desarrollarse un **videojuego utilizando la biblioteca Pygame**, con el objetivo de aplicar los conceptos vistos durante el desarrollo del cuatrimestre. En este sentido, el mismo está diseñado utilizando el paradigma orientado a objetos(POO), maneja Eventos y antincipa excepciones, utiliza SQLite para almacenar puntajes, emplea recursos gráficos como animaciones, cambios de estado y color, tiene un detallado uso del sonido para sus distintos momentos, administra colisiones entre los distintos objetos, recibe inputs de distinta índole, utiliza el tiempo y eventos temporales, alterna entre pantallas, entre otros.

## Características del juego
* Tres niveles principales, con dificultad creciente.
* Una batalla final contra un boss que se vuelve más complicado al pasar el tiempo.
* Música original creada por el músico Joel Ferraris.
* Sonidos y animaciones en mapas que recuerdan al legendario 'Battle City'.
* Ranking de puntajes, para quienes gustan de superarse.

![Nivel 1](https://github.com/EzequielFerraris/Tank-Wars/blob/master/Imagenes%20README/Level_1.png)


## Funcionalidad
Al correr el script main.py el juego comienza con una pantalla donde figura el título del juego y se pide presionar la tecla Enter.
Al hacerlo se pasa a la pantalla de ingreso del nombre.

![Ingreso del nombre](https://github.com/EzequielFerraris/Tank-Wars/blob/master/Imagenes%20README/name_input.png)

Tras ingresar el nombre, que es validado para que solo incluya caracteres alfanuméricos y guiones, el jugador comienza la partida. Hay tres niveles, uno de batalla en las afueras de una ciudad, otro en los lagos y uno más en una playa.
El jugador **gana puntos** al destruir enemigos.

![Nivel 3](https://github.com/EzequielFerraris/Tank-Wars/blob/master/Imagenes%20README/Level_3.png)

Luego de superar estos obstáculos, el jugador debe enfrentarse al Boss final.

![Boss final](https://github.com/EzequielFerraris/Tank-Wars/blob/master/Imagenes%20README/Boss_fight.png)

El jugador cuenta para esto con tres vidas por nivel, que se recuperan al comenzar una nueva instancia. Sin embargo, perder vidas hace que **pierda puntaje**.
Si el jugador no gana el nivel antes de que el contador de tiempo llegue a 0, perderá automáticamente. De lo contrario, resultará vencedor.

![Victoria](https://github.com/EzequielFerraris/Tank-Wars/blob/master/Imagenes%20README/Victory_screen.png)

Si al perder o al resultar vencedor su puntaje está entre los 10 más altos, aparecerá en la pantalla de Top Scores.

![Scores](https://github.com/EzequielFerraris/Tank-Wars/blob/master/Imagenes%20README/Scores.png)


