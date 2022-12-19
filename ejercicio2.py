
#Ejemplos:

#simplify("3x-zx+2xy-x") debe devolver "y^2+3x"
#simplify("-y+x-5yz+3xy-x") debe devolver "-4y^2+2xy"



def simplify(polinomio):
    #separo los terminos
    terminos = polinomio.split("+")
    #separo los coeficientes de las variables
    coeficientes = []
    variables = []
    for termino in terminos:
        coeficientes.append(termino[:-1])
        variables.append(termino[-1])
    #separo los exponentes de las variables
    exponentes = []
    for variable in variables:
        if variable.isalpha():
            exponentes.append(1)
        else:
            exponentes.append(int(variable[1:]))
    #separo las variables
    variables = []
    for variable in variables:
        if variable.isalpha():
            variables.append(variable)
        else:
            variables.append(variable[0])
    #simplifico los exponentes
    for i in range(len(exponentes)):
        if exponentes[i] == 2:
            exponentes[i] = 1
            variables[i] = variables[i] * 2
    #simplifico los coeficientes
    for i in range(len(coeficientes)):
        if coeficientes[i] == "1":
            coeficientes[i] = ""
        elif coeficientes[i] == "-1":
            coeficientes[i] = "-"
        elif coeficientes[i] == "-":
            coeficientes[i] = "-"
        elif coeficientes[i] == "+":
            coeficientes[i] = "+"
    #simplifico los exponentes
    for i in range(len(exponentes)):
        if exponentes[i] == 1:
            exponentes[i] = ""
    #simplifico las variables
    for i in range(len(variables)):
        if variables[i] == "1":
            variables[i] = ""
    #junto los terminos
    terminos = []
    for i in range(len(coeficientes)):
        terminos.append(coeficientes[i] + variables[i] + str(exponentes[i]))
    #junto los terminos
    polinomio = ""
    for termino in terminos:
        polinomio = polinomio + termino + "+"
    #elimino el ultimo +
    polinomio = polinomio[:-1]
    return polinomio
    

if __name__=="__main__":
    print(simplify("3x-zx+2xy-x"))