"""
7. Faça um programa que receba o salário base de um funcionário, calcule e mostre seu salário a receber, sabendo-se que 
o funcionário tem gratificação de 50,00 sobre o salário base e paga imposto que deve ser lido e é aplicado sobre o 
salário base.

    LEIA salario, perImposto
    imposto = salario * perImposto / 100
    salario_a_receber = salario + 50 - imposto
    ESCREVA salario_a_receber
"""

# entrada
salario = float(input('Informe o valor do salário: '))
perImposto = float(input('Informe o valor do Imposto: '))

# processamento
imposto = salario * perImposto / 100
salario_a_receber = salario + 50 - imposto

# saída
print('O salário a receber é =',salario_a_receber)