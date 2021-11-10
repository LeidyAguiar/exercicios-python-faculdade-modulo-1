"""
17. Um trabalhador recebeu seu salário e o depositou em sua conta bancária. Esse trabalhador emitiu dois cheques e agora 
deseja saber seu saldo atual. O banco criou uma taxa para a operação bancária de retirada que tem que pagar um imposto 
de 0.38% e o saldo inicial da conta está zerado.

    LEIA salario
    LEIA valor_cheque1
    LEIA valor_cheque2
    imposto_cheque1 = valor_cheque1 * 0.38 / 100
    saque1 = valor_cheque1 + imposto_cheque1
    imposto_cheque2 = cheque2 * 0.38 / 100
    saque2 = valor_cheque2 + imposto_cheque2
    saldo = salario - saque1 - saque2
    ESCREVA saldo
"""
# entrada
salario = float(input('Informe o salário: '))
valor_cheque1 = float(input('Informe o valor do cheque 1: '))
valor_cheque2 = float(input('Informe o valor do cheque 2: '))

# processamento
imposto_cheque1 = valor_cheque1 * 0.38 / 100
saque1 = valor_cheque1 + imposto_cheque1
imposto_cheque2 = valor_cheque2 * 0.38 / 100
saque2 = valor_cheque2 + imposto_cheque2
saldo = salario - saque1 - saque2

# saída
print('O saldo é =', saldo)