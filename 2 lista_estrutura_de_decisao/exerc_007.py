"""
7. A Organização Mundial de Saúde usa a seguinte tabela para determinar a condição de um adulto, para isso desenvolva 
um algoritmo para calcular o Índice de Massa Corporal (IMC) e apresenta-lo, dado pela fórmula:

IMC = peso / (altura * altura)

CONDIÇÃO        |   IMC em adultos 
Abaixo do peso  |	Abaixo de 18.5  
No peso normal	|	Entre 18.5 e 25
Acima do peso	|	Entre 25.1 e 30
Obeso		    |	Acima de 30
"""

peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))
IMC = peso / (altura * altura)
print(f'Seu IMC é = {IMC:.2f}')
if IMC < 18.5:
    print('Você está abaixo do peso')
elif IMC >= 18.5 and IMC <= 25:
    print('Seu peso está normal')
elif IMC >= 25.1 and IMC <= 30:
    print('Você está acima do peso')
else:
    print('Você está obeso')