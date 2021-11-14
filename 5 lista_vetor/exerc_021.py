"""
21. Faça um programa que:
    * leia dois vetores (A e B) com cinco posições para números inteiros.
    * o programa deve, então, subtrair o primeiro elemento de A do último de B, armazenando o resultado num terceiro vetor, subtrair o segundo elemento de A do penúltimo de B, 
     armazenando o resultado num terceiro vetor e assim por diante. 
    * ao final, mostre o resultado do terceiro vetor
    * não use nenhuma função pronta da linguagem Python
"""

vet_A = []
vet_B = []

for i in range(5):
    vet_A.append(int(input('Digite um número: ')))
for i in range(5):
    vet_B.append(int(input('Digite um número.... ')))

ultima_posi = len(vet_A) - 1
vet_subt = []
for i in range(len(vet_A)):
    vet_subt.append(vet_A[i] - vet_B[ultima_posi - i])
print(vet_A)
print(vet_B)
print(vet_subt)
    
