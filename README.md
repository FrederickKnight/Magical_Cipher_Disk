# Magic-Cipher-Disk

Es un pequeño proyecto hecho para facilitarme la vida al jugar D&D con mis amigos, siendo el DM he preparado cosas para la diversión de ambas partes y como a algunos de ellos les gusta descifrar mensajes fue que programe esto y así encriptar mensajes incluso a media partida.

## Inspiración

Este cifrado esta basado en el Cifrado de César, es casi exactamente igual en la base.

Sin embargo para añadirle el toque de fantasía, añadí una mecánica con unas "Piedras" de colores, estas las explicare mas adelante pero su función es cambiar partes del cifrado, como añadir que la posición sea unas cuantas mas o unas cuantas menos, o que la posición sea la opuesta en el Disco.

Pienso añadir mas mecánicas a este "minijuego", como podría ser mas piedras con efectos diferentes o incluso mas partes.

# Partes

## Discos

El cifrado consta de dos Discos, cada uno con un alfabeto que puede ser proporcionado y personalizado, no solo con letras o números sino otros tipos de caracteres especiales.

El alfabeto de ambos discos puede ser proporcionado a su función correspondiente, y puede ser el mismo o diferente. Ambos discos pueden configurarse, sin embargo solo el interior, el cual servirá como el alfabeto encriptado, es el que se configurara con la siguiente función.

```python
disco_interior = Magical_Cipher_Disk.Disk('ABCDEFGHIJKLMNOPQRSTUVWXYZ').Create_Disk()
```

Por otro lado el alfabeto que servirá como el "normal" o aquel que no esta encriptado se proporcionara mas adelante en una funcion cuando creemos y configuremos el "Cipher".

## Piedras

Hay varios tipos de piedras, cada una con su función y color respectivo. Además de que cada una sirve en una jerarquía y orden, siendo la amarilla la mas importante.

Por ahora se tienen:
- ==**Amarilla**==  :: Sirve como la piedra de energía, si no hay una presente ninguna otra piedra tendrá alguna función. Además el valor que se le de a esta piedra servirá como el "tempo" de cada cuanto se activaran las otras piedras. Si su valor es 3, entonces cada 3 letras se activaran y harán su función las demás. 
- ==**Roja-Verde**== :: Esta es como una moneda de dos caras, una roja y otra verde, su función es simple pues dependiendo del valor que se le de, esta añadirá o restara posiciones al cifrado de la letra.
- ==**Azul**== :: Cuando esta actúe la letra pasara a ser la del lado opuesto del disco, significando que se añadirá 13 posiciones adelante de donde debería estar. Como si añadieras una piedra verde con valor 13. Sin embargo esta tiene un "tempo" propio que dependerá de su valor, pues actuara cada ciertas letras como su valor tenga, igual que la ==**Piedra Amarilla**==, pero solo sumara el "tempo" con cada letra que se le pase. Significa que no seguirá contando si la piedra amarilla no dejo pasar alguna letra.

Las piedras se configuran de esta manera en el programa.

```python
piedras = Magical_Cipher_Disk.Stones([("YELLOW",1),('RED-GREEN',2),("BLUE",1)])
```

Dando una lista que contiene las tuplas de una piedra con su nombre y valor, 

## Estructura Central

==**IMPORTANTE**== :: Esta pieza es Teórica actualmente en el programa, solo "existe" en la versión dibujada a mis jugadores, pero sigue existiendo su mecánica en el programa, pues es donde las piedras se colocan y "configuran".

Esta pieza es un circulo completo y relleno, en el centro de todo el mecanismo, y consta de un hueco en el centro y aparte una separación de 4 partes en su parte solida.

### Uso

- ==**Valor de las piedras**== :: En esta estructura en las 4 partes hay pequeños huecos para colocar las ==**Piedras**==, y cada una de las 4 partes tiene un valor, siendo 1 :: 2 :: 3 :: 4 exactamente, en orden de reloj. Cuando una ==**Piedra**== se coloca en alguna de estos huecos, dependiendo en que parte este esta tendrá ese valor, siendo por lo cual 4 el máximo para una sola piedra. Sin embargo si tienes mas de una misma piedra puedes colocarlas y darle mas valor.
- ==**Hueco Central**== :: Este es donde la piedra amarilla iría, y el valor se le da dependiendo de hacia donde este viendo la piedra con su parte "norte" funcionando como una brújula. Esta su valor máximo en todas las ocasiones es 4 y el mínimo es 1. Si se intenta dar un valor mas alla de 4 funcionara como un reloj y pasara al siguiente, si se da un 5 será 1.

# Funcionamiento Completo

El funcionamiento viene explicado con el código completo en el archivo =="example.py"==.



# To-do

- [ ] Versión Ingles del README.md
- [ ] Imágenes para mayor comprensión
- [ ] Programa/app del disco interactivo