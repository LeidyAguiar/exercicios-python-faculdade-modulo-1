"""
14. Faça um programa que informada a idade de 10 nadadores o mesmo terá condições de classificar em uma das seguintes categorias: 
infantil = 5 - 10 anos; juvenil = 11-17 anos; adulto >= maiores de 18 anos.
"""

contador = 0
while contador < 10:
    idade = int(input('Informe sua idade: '))
    if idade >= 5 and idade <= 10:
        print('Infantil')
    elif idade >= 11 and idade <= 17:
        print('Juvenil')
    elif idade >= 18:
        print('Adulto')
    else:
        print('Idade não classificada')
    contador = contador + 1