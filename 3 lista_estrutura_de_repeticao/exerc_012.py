"""
12. Construir um algoritmo que, dado o valor de 20 preços de TV, determine e apresente o valor mais caro e mais barato entre eles. Pode implementar com o comando while ou for.
"""
contador = 0
while contador < 20:
    preco_tv = float(input('Informe o preço da TV: '))
    if contador == 0:
        preco_baixo = preco_tv
        preco_alto = preco_tv
    if preco_tv >= preco_alto:
        preco_alto = preco_tv
    if preco_tv <= preco_baixo:
        preco_baixo = preco_tv
    contador = contador + 1
print('Preço da TV com preço mais caro:',preco_alto)
print('Preço da TV com preço mais barato:',preco_baixo)