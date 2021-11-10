"""
10. Faça um programa que calcule e mostre a área de um círculo. 
Sabe-se que: Área = p * raio 2 (o número 2 significa potência, ou seja, raio é elevado ao quadrado)

    LEIA raio
    area = 3.1415 * raio ** 2
    ESCREVA area
"""

# entrada
raio = float(input('Informe o número do raio: '))

# processamento
area = 3.1415 * (raio ** 2)

# saída
print(f'O resultado da área é {area:.2f}')
