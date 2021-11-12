"""
19. Faça um programa que:
    * insira dez números inteiros em um vetor
    * crie um segundo vetor, substituindo os números multiplos de 3 por "999""
    * exiba os dois vetores
    * não use nenhuma função pronta da linguagem Python
"""

vet_inteiro = []
mult_3 = []

for i in range(10):
    vet_inteiro.append(int(input('Digite números inteiros: ')))
print('Vetor inicial:',vet_inteiro)

for i in range(len(vet_inteiro)):     
    if vet_inteiro[i] % 3 == 0:
        mult_3.append(999)
    else:
        mult_3.append(vet_inteiro[i])
print('Vetor substituído por 999:',mult_3)       