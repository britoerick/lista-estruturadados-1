'''
QUESTÃO 5
Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da direita
para esquerda ou vice−versa. Por exemplo: OSSO e OVO são palíndromos. Em textos
mais complexos os espaços e pontuação são ignorados. A frase SUBI NO ONIBUS é o
exemplo de uma frase palíndroma onde os espaços foram ignorados. Faça um
programa que leia uma seqüência de caracteres, mostre−a e diga se é um palíndromo
ou não.
'''

import pilha as pilha
from unidecode import unidecode


def palindromoPilha(array):
    auxA = []
    auxB = []

    if pilha.isEmpty(array):
        print("String vazia")

    else:
        print("\n*************** teste de palíndromo ***************")
        print('Verificar: ' + array)

        # Remover acentos
        array = unidecode(array)

        # Deixar letras minúsculas, pois evita erro de comparação
        array = array.lower()

        # Verificar se contém espaço e remover
        if " " in array:
            array = array.replace(" ", "")

        loop = ((pilha.size(array)) - 1)
        for i in range(loop, -1, -1):
            auxA = pilha.push(array[i], auxA)
            auxB = pilha.push(array[loop - i], auxB)

        if auxA == auxB:
            print("Teste Verdadeiro")
            return True

        else:
            print("Teste Falso")
            return False


# Função Palíndromo utilizando estrutura de pilha

print("\n********** Função de Palíndromo **********")

palin = ['ralo do dólar', 'até o poeta', 'tomarei café após a sopa']

for i in range(len(palin)):
    palindromoPilha(palin[i])