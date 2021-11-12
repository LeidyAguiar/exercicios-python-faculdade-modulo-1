"""
4. Faça um programa que carregue um vetor com a média de dez alunos, calcule e mostre a MÉDIA DA SALA e quantos alunos estão acima e abaixo da média da sala.
"""

vet_media_alunos = []
soma_media = 0
acima_da_media = 0
abaixo_da_media = 0

for i in range(3):
    vet_media_alunos.append(float(input('Informe a nota do aluno: ')))
    soma_media = soma_media + vet_media_alunos[i]
    if vet_media_alunos[i] >= 6:
        acima_da_media += 1
    else:
        abaixo_da_media += 1
media = soma_media / len(vet_media_alunos)
print(f'A média da sala é: {media:.2f}')
print('Quantidade de alunos acima da média: ',acima_da_media)
print('Quantidade de alunos abaixo da média: ',abaixo_da_media)