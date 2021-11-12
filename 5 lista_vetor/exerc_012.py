"""
12. Faça um programa que:
    * preencha um vetor com quinze elementos inteiros
    * verifique a existência de elementos iguais a 30, mostrando os índices/posições em que apareceram.
"""

vet_inteiro = []

for i in range(15):
    vet_inteiro.append(int(input('Digite números inteiros: ')))
    
for i in range(len(vet_inteiro)):
    if vet_inteiro[i] == 30:
        print('número' ,vet_inteiro[i], 'está na posição',i)
print('Numeros:',vet_inteiro)