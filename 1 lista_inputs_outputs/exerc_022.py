"""
22. Sabe-se que o quilowatt de energia custa um quinto do salário mínimo. 
Faça um programa que receba o valor do salário mínimo e a quantidade de quilowatts consumida por uma residência. 
Calcule e mostre:

- O valor de cada quilowatt;
- O valor a ser pago por essa residência;
- O valor a ser pago com desconto de 15%.

    LEIA valor_salario
    LEIA qtde_quilowatt
    valor_quilowatt = valor_salario / 5
    valor_em_reais = valor_quilowatt * qtde_quilowatt
    valor_descontado = valor_em_reais * 15 / 100
    valor_com_desconto =  valor_em_reais − valor_descontado
    ESCREVA valor_quilowatt
    ESCREVA valor_em_reais
    ESCREVA valor_com_desconto
"""

# entrada
valor_salario = float(input('Informe o valor do salário mínimo: '))
qtde_quilowatt = float(input('Informe a quantidade de quilowatts consumida: '))

# processamento
valor_quilowatt = valor_salario / 5
valor_em_reais = valor_quilowatt * qtde_quilowatt
valor_descontado = valor_em_reais * 15 / 100
valor_com_desconto =  valor_em_reais - valor_descontado

# saída
print('Valor de cada quilowatt =', valor_quilowatt)
print('Valor a ser pago por essa residência =', valor_em_reais)
print('Valor a ser pago com desconto de 15% =', valor_com_desconto)