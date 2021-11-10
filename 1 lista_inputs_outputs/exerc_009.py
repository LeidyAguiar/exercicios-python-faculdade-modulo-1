"""
9. Faça um programa que calcule e mostre a área de um triângulo. Sabe-se que: Área = (base * altura) / 2.

    LEIA base, altura
    area = (base * altura) / 2
    ESCREVA area
"""

# entrada
base = float(input('Informe a base o triângulo: '))
altura = float(input('Informe a altura do triângulo: '))

# processamento
area = (base * altura) / 2

# saída
print('O resultado da área do triângulo é =', area)