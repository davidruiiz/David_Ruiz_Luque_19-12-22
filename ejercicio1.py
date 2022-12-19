

#https://github.com/davidruiiz/David_Ruiz_Luque_19-12-22.git

import doctest

class Nonograma:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.matriz = []
        for i in range(len(filas)):
            self.matriz.append([])
            for j in range(len(columnas)):
                self.matriz[i].append(0)
    def __str__(self):
        s = ""
        for i in range(len(self.filas)):
            s += str(self.filas[i]) + "\n"
        s += "\n"
        for i in range(len(self.columnas)):
            s += str(self.columnas[i]) + "\n"
        s += "\n"
        for i in range(len(self.matriz)):
            s += str(self.matriz[i]) + "\n"
        return s


