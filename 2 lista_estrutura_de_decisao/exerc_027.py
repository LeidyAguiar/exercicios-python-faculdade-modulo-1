"""
27. Faça um programa que receba:
* o código do estado de origem da carga de um caminhão, supondo que a digitação do código do estado seja sempre válida, isto é, um número inteiro entre 1 e 5;
* o peso da carga do caminhão em toneladas;
* o código da carga, supondo que a digitação do código seja sempre válida, isto é, um número inteiro entre 10 e 40.

                                                CÓDIGO DO ESTADO    | IMPOSTO
                                                    1               |   35%
                                                    2               |   25%
                                                    3               |   15%
                                                    4               |   5%
                                                    5               |   Isento
                                                
                                                CÓDIGO DA CARGA     |  PREÇO POR QUILO
                                                    10 a 20         |    100
                                                    21 a 30         |    250
                                                    31 a 40         |    400

Calcule e mostre:
* o peso da carga do caminhão convertido em quilos;
* o preço da carga do caminhão;
* o valor do imposto, sabendo que o imposto é cobrado sobre o preço da carga do caminhão e depende do estado de origem;
* o valor total transportado pelo caminhão, preço da carga mais imposto.
"""
codigo_estado = float(input('Informe o código do Estado: '))
peso_em_toneladas = float(input('Informe o peso em toneladas: '))
codigo_carga = float(input('Informe o código da carga: '))
peso_em_quilos = peso_em_toneladas * 1000
print('O peso em quilos é de:',peso_em_quilos)

if codigo_carga >= 10 and codigo_carga <= 20:
    preco_da_carga = 100 * peso_em_quilos
elif codigo_carga >= 21 and codigo_carga <= 30:
    preco_da_carga = 250 * peso_em_quilos
elif codigo_carga >= 31 and codigo_carga <= 40:
    preco_da_carga = 340 * peso_em_quilos   
print('O preço da carga é de:',preco_da_carga)
if codigo_estado == 1:
    imposto = 35 / 100 * preco_da_carga
elif codigo_estado == 2:
    imposto = 25 / 100 * preco_da_carga
elif codigo_estado == 3:
    imposto = 15 / 100 * preco_da_carga
elif codigo_estado == 4:
    imposto = 5 / 100 * preco_da_carga
elif codigo_estado == 5:
    imposto = 0
print('O imposto será de:',imposto)
valor_total = preco_da_carga + imposto
print('O valor total será de:',valor_total)