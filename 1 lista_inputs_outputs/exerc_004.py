"""
4. Faça um programa que:
- receba o salário de um funcionário
- calcule e mostre o novo salário, sabendo-se que este sofreu um aumento de 25%.

LEIA salario
novoSalario = salario + (salario * 25 / 100)
ESCREVA novoSalario
"""

salario = float(input('Informe o valor do salário: '))
novoSalario = salario + (salario * 25 / 100)
print('O resultado do novo salário é =', novoSalario)