"""
9. Faça um algoritmo que conheça 4 valores diferentes, some-os e mostre o resultado. Pode implementar com o comando while ou for.
"""
print('Exemplo com o for')
i = 0
qnt = 0
soma = 0
for i in range(4):
    qnt = int(input('Digite os valores: '))
    soma = soma + qnt
print('A soma é de:',soma)