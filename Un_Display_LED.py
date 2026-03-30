'''
Seguramente has visto un display de siete segmentos.
Es un dispositivo (a veces electrónico, a veces mecánico) diseñado para presentar un dígito decimal utilizando un subconjunto de siete segmentos. 
Tu tarea es escribir un programa que puede simular el funcionamiento de un display de siete segmentos, aunque vas a usar LEDs individuales en lugar de segmentos.
Cada dígito es construido con 13 LEDs (algunos iluminados, otros apagados, por supuesto), así es como lo imaginamos:

  # ### ### # # ### ### ### ### ### ###
  #   #   # # # #   #     # # # # # # # 
  # ### ### ### ### ###   # ### ### # # 
  # #     #   #   # # #   # # #   # # # 
  # ### ###   # ### ###   # ### ### ###
Nota: el número 8 muestra todas las luces LED encendidas.

Tu código debe mostrar cualquier número entero no negativo ingresado por el usuario.
Consejo: puede ser muy útil usar una lista que contenga patrones de los diez dígitos.
'''
def led(a):
    #linea1 = ["####","  #","####", "####","#  #","####","####","####","####","####"]
    #linea2 = ["#  #","  #","   #", "   #","#  #","#   ","#   ","   #","#  #","#  #"]
    #linea3 = ["#  #","  #","####", "  ##","####","####","####","   #","####","####"]
    #linea4 = ["#  #","  #","#   ", "   #","   #","   #","#  #","   #","#  #","   #"]
    #linea5 = ["####","  #","#### ","####","   #","####","####","   #","####","####"]
    num0 = ["####","#  #","#  #","#  #","####"]
    num1 = ["   #","   #","   #","   #","   #"]
    num2 = ["####","   #","####","#   ","####"]
    num3 = ["####","   #","  ##","   #","####"]
    num4 = ["#  #","#  #","####","   #","   #"]
    num5 = ["####","#   ","####","   #","####"]
    num6 = ["####","#   ","####","#  #","####"]
    num7 = ["####","   #","   #","   #","   #"]
    num8 = ["####","#  #","####","#  #","####"]
    num9 = ["####","#  #","####","   #","####"]
    
    
    
    for x in a:
        x = int(x)
        
        print(linea1[x])
        print(linea2[x])
        print(linea3[x])
        print(linea4[x])
        print(linea5[x], sep=' ')
    print(a)


entrada = input("Ingrese un numero: ")
led(entrada)
