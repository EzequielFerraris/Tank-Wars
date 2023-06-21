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
* Música original creada por el profesor y músico [Joel Ferraris](https://www.linkedin.com/in/joel-f-4101bb153/).
* Sonidos y animaciones en mapas que recuerdan al legendario 'Battle City'.
* Ranking de puntajes, para quienes gustan de superarse.

![Nivel 1](https://github.com/EzequielFerraris/Tank-Wars/blob/master/Imagenes%20README/Level_1.png)


## Funcionalidad
Tank Wars es un juego 2D de estilo arcade en el cuál el jugador controla un tanque y debe derrotar a sus enemigos. El mismo ha sido creado en referencia y tomando como modelo el famoso juego "Battle City".

Al ingresar al juego, el usuario se encuentra con una pantalla que muestra el título del juego y la indicación de presionar la tecla "Enter". 

![Ingreso del nombre](https://github.com/EzequielFerraris/Tank-Wars/blob/master/Imagenes%20README/name_input.png)

Esto permite acceder a la pantalla de ingreso del nombre, la que permite ingresar cualquier carácter alfanumérico y guiones para constituir el nombre. Si la cantidad de letras ingresadas llega al máximo, el juego muestra la leyenda "(MAX)" e impide ingresar más caracteres.

Al ingresar Enter, el jugador pasa a una pantalla que muestra el nivel al que ingresa (en este caso el 1).

![Nivel 3](https://github.com/EzequielFerraris/Tank-Wars/blob/master/Imagenes%20README/Level_3.png)

Una vez comenzado el nivel, el jugador nota que en la parte superior de la pantalla aparece una barra en la que se ven:
-Su nombre (izquierda)
-El tiempo restante (centro).
-La cantidad de vidas y el puntaje.

Respecto del tiempo, si el contador llega a 0 la partida se termina y el jugador pierde (pasa a una pantalla con la leyenda "Game Over" y su puntaje). Al quedar menos de un minuto, el color del temporizador pasa de amarillo a rojo.

Respecto de las vidas, las mismas son 3 por nivel y se recuperan al pasar de instancia. Se pierden vidas por recibir impactos de proyectiles enemigos. Cabe remarcar que al perder una vida, se pierden también 100 puntos del puntaje total.

Respecto del puntaje: el mismo arranca en 0 y va subiendo si el jugador impacta con proyectiles a sus enemigos. Cada impacto otorga 100 puntos. Recibir impactos causa el efecto contrario. El puntaje se mantiene a través de los niveles.

Fuera del contador, el jugador puede moverse en el mapa con las teclas de dirección, disparar con la tecla de espacio y pausar el juego con la tecla enter. 

Respecto de los disparos, el jugador cuenta con hasta 5 disparos simultáneos, después de los cuales debe esperar a que los mismos impacten antes de poder realizar nuevos.

Respecto de la tecla enter, pulsarla durante alguno de los niveles detiene el flujo del juego y el reloj, al llevar al usuario a la pantalla de pausa.

Luego de superar los obstáculos de los tres primeros niveles, el jugador debe enfrentarse al Boss final.

![Boss final](https://github.com/EzequielFerraris/Tank-Wars/blob/master/Imagenes%20README/Boss_fight.png)

Derrotar al Boss completa el juego.

![Victoria](https://github.com/EzequielFerraris/Tank-Wars/blob/master/Imagenes%20README/Victory_screen.png)

Si al perder o al resultar vencedor su puntaje está entre los 10 más altos, aparecerá en la pantalla de Top Scores.

![Scores](https://github.com/EzequielFerraris/Tank-Wars/blob/master/Imagenes%20README/Scores.png)


