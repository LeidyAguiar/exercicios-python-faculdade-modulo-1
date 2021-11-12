"""
2. Construir um algoritmo para calcular e apresentar a idade atual de algumas pessoas em relação ao ano atual, mas não é informado a quantidade de pessoas, 
então use como critério de parada (condição da estrutura de repetição, digitar zero no ano de nascimento para sair.
"""
ano_nascimento = int(input('Informe o ano de nascimento: '))
ano_atual = 2021

while ano_nascimento > 0:
    idade_atual = ano_atual - ano_nascimento
    print('A sua idade atual é:',idade_atual)

    ano_nascimento = int(input('Informe o ano de nascimento: '))