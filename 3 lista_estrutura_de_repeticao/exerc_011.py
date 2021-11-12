"""
11. Construir um algoritmo para calcular a média aritmética de preços de 5 produtos. Pode implementar com o comando while ou for.
"""
print('Exemplo com for')
preco = 0
media = 0
for contador in range(5):
    preco = float(input('Informe um preço: '))
    media = media + preco
media = media / 5
print('A média dos preços é de:',media)