"""
2. Faça um programa que carregue uma matriz 2 x 2, que representa o salário de 4 funcionários, calcule e mostre a soma total 
de todos os elementos que será o montante pago pela empresa a esses funcionários.
"""

matriz_func = [] # ................................................... Lendo a matriz
soma = 0

for lin in range(2): # lin corresponde ao índice das linhas
    vet_linha = []
    for col in range(2): # col cooresponde ao índice das colunas
        vet_linha.append(float(input('Digite o salário['+ str(lin) + '][' + str(col) + ']: ')))
    matriz_func.append(vet_linha)

for lin in range(2):  # .................................. Apresentando a matriz
    for col in range(2):
        soma += matriz_func[lin][col]
print(f'A soma total é de: R$ {soma:.2f}')