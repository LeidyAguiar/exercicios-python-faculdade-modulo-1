"""
17. Faça um programa que receba a hora do início de um jogo e a hora do término (cada hora é composta por duas variáveis inteiras: hora e minuto). 
Calcule e mostre a duração do jogo (horas e minutos), sabendo que o tempo máximo de duração do jogo é de 24 horas e que ele pode começar em um dia e terminar no dia seguinte.
"""

hora_inicial = int(input('Informe a hora inicial do jogo: '))
minuto_inicial = int(input('Informe os minutos iniciais do jogo: '))
hora_final = int(input('Informe a hora final do jogo: '))
minuto_final = int(input('Informe os minutos finais do jogo: '))

if minuto_inicial > minuto_final:
    minuto_final = minuto_final + 60
    hora_final = hora_final - 1
if hora_inicial > hora_final:
    hora_final = hora_final + 24

minuto_duracao = minuto_final - minuto_inicial
hora_duracao = hora_final - hora_inicial

print('A duração do jogo foi de:', hora_duracao,'h', minuto_duracao,'minutos',)