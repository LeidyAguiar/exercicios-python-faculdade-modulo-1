"""
3. Utilize a linguagem de programação PYTHON. Crie um programa que leia o salário de 10 funcionários. 
Calcule e apresente a média de salários pagos acima de 2000 reais. Escolha a estrutura de repetição.
"""
contador = 0
soma = 0
divisor = 0
while contador < 10:
    salario = float(input('Digite o salário: '))
    if salario > 2000:
        soma += salario
        divisor += 1
    contador += 1

media = soma / divisor
print(f'A média será de: {media:.2f}')