# Cipher-Disks
App de Cifrado con inspiracion en el cifrado de Caesar, hecho principalmente para encriptar mensajes para mis jugadores de D&D, asi poder encriptar algo con tiempo de preparacion o en el momento.

# Introduccion

Este es un minijuego hecho para mis sesiones de juego de D&D, ya que a mis jugadores les gusta descifrar cosas.
No tiene uso practico fuera de ser un cifrador basado en el de Caesar, con algunos pocos cambios para un mayor dificultad y/o diversion al descifrarlo.

# Uso
Es exactamente igual (En la base al menos) al cifrado de Caesar, se intercambia una letra por su equivalente en la posicion del disco opuesto, 1 a 1 cada letra.
Si se añade una piedra Amarilla, dependiendo del valor de la piedra amarilla, se haran los efectos extra de las demas piedras, si no hay una piedra amarilla, las demas piedras no surtiran efecto. Esta piedra funciona meramente como una bateria
Esto esta hecho como un añadido al puzzle aunque la piedra como tal no sirva si no pones mas piedras de otros colores.
Ademas habran diferentes anillos (Se pueden randomizar) para hacer un cifrado modular

## Partes
Consta de varias partes, para que funcione de manera modular y se puedan hacer varios cifrados sin perder la esencia
Comenzando con los conocidos de Caesar

- 2 anillos con los alfabetos, para el intercambio de letras por indice, una letra corresponde a la otra en el anillo opuesto.
    - Sin embargo esto tiene un añadido, pues uno de los anillos esta dividido en partes (Se puede elegir que tantas y cuantas letras iran en cada una, si es que alcanza el alfabeto.)
    - El otro anillo es exactamente un alfabeto normal, sin divisiones ni nada extraño.
    - IMPORTANTE: estos alfabetos se pueden proporcionar, pueden ser simbolos o demas. Aunque aun deben arreglarse algunas cosas, podra ser personalizado sin problemas

- Estructura central, la cual consta de ser solo una pieza con 4 agujeros, separados uniformemente.
    - Estos agujeros tienen el espacio suficiente para poner hasta 4 piedras dentro de ellos, dando un total de 8 piedras
    - Cada uno de estos equivale a un numero del 1 al 4, siendo el "orden" o "valor" o "peso" de cada piedra al usarse en el cifrado
    - Van desde arriba derecha, arriba izquierda, abajo izquierda, abajo derecha. En sentido de reloj dando 1,2,3,4 respectivamente.

- Por ultimo las piedras con efecto, cada piedra tendra un efecto al cifrar, siendo la mas importante la Amarilla/Yellow.
    - Los efectos de las piedras varian a como las he creado para las sesiones, tengo pensado ir añadiendo mas pero por ahora tenemos
        - AMARILLA: Su efecto es dictar cada cuantas letras se hara el cambio extra
        - Rojo-Verde: Piedra dual, un lado de color Rojo y otro de color Verde. Su significado es simple, añade la cantidad de posiciones a mover extra, el lado Rojo indica contrareloj y Verde indica a reloj.
        - Azul: Cada cuantas letras, se hara un cambio especial, este cambio sera el ultimo en la cadena, e intercambiara la letra que se haya cifrado, por su opuesto en el circulo (13 posiciones). Esta se aplica con un tempo propio, ejemplo con una piedra con valor 4, se aplicara cada 4 letras que las piedras se apliquen, si la piedra amarilla tiene valor de 2, la azul se aplicara cada 2x4 = 8 letras

# Jerarquia de Color

1.-Amarilla
2.-Rojo-Verde
3.-Azul
4.-Morada - Por implementar


### Disclaimer ###
Actualizare el README para que sea mas legible, y dare una version en ingles.