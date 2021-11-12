"""
23. Faça um programa para calcular a tabuada do 2 até a do 9. USE DUAS ESTRUTURAS DE REPETIÇÃO
"""
tabuada = 2
while tabuada <= 9:
    for contador in range(1,11):
        print(tabuada,' x ',contador,' = ', tabuada * contador)
    tabuada = tabuada + 1