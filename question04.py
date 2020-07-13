'''
QUESTÃO 4
Um número é dito perfeito se é igual à soma de todos os seus divisores próprios (todos
os divisores menos ele). Por exemplo, como os divisores próprios de 6 são 1, 2, 3 e e 1
+ 2 + 3 = 6, 6 é perfeito. A matemática ainda não sabe se a quantidade de números
perfeitos é ou não finita e, por isso, há programas de computador que buscam encontrar
números perfeitos grandes. Escreva um programa PYTHON utilizando sub-rotinas
(funções), que leia dois valores a e b e encontre os números perfeitos compreendidos
dentro desse intervalo.
Entrada: 0 e 30
Saída esperada: 6 , 28
'''

def verificador(valor):

    aux = valor
    auxLista = divisor(valor)
    auxNum = somar(auxLista)

    if (auxNum == aux):
        return auxNum


def divisor(valor):
    n1 = valor
    aux = valor

    lista = []

    for i in range(n1):
        n1-=1
        if (n1 != 0):
            if (aux%n1 == 0):
                lista.append(n1)

    return lista


def somar(lista):

    num = sum(lista)

    return (num)

## main ##

num1 = int(input("Informe o número do início do intervalo: "))
num2 = int(input("Informe o número do fim do intervalo: "))
numeros = []

for num1 in range(num1, num2+1):
    if(num1 != 0):
        aux = verificador(num1)

        if(aux == num1):
            numeros.append(aux)


print(str(numeros)[1:-1])
