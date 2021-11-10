"""
14. Faça um programa que receba o ano de nascimento de uma pessoa e o ano atual, calcule e mostre:
- a idade dessa pessoa;
- quantos anos ela terá em 2050.

    LEIA ano_atual
    LEIA ano_nascimento
    idade_atual = ano_atual − ano_nascimento
    idade_2050 = 2050 − ano_nascimento
    ESCREVA idade_atual
"""

# entrada
ano_atual = int(input('Informe o ano atual: '))
ano_nascimento = int(input('Informe seu ano de nascimento: '))

# processamento
idade_atual = ano_atual - ano_nascimento
idade_2050 = 2050 - ano_nascimento

# saída
print(f'A sua idade é {idade_atual} anos')
print(f'Em 2050 sua idade {idade_2050} anos') 