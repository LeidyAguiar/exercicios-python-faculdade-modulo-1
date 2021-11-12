"""
7. Faça um algoritmo que calcule e apresente a média de alturas superior a 1,80 de 10 alunos. Informe também quantos e quais (índice/posição) são os alunos.
Não use nenhuma função pronta da linguagem Python.
"""

vet_altura_alunos = []
soma_media = 0
altura_superior = 0

for i in range(5):
    vet_altura_alunos.append(float(input('Informe a altura do aluno: ')))
    if vet_altura_alunos[i] > 1.80:
        soma_media = soma_media + vet_altura_alunos[i]
        altura_superior += 1
    
media = soma_media / altura_superior
print(f'Média altura: {media:.2f}')
print('Quantidade de alunos com altura superior: ',altura_superior)

for i in range(len(vet_altura_alunos)):
    if vet_altura_alunos[i] > 1.80:
        print('Altura=',vet_altura_alunos[i],'na posição',i, end='\t')

