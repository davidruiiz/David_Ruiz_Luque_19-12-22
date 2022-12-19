#escribir una función llamada do_math que reciba un solo argumento. Este argumento es una cadena que contiene varios números delimitados por espacios en blanco. 

#La función debe devolver una cadena que contiene los números del argumento, ordenados de menor a mayor, y separados por un solo espacio en blanco. Si dos números son iguales, el orden en que aparecen en la cadena de entrada es el que debe mantenerse en la cadena de salida.

#Por ejemplo, si la función recibe la cadena "4a 3b 2c 1d", debe devolver la cadena "1d 2c 3b 4a".

#Si la función recibe la cadena "28a 14b 28c", debe devolver la cadena "14b 28a 28c".

#Si la función recibe la cadena "ab1 cd2 ef3 gh4", debe devolver la cadena "ab1 cd2 ef3 gh4".



def do_math(cadena):
    #separo los numeros
    numeros = cadena.split(" ")
    #separo los numeros de las letras
    numeros2 = []
    letras = []
    for numero in numeros:
        numeros2.append(numero[:-1])
        letras.append(numero[-1])
    #ordeno los numeros
    numeros2.sort()
    #junto los numeros
    numeros = []
    for i in range(len(numeros2)):
        numeros.append(numeros2[i] + letras[i])
    #junto los numeros
    cadena = ""
    for numero in numeros:
        cadena = cadena + numero + " "
    # Cada número tiene una sola letra del alfabeto en algún lugar dentro de él.
    return cadena
    


if __name__ == '__main__':
    print(do_math("4a 3b 2c 1d"))
    print(do_math("28a 14b 28c"))
    print(do_math("ab1 cd2 ef3 gh4"))
    

