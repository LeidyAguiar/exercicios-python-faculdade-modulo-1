"""
8. Faça um algoritmo que calcule e exiba o salário reajustado de dez funcionários de acordo com a seguinte regra (pode implementar com o comando while ou for):
    - Salário até 300, reajuste de 50%;
    - Salários maiores que 300, reajuste de 30%.
"""
print('Exemplo com o while')
qtde_funcionarios = 1 # inicialização
while qtde_funcionarios <= 3: # condição #quando começar de 1, colocar o sinal de =
    salario = float(input('Informe o salário '))
    if salario <= 300:
        novo = salario + (salario * 50 / 100)
    else:
        novo = salario + (salario * 30 / 100)
    print('O novo salário é',novo)
    qtde_funcionarios = qtde_funcionarios + 1 # incremento

