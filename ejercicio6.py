import numpy as np
import doctest

def area(diametro):
    radio = diametro/2
    return (np.pi * radio ** 2)

def area_protegida(diametro,porcentaje):
    area_prot = area(diametro)*porcentaje
    return area_prot



