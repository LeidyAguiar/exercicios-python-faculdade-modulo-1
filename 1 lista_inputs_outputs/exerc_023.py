"""
23. Faça um programa que receba um número real, encontre e mostre:

* a parte inteira desse número;
* a parte fracionária desse número;
* o arredondamento desse número.

    LEIA numero
    parte_inteira = numero // 1
    parte_fracionaria = numero - parte_inteira
    numero_arredondado = arredonda (numero)
    ESCREVA parte_inteira
    ESCREVA parte_fracionaria
    ESCREVA numero_arredondado

* Observação: Para arredondar um número em Python, usa-se a função round(numero), onde se o número real/float estiver 
em igual distância entre o inteiro de cima e o inteiro de baixo, esta função arredonda para o número par mais próximo.
"""

# entrada
numero = float(input('Digite um número: '))

# processamento
parte_inteira = numero // 1
parte_fracionaria = numero - parte_inteira
numero_arredondado = round(numero)

# saída
print(f'A parte inteira do número {numero} = {parte_inteira}')
print(f'A parte fracionária do número {numero} = {parte_fracionaria}')
print(f'O arredondado do número {numero} = {numero_arredondado}')