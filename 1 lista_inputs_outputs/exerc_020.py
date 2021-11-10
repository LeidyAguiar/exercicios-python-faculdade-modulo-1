"""
20. Faça um programa que receba a medida do ângulo (em graus) formado por uma escada apoiada no chão e encostada na parede 
e a altura da parede onde está a ponta da escada. Calcule e mostre a medida dessa escada. 

* Observação: as funções trigonométricas implementadas nas linguagens de programação trabalham com medidas de ângulos em 
radianos.

    LEIA angulo
    LEIA altura
    import math # carrega a biblioteca matemática
    radiano = angulo * math.pi / 180
    escada = altura / math.sin(radiano)
    ESCREVA escada

* Observação: Para usar seno em Python, deve-se usar esta linha de código import math e esta, no cálculo, math.sin(numero)
import math
escada = altura / math.sin(numero)
"""

# entrada
import math
angulo = float(input('Digite a medida do ângulo em graus: '))
altura = float(input('Digite a altura da parede: '))

# processamento
radiano = angulo * math.pi / 180
escada = altura / math.sin(radiano)

# saída
print('A medida da escada é =', escada)