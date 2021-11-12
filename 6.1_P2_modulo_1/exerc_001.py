"""
1. Em Python, crie um programa que leia a quantidade de linhas e colunas de uma matriz, digite valores int e verifique/apresente se ela "é simétrica" ou "não é simétrica". 
Uma matriz é considerada simétrica quando a quantidade de linhas é igual a quantidade de colunas. Mostre a matriz no formato de linha e colunas, conforme foi visto em aula.
"""

l = int(input('Digite um número de linhas: '))
c = int(input('Digite um número de colunas: '))

matriz = []

for lin in range(l):
    vet_linha = []
    for col in range(c):
        vet_linha.append(int(input('Digite um número ['+ str(lin) + '][' + str(col) + ']: ')))
    matriz.append(vet_linha)

for lin in range(l):
    for col in range(c):
        print(matriz[lin][col], end='\t')
    print()
if l == c:
    print('é simétrica')
else:
    print('não é simétrica')


