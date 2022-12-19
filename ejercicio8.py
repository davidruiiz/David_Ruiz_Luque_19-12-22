#importamos las librerías
import doctest
import re

#Creamos para encontrar si es el monstruo del Lago Ness
def buscar_coincidencia(texto):
    texto = texto.lower()
    if 'three fifty' in texto or '3.50' in texto or 'tree fiddy' in texto:
        return 'Es el monstruo del Lago Ness.'
    else:
        return 'No es el monstruo del Lago Ness.'


texto = input('Introduce una oración: ')
    
#Llamamos a la función main
if __name__ == '__main__':
    print(buscar_coincidencia(texto))
    doctest.testmod() #hacemos el test