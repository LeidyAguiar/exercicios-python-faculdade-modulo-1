"""
4. Faça um programa que receba um conjunto de valores inteiros, calcule e exiba o maior e o menor valor do conjunto.
    * Para encerrar a entrada de dados, deve ser digitado o valor zero;
    * Para valores negativos, deve ser enviada uma mensagem;
    * Esses valores (zero e negativos) não entrarão nos cálculos.
"""
numero_inteiro = int(input('Digite um número inteiro: '))
num_maior = numero_inteiro
num_menor = numero_inteiro

while numero_inteiro != 0:
    if numero_inteiro < 0:
        print('Este número é negativo, tem que ser positivo')
    elif numero_inteiro > num_maior:
        num_maior = numero_inteiro
    elif numero_inteiro < num_menor:
        num_menor = numero_inteiro
    numero_inteiro = int(input('Digite um número inteiro... '))
  
print('O maior número é',num_maior, 'e o menor número é',num_menor)
