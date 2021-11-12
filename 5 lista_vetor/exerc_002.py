"""
2. Faça um programa que calcule e apresente a média de alturas de uma sala de 35 alunos. Informe também quantos alunos e quais (índice/posição) 
são os que possuem idade superior a 25 anos.​ Use dois vetores, um para altura e outro para idade. Não use nenhuma função pronta da linguagem Python.
"""

vet_altura = []
vet_idade = []
cont_alunos = 0
cont_altura = 0
soma_altura = 0

for i in range(3):
    vet_idade.append(int(input('Informe a idade: ')))
    vet_altura.append(float(input('Informe a altura: ')))
    soma_altura = soma_altura + vet_altura[i]
    if vet_idade[i] > 25:
        cont_alunos += 1
print(f'A quantidade de alunos maiores de 25 anos é: {cont_alunos}')
media = soma_altura / len(vet_altura)
print(f'Média de alturas: {media:.2}')

