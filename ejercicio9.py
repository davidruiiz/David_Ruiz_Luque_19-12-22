#importamos las librerías de datetime para poder trabajar con fechas
from datetime import datetime
from datetime import timedelta

#creamos la clase Edad
class Edad:

    def __init__(self, edad):
        self.edad = edad

def comprobar_edad(self): #comprobar edad
    if self.edad > 22 and self.edad < 78:
        return True
    else:
        return False

def pedir_edad(): #pide la edad
    while True:
        try:
            edad = int(input("Introduce tu edad: "))
            if edad < 0:
                print("No tienes edad negativa. Intentalo de nuevo")
            else:
                return edad
        except ValueError:
            print("El valor introducido no es un número. Intentalo de nuevo")

def comprobar_edad():
    edad  = pedir_edad()
    if edad > 22 and edad < 78:
        return True
    else:
        return False


def pedir_dia_cumpleaños(): #pedir fecha de cumpleaños
    while True:
        try:
            dia = int(input("Introduce el día de tu cumpleaños: "))
            if dia < 1 or dia > 31:
                print("El día debe estar entre 1 y 31")
            else:
                return dia
        except ValueError:
            print("El valor introducido no es un número. Intentalo de nuevo")

def pedir_mes_cumpleaños():
    while True:
        try:
            mes = int(input("Introduce el mes de tu cumpleaños: "))
            if mes < 1 or mes > 12:
                print("El mes debe estar entre 1 y 12")
            else:
                return mes
        except ValueError:
            print("El valor introducido no es un número. Intentalo de nuevo")


def calcular_lunes(): #calcula el lunes más cercano que coincidirá con el cumpleaños
    dia = pedir_dia_cumpleaños()
    mes = pedir_mes_cumpleaños()
    año = datetime.now().year
    fecha_cumpleaños = datetime(año,mes,dia)
    while fecha_cumpleaños.weekday() != 0:
        fecha_cumpleaños = fecha_cumpleaños + timedelta(days=1)

    return fecha_cumpleaños


#probamos el programa
if __name__ == "__main__":
    edad = Edad(pedir_edad())
    if comprobar_edad():
        print("Tu cumpleaños caerá en un lunes: {}".format(calcular_lunes()))
    else:
        print("¡Oh vaya! No puedes acceder a este programa porque no estas en edad laboral.")