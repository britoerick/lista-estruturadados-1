'''
QUESTÃO 3
Faça um programa que leia os dados de 3 alunos (Nome e Media Final), armazenando
em um dicionário onde o nome do aluno é a chave e a média do aluno o valor. Uma vez
lidos os dados, imprima a lista de alunos em ORDEM ALFABÉTICA com sua respectiva
nota final e dizendo se foi aprovado ou reprovado (considere aprovado media final maior
ou igual a 5.0).
Regra:
1. Utilize uma função para checar se o aluno foi reprovado ou aprovado
Exemplo de saída:
João, nota 8.0, Aprovado
Maria, nota: 5.5 , Aprovado
José, nota 4.5, Reprovado
'''

alunos = {'João': 8.0, 'Maria': 5.0, 'José': 4.9}

for alkey in alunos.keys():

    if alunos[alkey] >= 5.0:
        print(alkey, ", nota: ", alunos[alkey], ", Aprovado")

    else:
        print(alkey, ", nota: ", alunos[alkey], ", Reprovado")
