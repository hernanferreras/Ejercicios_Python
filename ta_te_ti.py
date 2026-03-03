'''
PROYECTO  Tic-Tac-Toe
Escenario
Tu tarea es escribir un simple programa que simule jugar a tic-tac-toe (nombre en inglés) con el usuario. 
Para hacerlo más fácil, hemos decidido simplificar el juego. Aquí están nuestras reglas:

* la maquina (por ejemplo, el programa) jugará utilizando las 'X's;
* el usuario (por ejemplo, tu) jugarás utilizando las 'O's;
* el primer movimiento es de la maquina - siempre coloca una 'X' en el centro del tablero;
* todos los cuadros están numerados comenzando con el 1 (observa el ejemplo para que tengas una referencia)
* el usuario ingresa su movimiento introduciendo el número de cuadro elegido - el número debe de ser valido, por ejemplo un valor entero mayor que 0 y menor que 10, y no puede ser un cuadro que ya esté ocupado;
* el programa verifica si el juego ha terminado - existen cuatro posibles veredictos: el juego continua, el juego termina en empate, tu ganas, o la maquina gana;
* la maquina responde con su movimiento y se verifica el estado del juego;
* no se debe implementar algún tipo de inteligencia artificial - la maquina elegirá un cuadro de manera aleatoria, eso es suficiente para este juego.
El ejemplo del programa es el siguiente:

+-------+-------+-------+
|       |       |       |
|   1   |   2   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+
Ingresa tu movimiento: 1
+-------+-------+-------+
|       |       |       |
|   O   |   2   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+
Ingresa tu movimiento: 8
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   O   |   9   |
|       |       |       |
+-------+-------+-------+
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   O   |   9   |
|       |       |       |
+-------+-------+-------+
Ingresa tu movimiento: 4
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   O   |   9   |
|       |       |       |
+-------+-------+-------+
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   O   |   9   |
|       |       |       |
+-------+-------+-------+
Ingresa tu movimiento: 7
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   O   |   O   |   9   |
|       |       |       |
+-------+-------+-------+
¡Has Ganado!

Requerimientos
Implementa las siguientes características:

El tablero debe ser almacenado como una lista de tres elementos, mientras que cada elemento es otra lista de tres elementos (la lista interna representa las filas) 
de manera que todos los cuadros puedas ser accedidos empleado la siguiente sintaxis:

board[row][column]
 
Cada uno de los elementos internos de la lista puede contener 'O', 'X', o un digito representando el número del cuadro (dicho cuadro se considera como libre)
la apariencia de tablero debe de ser igual a la presentada en el ejemplo.
implementa las funciones definidas para ti en el editor.

Para obtener un valor numérico aleatorio se puede emplear una función integrada de Python denominada randrange(). 
El siguiente ejemplo muestra como utilizarla (El programa imprime 10 números aleatorios del 1 al 8).
Nota: la instrucción from-import provee acceso a la función randrange definida en un módulo externo de Python denominado random.

from random import randrange
 
for i in range(10):
    print(randrange(8))
'''
from random import randrange

#Funcion que muestra el estado actual del tablero
def display_board(board):
    line_1 = "+-------"*3+"+"   
    line_2 = "|       "*3+"|" 
    for i in range(len(board)):
        print(line_1)
        print(line_2)
        for j in range(len(board[i])):
            print("|  ",board[i][j],"  ",end="")
        print("|\n"+line_2)
    print(line_1)
    
def make_list_of_free_fields(board):
    # La función examina el tablero y construye una lista de todos los cuadros vacíos.
    # La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna
    empty_spaces = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]!= "X" and board[i][j]!= "O":
                empty_spaces.append((i,j))
    return empty_spaces

# La función acepta el estado actual del tablero y pregunta al usuario
# acerca de su movimiento, verifica la entrada y actualiza el tablero
# acorde a la decisión del usuario.
def enter_move(board):
    

def jugada():
    a = int(input("Ingresa tu movimiento:"))
    return a

board = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]
posiciones_ocupadas = [5,]
juego = True
contador_jugada = 1
#line_1 = "+-------"*3+"+"
#line_2 = "|       "*3+"|" 

display_board(board)


#def victory_for(board, sign):
    # La función analiza el estatus del tablero para verificar si 
    # el jugador que utiliza las 'O's o las 'X's ha ganado el juego.


#def draw_move(board):
    # La función dibuja el movimiento de la máquina y actualiza el tablero.



    
