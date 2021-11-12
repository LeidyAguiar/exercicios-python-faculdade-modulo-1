"""
1. Faça um programa que leia uma matriz 2x3 (2 linhas, 3 colunas). Apresenta os elementos da matriz e seus respectivos índices.
"""

matriz = [] # ................................................... Lendo a matriz
for lin in range(2): # lin corresponde ao índice das linhas
    vet_linha = []
    for col in range(3): # col cooresponde ao índice das colunas
        vet_linha.append(int(input('Digite o valor ['+ str(lin) + '][' + str(col) + ']: ')))
    matriz.append(vet_linha)

for lin in range(2):  # .................................. Apresentando a matriz
    for col in range(3):     
        print(matriz[lin][col], end='\t')
    print()

for lin in range(len(matriz)):  # a função len(matriz), possui a quantidade de linhas
    for col in range(len(matriz[0])): # a função len(matriz[0]), possui a quantidade de colunas
        print('O elemento ',matriz[lin][col], ' está na linha',lin,' e na coluna',col)
