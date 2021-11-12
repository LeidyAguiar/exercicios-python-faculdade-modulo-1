"""
9. Criar um algoritmo que leia dados para um vetor de 100 elementos inteiros, imprimir o maior, o menor, o percentual de números pares e a média dos elementos do vetor. 
Obs.: percentual = quantidade contada * 100 / quantidade total. Não use nenhuma função pronta da linguagem Python.
"""

vet_num_inteiro = []
maior = 0
menor = 0
percent_par = 0
media_vetor = 0
contador = 0
for i in range(5):
    vet_num_inteiro.append(int(input('Digite um número inteiro: ')))
    soma_media = soma_media + vet_num_inteiro[i]

for i in range(5):
    if vet_num_inteiro[i] > maior:
        maior = vet_num_inteiro[i]
    elif vet_num_inteiro[i] <  menor:
        menor = vet_num_inteiro[i]
    elif vet_num_inteiro[i] % 2 == 0:
        contador += 1
        percent_par = vet_num_inteiro * (100 / len(vet_num_inteiro))
        print('Percentual de números pares: ',percent_par)
media = soma_media / len(vet_num_inteiro)

print('Maior: ',maior)
print('Menor: ',menor)
print(f'Média: {media:.2f}')
