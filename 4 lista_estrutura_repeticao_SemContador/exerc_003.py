"""
3. Faça um programa que receba a idade e a altura de várias pessoas. Calcule e exiba a média das alturas das pessoas com mais de 20 anos. 
Para encerrar a entrada de dados, digite uma idade negativa ou igual a zero.
"""
idade = 1
soma_alturas = 0
contador = 0
while idade > 0:
    if idade > 20:
        altura = float(input('Informe a altura: '))
        soma_alturas = soma_alturas + altura 
        contador = contador + 1
    idade = int(input('Informe a idade: '))

media = soma_alturas / contador
print('A média de altura das pessoas com mais de 20 anos é:', media)