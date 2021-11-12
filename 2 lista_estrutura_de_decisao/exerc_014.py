"""
14. Faça um programa que mostre o menu de opções a seguir, receba a opção do usuário e os dados necessários para executar cada operação.

Menu de opções:
1. Somar dois números.
2. Raiz quadrada de um número.

* Observação: raiz = numero ** (1/2), ou import math raiz = math.sqrt(numero)
"""
print('Menu de opções: ')
print('1. Somar dois números. ')
print('2. Raiz quadrada de um número. ')
opcao = int(input('Qual opção deseja? '))
print()
if opcao == 1:
    n1 = float(input('Informe o primeiro número: '))
    n2 = float(input('Informe o segundo número: '))
    soma = n1 + n2
    print('\nO resultado da soma é:', soma)
elif opcao == 2:
    numero = int(input('Informe um número: '))
    raiz_quadrada = numero ** (1 / 2)
    print(f'\nA raiz quadrada do número é: {raiz_quadrada:.2f}')