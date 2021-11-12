"""
10. Faça um programa que:
    * preencha um vetor com seis elementos numéricos inteiros. 

Calcule e mostre:
    * todos os números pares;
    * a quantidade de números pares;
    * todos os números ímpares;
    * a quantidade de números ímpares
"""

vet_inteiro = []
qntd_par = 0
qntd_impar = 0

for i in range(6):
    vet_inteiro.append(int(input('Digite um número inteiro: ')))
    
for i in range(6):
    if vet_inteiro[i] % 2 == 0:
        print('Par:',vet_inteiro[i])
        qntd_par += 1       
    else:
        print('Impar:',vet_inteiro[i])
        qntd_impar += 1
print('Quantidade de números pares:',qntd_par)
print('Quantidade de números impares:',qntd_impar)
        