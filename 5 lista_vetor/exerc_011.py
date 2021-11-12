"""
11. Faça um programa que:
    * preencha um vetor com sete números inteiros

Calcule e mostre:
    * os números múltiplos de 2;
    * os números múltiplos de 3;
    * os números múltiplos de 2 e de 3.
"""

vet_inteiro = []
mult_2 = []
mult_3 = []
mult_2_3 = []

for i in range(7):
    vet_inteiro.append(int(input('Digite números inteiros: ')))

for i in range(len(vet_inteiro)):
    if vet_inteiro[i] % 2 == 0:
        mult_2.append(vet_inteiro[i])
    if vet_inteiro[i] % 3 == 0:
        mult_3.append(vet_inteiro[i])
    if vet_inteiro[i] % 2 == 0 and vet_inteiro[i] % 3 == 0:
        mult_2_3.append(vet_inteiro[i])
print('Números múltiplos de 2:',mult_2,'números múltiplos de 3:',mult_3,'e números múltiplos de 2 e 3:',mult_2_3)

        