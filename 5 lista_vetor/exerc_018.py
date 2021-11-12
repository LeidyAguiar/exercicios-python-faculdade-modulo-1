"""
18. Faça um programa que:
    * leia um vetor de 10 números inteiros
    * exiba na tela os números positivos e seus respectivos índices.
    * não use nenhuma função pronta da linguagem Python
"""

vet_int = []
num_posit = 0

for i in range(5):
    vet_int.append(int(input('Digite um número inteiro: ')))
print(vet_int)  
  
for i in range(len(vet_int)): 
    if vet_int[i] > 0:
        num_posit += 1
        print('Número positivo:',num_posit,'está na posição',i, end='\n')