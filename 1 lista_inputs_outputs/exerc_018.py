"""
18. Pedro comprou um saco de ração com peso em quilos. Ele possui dois gatos, para os quais fornece a quantidade de ração 
em gramas. A quantidade diária de ração fornecida para cada gato é sempre a mesma. 
Faça um programa que receba o peso do saco de ração em gramas e a quantidade de ração fornecida para cada gato, calcule 
e mostre quanto restará de ração no saco após cinco dias.

    LEIA peso_saco
    LEIA racao_gato1
    LEIA racao_gato2
    total_final = peso_saco − 5 * (racao_gato1 + racao_gato2)
    ESCREVA total_final
"""

# entrada
peso_saco = float(input('Digite o peso do saco de ração: '))
racao_gato1 = float(input('Informe a ração do primeiro gato: '))
racao_gato2 = float(input('Informe a ração do segundo gato: '))

# processamento
total_final = peso_saco - 5 * (racao_gato1 + racao_gato2)

# saída
print('Após 5 dias restará de ração =', total_final)