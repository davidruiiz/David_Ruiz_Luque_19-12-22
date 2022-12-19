import doctest
#creamos un diccionario con los numeros del 0 al 9 en ingles
diccionario = {
            1: 'one',
            2: 'two',
            3: 'three',
            4: 'four',
            5: 'five',
            6: 'six',
            7: 'seven',
            8: 'eight',
            9: 'nine'
            }


#la siguiente funcion nos separa los digitos del numero en una lista
def separar_numero_lista(n):
    lista = []
    while n > 0:
        lista.append(n % 10)
        n = n // 10
    lista.reverse()
    return lista

if __name__ == '__main__':
    print(separar_numero_lista(1234))
    doctest.testmod()
