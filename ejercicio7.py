#importamos las librerías
import doctest
import numpy as np

class Caballo:
    
    tablero=np.full((8,8),' ')
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __str__(self) -> str:
        
        return f'El caballo se encuentra en la posición {self.x1},{self.y1} y quiere llegar a la posición {self.x2},{self.y2}'

    
    def numero_de_movimientos(x1,y1,x2,y2):
        if x1 == x2 and y1 == y2:
            return 0
        if (x1 + y1) % 2 == (x2 + y2) % 2:
            #si la distancia entre las posiciones es igual en x e y 
            if abs(x1 - x2) == abs(y1 - y2): #utilizamos la función abs para obtener el valor absoluto de la resta, es decir, la distancia entre las posiciones
                return 'El menor número de movimientos es 1'
            else:
                return 'El menor número de movimientos es 2'
        else:
            return "No se puede llegar"


    #probamos el código
    if __name__ == '__main__':
        print(tablero)
        print(numero_de_movimientos(1,1,2,3))
        print(numero_de_movimientos(1,1,4,6))
        doctest.testmod()

