'''
Ya conoces como funiona el método split(). Ahora queremos que lo pruebes.
Tu tarea es escribir tu propia función, que se comporte casi como el método original split(), por ejemplo:

*  Debe aceptar únicamente un argumento: una cadena.
*  Debe devolver una lista de palabras creadas a partir de la cadena, dividida en los lugares donde la cadena contiene espacios en blanco.
*  Si la cadena está vacía, la función debería devolver una lista vacía.
*  Su nombre debe ser mysplit().

Utiliza la plantilla en el editor. Prueba tu código con cuidado.
'''
def mysplit(a):
    b = []
    c = []
    x = ""
    solo_espacios = False
    if len(a) == 0:
        if len(a) == 0:
            return b
        else:
            for ch in a:
                if ch == chr(32):
                    solo_espacios = True
        if solo_espacios == True:
            return c
    else:
        for i in range(len(a)):
            if (a[i] == chr(32)):
                b.append(x)
                x = ""
            else:
                x += a[i]
        b.append(x)
        for z in b:
            if z != '':
                c.append(z)
    del b        
    return c

cadena = input("Ingrese una cadena: ")
print(mysplit(cadena))
print(mysplit("Ser o no ser, esa es la cuestión"))
print(mysplit("Ser o no ser, esa es la cuestión"))
print("Esta cadena es solo espacios: ", mysplit2("   "))
print("Esta cadena tiene espacio al final y principio: ", mysplit(" abc "))
print("Esta cadena esta vacia: ", mysplit(""))
