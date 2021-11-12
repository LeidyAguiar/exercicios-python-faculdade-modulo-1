"""
11. Faça um programa que receba três números e mostre-os em ordem crescente. 
Suponha que o usuário digitará três números diferentes.
"""

n1 = float(input('Informe o número 1: '))
n2 = float(input('Informe o número 2: '))
n3 = float(input('Informe o número 3: '))
if n1 <= n2 and n1 <= n3:
    if n2 <= n3:
        print(f'A ordem crescente é: {n1} - {n2} - {n3}')
    else:
        print(f'A ordem crescente é: {n1} - {n3} - {n2}')
elif n2 <= n1 and n2 <= n3:
    if n1 <= n3:
        print(f'A ordem crescente é: {n2} - {n1} - {n3}')
    else:
        print(f'A ordem crescente é: {n2} - {n3} - {n1}')
elif n3 <= n1 and n3 <= n2:
    if n1 <= n2:
        print(f'A ordem crescente é: {n3} - {n1} - {n2}')
    else:
        print(f'A ordem crescente é: {n3} - {n2} - {n1}')

