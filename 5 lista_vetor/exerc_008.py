"""
8. Criar um algoritmo que a partir de um vetor de 10 elementos inteiros, crie outros dois vetores que receberão os elementos positivos e negativos e ao final apresente-os. 
Não use nenhuma função pronta da linguagem Python.
"""

vet_inteiro = []
vet_positivo = []
vet_negativo = []
for i in range(5):
    vet_inteiro.append(int(input('Digite um número inteiro: ')))
for i in range(5):
    if vet_inteiro[i] > 0:
        vet_positivo.append(vet_inteiro[i])
    elif vet_inteiro[i] < 0:
        vet_negativo.append(vet_inteiro[i])
print('Números positivos: ',vet_positivo)
print('Números negativos: ',vet_negativo)
