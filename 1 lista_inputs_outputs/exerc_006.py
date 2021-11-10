"""
6. Faça um programa que receba o salário base de um funcionário, calcule e mostre o salário a receber, sabendo-se que o 
funcionário tem gratificação de 5% sobre o salário base e paga imposto de 7% também sobre o salário base.

    LEIA salario
    gratificacao = salario * 5 / 100
    imposto = salario * 7 / 100
    salario_a_receber = salario + gratificacao − imposto
    ESCREVA salario_a_receber
"""

# entrada
salario = float(input('Informe o valor do salário: '))

# processamento
gratificacao = salario * 5 / 100
imposto = salario * 7 / 100
salario_a_receber = salario + gratificacao - imposto

# saída
print('O salário a receber é =', salario_a_receber)