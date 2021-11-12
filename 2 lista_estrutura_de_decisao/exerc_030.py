"""
30. Faça um programa que receba de um produto:
* o preço
* o tipo (A — alimentação; L — limpeza; e V — vestuário)
* a refrigeração (S — produto que necessita de refrigeração; e N — produto que não necessita de refrigeração) .

**Suponha que haverá apenas a digitação de dados válidos e, quando houver digitação de letras, utilize maiúsculas. Calcule e mostre:**

* O valor adicional, de acordo com a tabela a seguir:

                                    REFRIGERAÇÃO      |   TIPO        |    PREÇO         |  VALOR ADICIONAL
                                      N               |    A          |   <  15,00       |      2,00
                                                      |               |   >= 15,00       |      5,00
                                  -----------------------------------------------------------------------------
                                                      |    L          |   < 10,00        |      1,50
                                                      |               |   >= 10,00       |      2,50
                                  -----------------------------------------------------------------------------
                                                      |    V          |   < 30,00        |      3,00
                                                      |               |  >= 30,00        |      2,50
                                  -----------------------------------------------------------------------------
                                      S               |    A          |                  |      8,00
                                                      |    L          |                  |      0,00
                                                      |    V          |                  |      0,00

* O valor do imposto, de acordo com a regra a seguir.

                                                         PREÇO        |   PERCENTUAL SOBRE O PREÇO
                                                        < 25,00       |       5%
                                                       >= 25,00       |       8%

O preço de custo, ou seja, preço mais imposto.
O desconto, de acordo com a regra a seguir.

O produto que não preencher nenhum dos requisitos a seguir terá desconto de 3%, caso contrário, 0 (zero). Os requisitos são:
* Tipo: A
* Refrigeração: S

* O novo preço, ou seja, preço de custo mais adicional menos desconto.
* A classificação, de acordo com a regra a seguir.

                                                                NOVO PREÇO              |  CLASSIFICAÇÃO
                                                                <= 50,00                |   Barato
                                                                Entre 50,00 e 100,00    |   Normal
                                                                >= 100,00               |   Caro
"""
preco = float(input('Informe o preço: '))
tipo = str(input('Informe o tipo, se é A, L ou V: '))
refrig = str(input('Informe a refrigeração, se é N ou S: '))

if refrig == 'N':
    if tipo == 'A':
        if preco < 15:
           valor_adic = 2
        else: 
           valor_adic = 5
    elif tipo == 'L':
        if preco < 10:
           valor_adic = 1.5
        else: 
           valor_adic = 2.5
    elif tipo == 'V':
        if preco < 30:
           valor_adic = 3
        else: 
           valor_adic = 2.5
elif tipo == 'A':
    valor_adic = 8
elif tipo == 'L':
    valor_adic = 0
elif tipo == 'V':
    valor_adic = 0
print('O valor adicional será:',valor_adic)
if preco < 25:
    imposto = 5 / 100 * preco
else: 
    imposto = 8 / 100 * preco
print(f'O imposto será de: {imposto:.2f}')
preco_custo = preco + imposto
print(f'O preço de custo será de: {preco_custo:.2f}')
if tipo != 'A' and refrig != 'S':
  desconto = 3 / 100 * preco_custo
else: 
  desconto = 0
print('O desconto é:',desconto)
novo_preco = preco_custo + valor_adic - desconto
print(f'O novo preço é: {novo_preco:.2f}')
if novo_preco <= 50:
    print('Barato')
elif novo_preco < 100:
    print('Normal')
else: 
    print('Caro')