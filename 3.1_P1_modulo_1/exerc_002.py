"""
2. Utilize a linguagem de programação PYTHON. Crie um programa que leia o salário de um funcionário. Calcule e apresente os seguintes itens:
    a) Valor descontado do INSS (Instituto Nacional do Seguro Social)
    b) Valor do salário líquido

                                SALÁRIO R$              |  Alíquota INSS % 
                                até 1100.00             |	    7.50  
                                de 1100.01 até 2203.48	|       9.00 
                                de 2203.49 até 3305.22	|       12.00 
                                de 3305.23 até 6433.57  |       14.00
                                Acima 6433.57           |       R$ 751.97

Observação: o valor R$ 751.97 é fixo para qualquer valor de salário acima de R\$ 6433.57, conhecido como teto do INSS.
"""
salario = float(input('Informe seu salário: '))
if salario <= 1100:
    desconto_inss = salario * 7.50 / 100
elif salario >= 1100.01 and salario <= 2203.48:
    desconto_inss = salario * 9 / 100
elif salario >= 2203.49 and salario <= 3305.22:
    desconto_inss = salario * 12 / 100
elif salario >= 3305.23 and salario <= 6433.57:
    desconto_inss = salario * 14 / 100
else:
    desconto_inss = 751.97
salario_liquido = salario - desconto_inss
print(f'O valor descontado do INSS é de: R$ {desconto_inss:.2f}')
print(f'O valor do salário líquido vai ser: R$ {salario_liquido:.2f}')