"""
21. Uma pessoa deseja pregar um quadro em uma parede. Faça um programa para calcular e mostrar a que distância a escada deve 
estar da parede. A pessoa deve fornecer o tamanho da escada e a altura em que deseja pregar o quadro. Lembre-se de que o 
tamanho da escada deve ser maior que a altura que se deseja alcançar.

    LEIA Z
    LEIA X
    Y = Z ** 2 - X ** 2
    Y = Y **1/2
    ESCREVA Y
"""

# entrada
tamanho_da_escada = float(input('Digite qual o tamanho da escada(tem que ser maior que a altura desejada): '))
altura_desejada = float(input('Digite a altura desejada: '))

# processamento
distancia = tamanho_da_escada ** 2 - altura_desejada ** 2
distancia = distancia ** (1/2)

# saída
print(f'A distância que a escada deverá ficar da parede em metros será de {distancia:.2f}')