"""
24. Faça um programa que:
    * leia um valor N inteiro e positivo
    * Calcule e mostre o valor de E, conforme a fórmula:

E = 1 + 1/(1!) + 1/(2!) + 1/(3!) + 1/(4!) + ... 1/(N!)

USE **DUAS** ESTRUTURAS DE REPETIÇÃO.
NÃO DEVE SER USADA FUNÇÃO PRONTA DA LINGUAGEM PYTHON
"""
N = int(input('Digite um número inteiro e positivo: '))
contador = 1
acumuladora = 1 # toda vez que acumular começa com 0
while contador <= N:
    numero_atual = contador
    fatorial = 1
    
    while numero_atual > 1:
        fatorial = fatorial * numero_atual
        numero_atual = numero_atual - 1
    
    acumuladora = acumuladora + (1 / fatorial)
    contador = contador + 1
    
print('E =',acumuladora)
