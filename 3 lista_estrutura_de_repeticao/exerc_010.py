"""
10. Elabore um algoritmo que calcule e informe a média de idades de 5 alunos.Pode implementar com o comando while ou for.
"""

# Usando while
print('Exemplo com o while')
i = 0
soma = 0
while i < 5:
    idade = int(input('Informe a idade: '))
    soma = soma + idade
    i += 1
media = soma / 5
print('A média das idades é:',media)