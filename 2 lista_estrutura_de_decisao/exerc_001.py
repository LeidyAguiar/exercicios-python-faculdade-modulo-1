"""
1. a)Faça um algoritmo que calcule e exiba o salário reajustado de um funcionário de acordo com a seguinte regra: 
Salário até 500, reajuste de 50%.
"""

salario = float(input('Informe o salário: '))
if salario <= 500: # estrutura de decisão simples
    salario_reajustado = salario + (salario * 50 / 100)
    print('O novo salário é =', salario_reajustado)

"""
1.b)Faça um algoritmo que calcule e exiba o salário reajustado de um funcionário de acordo com a seguinte regra: 
Salário até 500, reajuste de 50%; Salários maiores que 500, reajuste de 30%.
"""
if salario <= 500: # estrutura de decisão composta
    salario_reajustado = salario + (salario * 50 / 100)
else: # > 500
    salario_reajustado = salario + (salario * 30 / 100)
print('Salário reajustado =', salario_reajustado)