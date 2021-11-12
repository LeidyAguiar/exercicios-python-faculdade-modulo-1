"""
12. Faça um programa que receba três números obrigatoriamente em ordem crescente e um quarto número que não siga essa 
regra. Mostre, em seguida, os quatro números em ordem decrescente. Suponha que o usuário digitará quatro números 
diferentes.
"""
n1 = float(input('Informe o número 1: '))
n2 = float(input('Informe o número 2: '))
n3 = float(input('Informe o número 3: '))
n4 = float(input('Informe o número 4: '))
if n1 <= n2 and n2 <= n3:
    if n4 >= n3:
        print(f'A ordem decrescente é: {n4} - {n3} - {n2} - {n1}')
    elif n4 >= n2 and n4 <= n3:
        print(f'A ordem decrescente é: {n3} - {n4} - {n2} - {n1}')
    elif n4 >= n1 and n4 <= n2:
        print(f'A ordem decrescente é: {n3} - {n2} - {n4} - {n1}')
    elif n4 <= n1:
        print(f'A ordem decrescente é: {n3} - {n2} - {n1} - {n4}')
else:
    print('\nDigite os três primeiros números em ordem crescente.')
