"""
5. Faça um programa que carregue um vetor de oito elementos numéricos inteiros, calcule e mostre os números pares e suas respectivas índices/posições. 
Não use nenhuma função pronta da linguagem Python.
"""

vet_inteiro = []

for i in range(8):
    vet_inteiro.append(int(input('Digite um número inteiro: ')))

for i in range(8):
    rest = vet_inteiro[i] % 2
    if rest == 0:
        print('O número par' ,vet_inteiro[i], 'está na posição',i)

