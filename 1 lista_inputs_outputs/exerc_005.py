"""
5. Faça um programa que receba o salário de um funcionário e o percentual de aumento, calcule e mostre o valor do aumento 
e o novo salário.

    LEIA salario, percentual
    aumento = salario * percentual/100
    ESCREVA aumento
    novo_salario = salario + aumento
    ESCREVA novo_salario

"""

# entrada de valores
salario = float(input('Informe o salário do funcionário: '))
percentual = float(input('Informe o percentual de aumento: '))

# processamento
valor_aumento = salario * percentual / 100
novo_salario = salario + valor_aumento

# saída
print(f'O valor do aumento foi de {valor_aumento} reais')
print(f'O novo salário é {novo_salario} reais')