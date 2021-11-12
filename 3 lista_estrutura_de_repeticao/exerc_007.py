"""
7. Escreva um algoritmo que receba 23 números, calcule e exiba a quantidade de números pares e impares. Pode implementar com o comando while ou for.
"""
print('\nExemplo com o while')
contador = 0 # 1 º passo inicialização
cont_par = 0
cont_impar = 0
while contador < 23: # 2º passo condição
    numero = int(input('Informe o valor '))
    if numero % 2 == 0:
        cont_par = cont_par + 1
    else:
        cont_impar += 1 # significa cont_impar = cont_impar + 1
    contador = contador + 1 # 3º passo incremento
print('Quantidade de valores pares:',cont_par)
print('Quantidade de valores ímpares:',cont_impar)

