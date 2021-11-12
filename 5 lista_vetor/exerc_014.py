"""
14. Faça um programa que:
    * receba dez números inteiros e armazene-os em um vetor
    * classifique os números em dois vetores, um com números pares e o outra com os ímpares
    * não use nenhuma função pronta da linguagem Python
"""

vet_num_int = []
vet_par = []
vet_impar = []

for i in range(10):
    vet_num_int.append(int(input('Digite um número inteiro: ')))
    
for i in range(len(vet_num_int)):
    if vet_num_int[i] % 2 == 0:
        vet_par.append(vet_num_int[i])
    else:
        vet_impar.append(vet_num_int[i])
print('Números pares:',vet_par)
print('Números ímpares:',vet_impar)
