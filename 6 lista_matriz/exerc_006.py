"""
6. Faça um programa que carregue: *um vetor com oito posições com os nomes das lojas; * um outro vetor com quatro posições com os nomes dos produtos; 
* uma matriz com os preços de todos os produtos em cada loja. O programa deve mostrar todas as relações (nome do produto – nome da loja) nas quais o preço 
não ultrapasse R$ 120,00. Escolha qual é o tipo da função que quer.
"""

matriz = []
vetor_lojas = []
vetor_produtos = []

# popular vet lojas
for i in range(3): 
    vetor_lojas.append(str(input('Digite o nome da loja: ')))
print()

# popular vetor de produtos
for i in range(2):
    vetor_produtos.append(str(input('Digite o nome do produto: ')))
print()

# popular matriz de precos
for lin in range(len(vetor_produtos)): 
    vetor_lin_precos = []
    for col in range(len(vetor_lojas)):
        vetor_lin_precos.append(float(input('Digite o valor do produto: ' + vetor_produtos[lin] + ' loja ' + vetor_lojas[col] + ': ')))
    matriz.append(vetor_lin_precos)
print()

# exibir matriz mostrando prod - loj e val < 120
for lin in range(len(vetor_produtos)):
    for col in range(len(vetor_lojas)):
        if matriz[lin][col] < 120:
            print(f'O produto {vetor_produtos[lin]} da loja {vetor_lojas[col]} tem valor de R$ {matriz[lin][col]}',end='\n')            