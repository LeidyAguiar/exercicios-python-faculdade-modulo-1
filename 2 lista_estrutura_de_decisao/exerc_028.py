"""
28. Faça um programa que receba o salário base e o tempo de serviço de um funcionário. Calcule e mostre:

* O imposto, conforme a tabela a seguir.
* A gratificação, de acordo com a tabela a seguir.
* O salário líquido, ou seja, salário base menos imposto mais gratificação.
* A categoria, que está na tabela a seguir.
"""
salario_base = float(input('Digite o salário base: '))
tempo_servico = float(input('Informe o tempo de serviço: '))

if salario_base < 200:
    imposto = 0
elif salario_base <= 450:
    imposto = 3 / 100 * salario_base
elif salario_base < 700:
    imposto = 8 / 100 * salario_base
else:
    imposto = 12 / 100 * salario_base
print(f'O imposto será de: {imposto:.2f}')

if salario_base > 500:
    if tempo_servico <= 3:
         gratificacao = 20
    else: 
        gratificacao = 30
else:
    if tempo_servico <= 3:
        gratificacao = 23
    elif tempo_servico < 6:
        gratificacao = 35
    else: 
        gratificacao = 33
        print('A gratificação será de:', gratificacao)
salario_liquido = salario_base - imposto + gratificacao
print('O salário líquido será de:',salario_liquido)

if salario_liquido <= 350:
    print('Classificação A')
elif salario_liquido < 600:
    print('Classificação B')
else:
    print('Classificação C')