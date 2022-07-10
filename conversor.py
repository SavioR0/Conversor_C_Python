from operator import index
import re


operadores = ["+", "-", "*", "/", "%"]
tipos = ["int", "float", "double", "char", "bool"]
inteiros = "[0-9]*"
floats = "[\d*].[\d*]"
doubles = "[\d*].[\d*]"
names = "\D[a-zA-z0-9]*"


def conversor(arq):
    arq = open(arq, 'r')
    arqPy = open("codigoPython.txt", "w")

    for x in arq:
        x = x.strip()
        lista = x.split()

        for x in lista:
            if ';' in x:
                ponto = x.split(";")
                lista.remove(x)
                lista.append(ponto[0])
            if x in tipos and "()" not in lista:
                lista.remove(x)
        print(lista)

        if 'int' in lista:
            for x in lista:
                if x in tipos:
                    arqPy.write("def ")
                elif x == '{':
                    arqPy.write(':\n')
                else:
                    arqPy.write("{} ". format(x))
        elif '=' in lista or operadores in lista:
            aux = 0
            for x in lista:
                if aux == 0:
                    print("Entrou")
                    arqPy.write("    ")
                if x in operadores or re.match(r"\d", x) != None or x == '=' or re.match(names, x):
                    arqPy.write("{} " .format(x))
                else:
                    arqPy.write("{} ". format(x))
                aux = aux + 1
            arqPy.write("\n")
        elif 'return' in lista:
            arqPy.write("    ")
            for x in lista:
                arqPy.write("{} ".format(x))

    arqPy.write("\nmain()")
    arq.close()
    arqPy.close()


conversor("codigos/Código 4.txt")
