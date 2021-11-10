"""
11. Faça um programa que receba um número, calcule e mostre:
- O número digitado ao quadrado
- O número digitado ao cubo
- A raiz do número digitado
- A raiz cúbica do número digitado

    LEIA numero
    quadrado = numero ** 2
    cubo = numero ** 3
    raiz_quadrada = numero ** ½ (meio, ou 0.5)
    raiz_cubica = numero ** ⅓ (um terço, ou 0.33)
    ESCREVA quadrado, cubo, raiz_quadrada, raiz_cubica
"""

# entrada
numero = int(input('Informe um número: '))

# processamento
quadrado = numero ** 2
cubo = numero ** 3
raiz_quadrada = numero ** (1 / 2 )
raiz_cubica = numero ** (1 / 3)

# saída
print(f'O valor do Quadrado é {quadrado}')
print(f'O valor do Cubo é {cubo}')
print(f'A Raiz Quadrada é {raiz_quadrada:.2f}')
print(f'A Raiz Cúbica é {raiz_cubica:.2f}')