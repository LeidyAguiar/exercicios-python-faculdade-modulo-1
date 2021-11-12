"""
22 Um supermercado deseja reajustar os preços de seus produtos usando o seguinte critério: o produto poderá ter seu preço aumentado ou diminuído. 
Para o preço ser alterado, o produto deve preencher pelo menos um dos requisitos a seguir:

                                VENDA MÉDIA MENSAL      |   PREÇO ATUAL                |    % DE AUMENTO   |    % DE DIMINUIÇÃO
                                    < 500               |   < 30.00                    |        10         |        -
                                    >= 500 e <1200      |   >= 30.00 e < 80.00         |        15         |        -
                                    >= 1200             |   >= 80.00                   |        -          |        20                    

* Faça um programa que receba o preço atual e a venda média mensal do produto, calcule e mostre o novo preço.
"""
preco_atual = float(input('Digite o preço atual: '))
media_mensal_vendas = float(input('Qual a média mensal de vendas? '))
 
if media_mensal_vendas < 500 or preco_atual < 30:
    novo_preco = preco_atual + 10 / 100 * preco_atual
elif media_mensal_vendas >= 500 and media_mensal_vendas < 1200 or preco_atual >= 30 and preco_atual < 80:
    novo_preco = preco_atual + 15 / 100 * preco_atual
elif media_mensal_vendas >= 1200 or preco_atual >= 80:
    novo_preco = preco_atual - 20 / 100 * preco_atual
 
print('O novo preço será de:',novo_preco)