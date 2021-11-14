"""
22. Faça um programa que:
    * preencha um vetor de cinco números e mostre a saída a seguir:
    * imprima a seguinte saída: n1 + n2 + n3 + n4 + n5 = soma_dos_numeros, exemplo 8 + 2 + 1 + 3 + 0 = 14
    * não use nenhuma função pronta da linguagem Python
"""
vet = [8, 2, 1, 3, 0]
indice = 0
soma = 0
while indice < 5:
    soma = soma + vet[indice]
    indice = indice + 1
print('A soma desses números é:',soma)

