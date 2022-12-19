
#Cree una función hollow_triangle(altura) que devuelva un triángulo hueco de la altura correcta. La altura se pasa a través de la función y la función debe devolver una lista que contiene cada línea del triángulo hueco.

#Ejemplo:
#>>> hollow_triangle(6)
#['____#____', '___#_#___', '__#___#__', '_#_____#_', '#########']
#>>> hollow_triangle(9)
#['________#________', '_______#_#_______', '______#___#______', '_____#_____#_____', '____#_______#____', '___#_________#___', '__#___________#__', '_#_____________#_', '#################']

import doctest

class Triangulo: #creo la clase


    def __init__(self,altura):
        self.altura = altura
        self.lista = []
        self.lista.append('_'*(altura-1)+'#'+'_'*(altura-1))
        for index in range(altura):
            if index != altura-1:
                self.lista.append('_'*(altura-index-1)+'#'+'_'*(2*index-1)+'#'+'_'*(altura-index-1))
            else:
                self.lista.append('#'*(2*altura-1))
    def __str__(self):
        return str(self.lista)
    def __repr__(self):
        return str(self.lista)

    def hollow_triangle(altura):
    
        lista = []
        for index in range(altura):
            if index == 0:
                lista.append('_'*(altura-index-1)+'#'+'_'*(altura-index-1))
            elif index != altura-1:
                lista.append('_'*(altura-index-1)+'#'+'_'*(2*index-1)+'#'+'_'*(altura-index-1))
            else:
                lista.append('#'*(2*altura-1))
        return lista

    #probamos el código
    if __name__ == '__main__':
        print(hollow_triangle(6))
        for  i in hollow_triangle(6): #imprtimimos cada elemento de la lista
            print(i)
        print(hollow_triangle(9))
        for  i in hollow_triangle(9): #imprtimimos cada elemento de la lista
            print(i)
        doctest.testmod()
