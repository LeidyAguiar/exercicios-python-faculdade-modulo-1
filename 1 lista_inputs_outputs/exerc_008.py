"""
8. Faça um programa que receba o valor de um depósito e o valor da taxa de juros, calcule e mostre o valor do rendimento 
e o valor total depois do rendimento de um mês.

    LEIA deposito, taxa
    rendimento = deposito * taxa / 100
    total = deposito + rendimento
    ESCREVA rendimento
    ESCREVA total
"""

# entrada
deposito = float(input('Informe o valor do depósito: '))
taxa = float(input('Informe o valor da taxa: '))

# processamento
rendimento = deposito * taxa / 100
total = deposito + rendimento

# saída
print('O resultado do rendimento é =', rendimento)
print('O resultado total é =', total)