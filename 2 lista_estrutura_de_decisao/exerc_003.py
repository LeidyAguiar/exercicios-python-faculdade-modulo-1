"""
3. Tendo como dados de entrada a altura e o sexo (M/F) de uma pessoa (M-masculino ou F-feminino), 
construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:

    homem: (72.7 * altura) - 58;
    mulher: (62.1 * altura) - 44.7
"""

altura = float(input('Informe sua altura: '))
sexo = str(input('Qual seu gênero sexual? '))
if sexo == 'M' or sexo == 'm':
    resultado = (72.7 * altura) - 58
    print(f'Esse é seu peso ideal: {resultado:.2f} kg')
elif sexo == 'F' or sexo == 'f':
    resultado = (62.1 * altura) - 44.7
    print(f'Esse é seu peso ideal: {resultado:.2f} kg')
else:
    print('Informe (M-masculino ou F-feminino)')

