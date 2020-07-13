'''
QUESTÃO 2
Analisando matematicamente as mortes do 7 reinos, o conselheiro Robert descobriu
que elas acontecem exponencialmente da seguinte forma: As mortes acontecem
exponencialmente de acordo com o número de famílias envolvidas nas batalhas e o
tempo. De acordo com o diagrama abaixo. Portanto, escreva um programa no qual a
entrada **n** representa o número de família e o resultado seja a seguinte tabela:
1 (1 família, nenhuma morte)
2 4 (2 familias, 4 mortes no primeiro ano)
3 6 9 (3 familias, 6 mortes no primeiro ano, 9 mortes no segundo ano)
4 8 12 16
n...
obs: o programa deve imprimir somente a tabela, sem os comentários
'''

num = int(input("Informe o número de famílias envolvidas nas batalhas: "))
aux = num


for i in range(1, num+1):
    aux2 = i
    for x in range(i):
        print(i, end="")
        i = i + aux2

    print("")
