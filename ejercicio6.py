import numpy as np
import doctest

def area_circulo(diametro):
    radio = diametro/2
    return (np.pi * radio ** 2)

def area_del_parche(diametro,porcentaje):
    area_prot = area_circulo(diametro)*porcentaje
    return area_prot

def pedir_porcentaje():
    while True:
        try:
            numero = float(input("Introduce el porcentaje de área protegida:"))
            if numero < 0 or numero > 1:
                print("El número debe estar comprendidoentre 0 y 1.")
            else:
                return numero
        except ValueError:
            print("El valor introducido no es un número.")

def pedir_diametro():
    while True:
        try:
            numero = int(input("Introduce el valor del diámetro: "))
            if numero < 0:
                print("El número debe ser positivo.")
            else:
                return numero
        except ValueError:
            print("El valor introducido no es un número.")

def longitud_maxima_cuerda():
    porcentaje = pedir_porcentaje()
    diametro = pedir_diametro()
    area_protejida= area_del_parche(diametro,porcentaje)
    radio= np.sqrt(area_protejida/np.pi)
    longitud = 2*np.pi*radio
    return 'La longitud para que Burro no pueda comer más del {} porciento de pasto longitud debe ser de {} pasos de ogro.'.format(porcentaje*100,round(longitud)) 
    #round redondea el número para que sea un entero

#probamos el código
if __name__ == '__main__':
    print(longitud_maxima_cuerda())
    doctest.testmod()