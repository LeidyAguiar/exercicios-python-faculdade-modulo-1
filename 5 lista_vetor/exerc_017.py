"""
17. Faça um programa que:
    * carregue dois vetores com 10 números cada
    * faça a multiplicação dos números na mesma posição
    * o resultado deverá ser adicionada em um terceiro vetor
    * não use nenhuma função pronta da linguagem Python
"""

vet_num1 = []
vet_num2 = []
vet_num3 = []

for i in range(5):
    vet_num1.append(int(input('Digite um número: ')))

for i in range(5):
    vet_num2.append(int(input('Digite um número... ')))

for i in range(5):
    vet_num3.append(vet_num1[i] * vet_num2[i])
    

print(vet_num1)
print(vet_num2)
print(vet_num3)