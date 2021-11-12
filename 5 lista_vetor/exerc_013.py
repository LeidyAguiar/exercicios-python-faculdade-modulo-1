"""
13. Faça um programa que:
    * preencha um vetor com dez números reais

Calcule e mostre:
    * a quantidade de números negativos
    * a soma dos números positivos desse *vetor*
    * não use nenhuma função pronta da linguagem Python
"""

vet_num_real = []
num_neg = []
soma_num_posit = 0
qntd_num_neg = 0
for i in range(10):
    vet_num_real.append(int(input('Digite número reais: ')))
for i in range(len(vet_num_real)):
    if vet_num_real[i] < 0:
        num_neg.append(vet_num_real[i])
        qntd_num_neg += 1
    if vet_num_real[i] > 0:
        soma_num_posit = soma_num_posit + vet_num_real[i]
        
print('Números negativos:',num_neg,'e a quantidade de números negativos é:',qntd_num_neg)
print('Soma dos números positivos:',soma_num_posit)