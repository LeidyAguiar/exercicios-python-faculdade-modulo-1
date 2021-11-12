"""
4. Faça um programa para armazenar em uma matriz 5x2 preços. Encontre e apresente os ÍNDICES dos valores menores que 23 reais.
"""

matriz = []
cont_abaixo = 0 # ................................................... Lendo a matriz
for lin in range(5): # lin corresponde ao índice das linhas
    vet_linha = []
    for col in range(2): # col cooresponde ao índice das colunas
        vet_linha.append(float(input('Digite o valor R$ ['+ str(lin) + '][' + str(col) + ']: ')))
    matriz.append(vet_linha)
    
for lin in range(5):  # .................................. Apresentando a matriz
    for col in range(2):
        if matriz[lin][col] < 23:
            print(f'O produto que está na linha {lin} e na coluna {col} custa menos que R$ 23,00')

