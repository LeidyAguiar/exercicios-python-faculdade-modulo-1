"""
20. Faça um programa que:
    * adicione 10 numeros inteiros em um vetor de nome A
    * remova todos os numeros menores que 0 do vetor A e os adicione no vetor B
    * exiba os dois vetores A e B
"""

A = []
B = []
for i in range(5):
    A.append(int (input('Digite um numero no vetor A: ')))
    if A[i] < 0: 
        B.append(A[i])
print('\nOs valores do vetor A são:',A)
print('Os valores do vetor B são:',B)
print('.'*50)
i = 0

while i < len(A):
    if i >= len(A):
        break
    else:
        if A[i] < 0:        
            A.remove(A[i])
            i = i - 1 
    i = i + 1
    
print('\nOs valores do vetor A são:',A)
print('Os valores do vetor B são:',B)