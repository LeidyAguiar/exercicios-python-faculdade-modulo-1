"""
13. Sabe-se que:
- pé = 12 polegadas
- 1 jarda = 3 pés
- 1 milha = 1,760 jarda

Faça um programa que receba uma medida em pés, faça as conversões a seguir e mostre os resultados.
- Polegadas;
- Jardas;
- Milhas.

    LEIA pes
    polegadas = pes * 12
    jardas = pes / 3
    milhas = jardas / 1760
    ESCREVA polegadas, jardas, milhas
"""

# entrada
pes = float(input('Informe um número: '))

# processamento
polegadas = pes * 12
jardas = pes / 3
milhas = jardas / 1760

# saída
print(f'O resultado da medida em polegadas é {polegadas:.2f}')
print(f'O resultado da medida em Jardas {jardas:.2f}')
print(f'O resultado da medida em Milhas {milhas:.2f}')