"""
5. Faça um programa que leia números inteiros m e n e os elementos de uma matriz A de números inteiros de dimensão m x n e conte o número de elementos que são iguais a zero.
"""

m = int(input('Digite um número(m) inteiro: '))
n = int(input('Digite um número(n) inteiro: '))

matriz = []
qtde = 0
for lin in range(m): 
    vet_linha = []
    for col in range(n):
        vet_linha.append(float(input('Digite o valor ['+ str(lin) + '][' + str(col) + ']: ')))
    matriz.append(vet_linha)

for lin in range(m): 
    for col in range(n):
        print(matriz[lin][col], end='\t')
        if matriz[lin][col] == 0:
            qtde += 1           
print('\nO número de elementos iguais a zero são:',qtde)