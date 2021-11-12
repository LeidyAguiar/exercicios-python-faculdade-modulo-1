"""
6. Faça um algoritmo que receba a idade de 10 pessoas, calcule e exiba a quantidade de pessoas maiores de idade, 
sendo que a maioridade é obtida após completar 18 anos. Pode implementar com o comando while ou for.
"""

# Usando For
print('Exemplo com o for')
contador_idade_maior = 0
for contador in range(10):
    idade = int(input('Digite sua idade: '))
    if idade >= 18:
        contador_idade_maior = contador_idade_maior + 1
print('São maiores de idade:',contador_idade_maior, 'pessoas')