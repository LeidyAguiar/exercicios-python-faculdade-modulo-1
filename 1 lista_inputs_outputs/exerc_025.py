"""
25. Faça um programa que receba o custo de um espetáculo teatral e o preço do convite desse espetáculo. Esse programa deverá 
calcular e mostrar a quantidade de convites que devem ser vendidos para que, pelo menos, o custo do espetáculo seja 
alcançado.

    LEIA custo
    LEIA convite
    quantidade = custo / convite
    ESCREVA quantidade
"""

# entrada
custo = float(input('Digite o valor do custo do espetáculo: '))
convite = float(input('Digite o valor do convite: '))

# processamento
quantidade = custo / convite

# saída
print('A quantidade a ser vendido para que o custo do espetáculo seja alcançado é =', quantidade)
