"""
10. Faça um programa que receba dois números e mostre o maior.
"""

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))

if n1 > n2:
    print(f'O número {n1} é maior que {n2}')
elif n2 > n1:
    print(f'O número {n2} é maior que {n1}')
else:
    print(f'O número {n1} e o número {n2} são iguais')