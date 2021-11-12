"""
6. Um banco concederá um crédito especial aos seus clientes, variável com o saldo médio no último ano. 
Faça um algoritmo que leia o saldo médio de um cliente e calcule o valor do crédito de acordo com a tabela a seguir. 
Mostre uma mensagem informando o saldo médio e o valor do crédito.

    Saldo médio
    * de 0 a 200 nenhum crédito
    * de 201 a  400 20% do valor do saldo médio
    * de 401 a  600 30% do valor do saldo médio
    * acima de 601 40% do valor do saldo médio
"""

saldo_medio = float(input('Informe o seu saldo médio: '))
if saldo_medio >= 0 and saldo_medio <= 200:
     valor_credito = 0
elif saldo_medio >= 201 and saldo_medio <= 400:
    valor_credito = saldo_medio + ((saldo_medio / 100) * 20)
elif saldo_medio >= 401 and saldo_medio <= 600:
    valor_credito = saldo_medio + ((saldo_medio / 100) * 30)
elif saldo_medio >= 601:
    valor_credito = saldo_medio + ((saldo_medio / 100) * 40)
print('O valor do saldo médio é', saldo_medio, 'e o valor do crédito é', valor_credito)
