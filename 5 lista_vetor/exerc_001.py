"""
1. Faça um programa que calcule e apresente a média de idades de uma sala de 35 alunos.​​
"""

print('Exemplo de leitura de vetor com o for')
vetor_idade = [] # declarando a variável como vetor vazio - fora da estrutura de repetição
soma_idade = 0

for i in range(5):
    vetor_idade.append(int(input('Informe a idade do aluno: ')))
    soma_idade = soma_idade + vetor_idade[i]
media = soma_idade / len(vetor_idade)
print('valor da variável indice:',i,'  Quantidade de elementos:',len(vetor_idade),'   Média de idades:',media)

for i in range(len(vetor_idade)):
    print(vetor_idade[i], end='  ')
print('\n',vetor_idade)

