"""
1. Utilize a linguagem de programação PYTHON. Crie um programa que leia o ano de nascimento de uma pessoa e o ano atual, calcule e mostre a idade da pessoa em:
    a) anos
    b) meses
"""
#entrada
ano_nascimento = int(input('Informe seu ano de nascimento: '))
ano_atual = int(input('Informe o ano atual: '))

#processamento
idade_atual = ano_atual - ano_nascimento

#saída
print('A sua idade é de:', idade_atual,'anos')
print('A sua idade em meses é:',idade_atual * 12)