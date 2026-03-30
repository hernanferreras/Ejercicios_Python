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
    #linea1 = ["####","  # ","####", "####","#  #","####","####","####","####","####"]
    #linea2 = ["#  #"," ## ","   #", "   #","#  #","#   ","#   ","   #","#  #","#  #"]
    #linea3 = ["#  #","  # ","####", "  ##","####","####","####","   #","####","####"]
    #linea4 = ["#  #","  # ","#   ", "   #","   #","   #","#  #","   #","#  #","   #"]
    #linea5 = ["####","####","#### ","####","   #","####","####","   #","####","####"]
    num0 = ["####","#  #","#  #","#  #","####"]
    num1 = ["  # "," ## ","  # ","  # ","####"]
    num2 = ["####","   #","####","#   ","####"]
    num3 = ["####","   #","  ##","   #","####"]
    num4 = ["#  #","#  #","####","   #","   #"]
    num5 = ["####","#   ","####","   #","####"]
    num6 = ["####","#   ","####","#  #","####"]
    num7 = ["####","   #","   #","   #","   #"]
    num8 = ["####","#  #","####","#  #","####"]
    num9 = ["####","#  #","####","   #","####"]
    
    dic = {"0": num0, "1":num1, "2":num2, "3":num3, "4":num4, "5":num5, "6":num6, "7":num7, "8":num8, "9":num9}

    for ch in a:
       for x in dic[ch]:
           print(x)
   
numero = input("Ingrese un numero: ")
led(numero)



entrada = input("Ingrese un numero: ")
led(entrada)
