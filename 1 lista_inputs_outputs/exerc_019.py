"""
19. Cada degrau de uma escada tem X de altura. Faça um programa que receba essa altura e a altura que o usuário deseja 
alcançar subindo a escada, calcule e mostre quantos degraus ele deverá subir para atingir seu objetivo, sem se preocupar 
com a altura do usuário. Todas as medidas fornecidas devem estar em metros.

    LEIA altura_degrau
    LEIA altura_desejada
    quantidade_de_degraus = altura_desejada // altura_degrau
    ESCREVA quantidade_de_degraus

  Observação: o operador // em Python é utilizado para pegar a parte inteira de uma divisão
"""

# entrada
altura_degrau = float(input('Informe a altura do degrau: '))
altura_desejada = float(input('Informe a altura desejada: '))

# processamento
quantidade_de_degraus = altura_desejada // altura_degrau

# saída
print('A quantidade de degraus será =', quantidade_de_degraus)