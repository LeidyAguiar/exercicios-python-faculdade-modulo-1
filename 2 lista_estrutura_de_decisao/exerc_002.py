"""
2. Faça um algoritmo que leia o nome e a idade de uma pessoa, verifique se a idade de uma pessoa é menor ou maior de 
idade. Considera-se maior de idade uma pessoa com 18 anos ou mais. 
Como saída o algoritmo deve informar o nome e a idade da pessoa e depois uma mensagem se ela é ou não maior de idade.
"""

nome = str(input('Informe seu nome: '))
idade = int(input('Informe sua idade: '))
print(f'Seu nome é {nome} e você tem {idade} anos')
if idade >= 18:
    print('Você é maior de idade')
else:
    print('Você é menor de idade')