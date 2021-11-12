"""
15. Faça um programa que:
    * preencha um vetor com quinze números

Determine e mostre:
    * o maior número e a posição por ele ocupada no vetor
    * o menor número e a posição por ele ocupada no vetor
    * Não use nenhuma função pronta da linguagem Python
"""

vet_num = []

for i in range(15):
    vet_num.append(int(input('Digite um número: ')))

for i in range(len(vet_num)):
    if i == 0:
        maior = vet_num[i]
        menor = vet_num[i]
        maior_i = 0
        menor_i = 0
    if vet_num[i] > maior:
        maior = vet_num[i]
        maior_i = i
    if vet_num[i] < menor:
        menor = vet_num[i]
        menor_i = i
        
print(vet_num)
print('Número maior:',maior,'está na posição',maior_i)
print('Número menor:',menor,'está na posição',menor_i)