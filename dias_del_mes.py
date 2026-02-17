'''
Tu tarea es escribir y probar una función que toma dos argumentos (un año y un mes) y devuelve el número de días del mes/año dado 
(mientras que solo febrero es sensible al valor year, tu función debería ser universal).
La parte inicial de la función está lista. Ahora, haz que la función devuelva None si los argumentos no tienen sentido.
Por supuesto, puedes (y debes) utilizar la función previamente escrita y probada (LAB 4.3.1.6). Puede ser muy útil. Te recomendamos que utilices una lista con los meses. Puedes crearla dentro de la función - este truco acortará significativamente el código.
Hemos preparado un código de prueba. Amplíalo para incluir más casos de prueba.
'''
def is_year_leap(year):
#
# Tu código del LAB anterior.
  if (year % 4 == 0) and (year % 400 == 0 or year % 100 != 0):
    return True
  else: 
    return False
#

def days_in_month(year, month):
    #
    # Escribe tu código nuevo aquí.
    dias_meses = [29, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    else:
        x = is_year_leap(year)
        if x == True:
            return 29
        else:
            return 28
    #

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Fallido")
