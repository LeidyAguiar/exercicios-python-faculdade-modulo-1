"""
12. Faça um programa que receba dois números maiores que zero, calcule e mostre um elevado ao outro.

    LEIA numero1, numero2
    numero1_elevado_numero2 = numero1 ** numero2
    numero2_elevado_numero1 = numero2 ** numero1
    ESCREVA numero1_elevado_numero2, numero2_elevado_numero1
"""

# entrada
numero1 = float(input('Informe o primeiro número: '))
numero2 = float(input('Informe o segundo número: '))

# processamento
numero1_elevado_numero2 = numero1 ** numero2
numero2_elevado_numero1 = numero2 ** numero1

# saída
print('O resultado do primeiro número é =', numero1_elevado_numero2)
print('O resultado do segundo número é =', numero2_elevado_numero1)