"""
21. Faça um programa que:
    * leia dois vetores (A e B) com cinco posições para números inteiros.
    * o programa deve, então, subtrair o primeiro elemento de A do último de B, armazenando o resultado num terceiro vetor, subtrair o segundo elemento de A do penúltimo de B, 
     armazenando o resultado num terceiro vetor e assim por diante. 
    * ao final, mostre o resultado do terceiro vetor
    * não use nenhuma função pronta da linguagem Python
"""

# Incompleto
A = []
B = []

for i in range(5,0,-1):
    A.append(int(input('Digite um número inteiro: ')))