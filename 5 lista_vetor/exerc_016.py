"""
16. Faça um programa que:
    * preencha dois vetores com de dez numeros cada
    * preencha um terceiro vetor com os números dos dois vetores anteriores ordenados em ordem crescente
    * Usar a função sort()
"""

vet_num1 = []
vet_num2 = []
vet_num3 = []

for i in range(10):
    vet_num1.append(int(input('Digite um número: ')))

for i in range(10):
    vet_num2.append(int(input('Digite um número... ')))

for i in range(10):
    vet_num3.append(vet_num1[i])
    vet_num3.append(vet_num2[i])
vet_num3.sort()
print(vet_num1)
print(vet_num2)
print(vet_num3)