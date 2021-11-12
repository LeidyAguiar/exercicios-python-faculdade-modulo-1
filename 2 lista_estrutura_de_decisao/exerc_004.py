"""
4. Faça um algoritmo que leia um número inteiro e mostre uma mensagem indicando se este número é par ou ímpar 
e se é positivo ou negativo.
"""

numero = int(input('Informe um número: '))
if numero % 2 == 0:
    print(f'O número {numero} é Par')
else:
    print(f'O número {numero} é Ímpar')
if numero > 0:
    print(f'O número {numero} é positivo')
elif numero < 0:
    print(f'O número {numero} é negativo')
else:
    print(f'O número {numero} é neutro')