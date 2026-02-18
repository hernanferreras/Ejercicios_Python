'''
Tu tarea es escribir y probar una función que toma tres argumentos (un año, un mes y un día del mes) y devuelve el día correspondiente del año, 
o devuelve None si cualquiera de los argumentos no es válido.
Debes utilizar las funciones previamente escritas y probadas. Agrega algunos casos de prueba al código. Esta prueba es solo el comienzo.
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
    # Tu código del LAB anterior.
    month_31 = [1, 3, 5, 7, 8, 10, 12]
    month_30 = [4, 6, 9, 11]
    if month in month_31:
        return 31
    elif month in month_30:
        return 30
    else:
        if is_year_leap(year) == True:
            return 29
        else:
            return 28
    #

def day_of_year(year, month, day):
    #
    # Escribe tu código nuevo aquí.
    if year < 1582 or month < 1 or month > 12 or day > 31:
        return None
    else:
        while 
    #

print(day_of_year(2000, 12, 31))
