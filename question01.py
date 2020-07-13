'''
QUESTÃO 1:
Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número
inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada.
A saída deve ser conforme o exemplo abaixo:
Tabuada de 5:
5 X 1 = 5
5 X 2 = 10
5 X 3 =30
...
5 X 10 = 50
Obs: A entrada só deve aceitar de 1 a 10, se for um numero diferente perguntar
novamente até que seja dentro do intervalo correto.
'''


num = int(input("Informe um número inteiro, de 1 a 10: "))

while num < 1 or num > 10:
    num = int(input("Informe um número inteiro válido, de 1 a 10: "))

print("Tabuada de {}:".format(num))
for i in range(1, 11):
    print("{} X {} = {}".format(num, i, num*i))
