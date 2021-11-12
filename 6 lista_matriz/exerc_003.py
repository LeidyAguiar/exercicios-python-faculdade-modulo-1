"""
3. Faça um programa que carregue uma matriz 3 x 2, que representa preços de produtos, crie OUTRA matriz que armazene todos os preços com 7% de aumento.
"""

matriz = [] # ................................................... Lendo a matriz

for lin in range(3): # lin corresponde ao índice das linhas
    vet_linha = []
    for col in range(2): # col cooresponde ao índice das colunas
        vet_linha.append(float(input('Digite o preço dos produtos['+ str(lin) + '][' + str(col) + ']: ')))
    matriz.append(vet_linha)
    
for lin in range(3):  # .................................. Apresentando a matriz
    for col in range(2):
        print(matriz[lin][col], end='\t')
    print()

# 7 % de aumento  
matriz_2 = [] # ................................................... Lendo a matriz
for lin in range(3): # lin corresponde ao índice das linhas
    vet_linha = []
    for col in range(2): # col cooresponde ao índice das colunas
        vet_linha.append(matriz[lin][col] + matriz[lin][col]  * (7 / 100)) 
    matriz_2.append(vet_linha)

for lin in range(3):  # .................................. Apresentando a matriz
    for col in range(2):
        print('Aumento dos preços: ',matriz_2[lin][col], end='\t')
    print()
