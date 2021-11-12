"""
1. Construir um algoritmo para calcular e apresentar o total de salários pagos de funcionários, mas não é informado a quantidade de pessoas, 
então use como critério de parada (condição da estrutura de repetição, digitar zero no salário para sair.
"""
salario = float(input('Informe o salário: '))
total = 0
while salario > 0:
    total = total + salario
    salario = float(input('Informe o salário:... ')) #DEVE SEMPRE SER A ÚLTIMA LINHA DE CÓDIGO O INPUT
    
print(f'O total de salários pagos é: {total:.2f}'' reais')
