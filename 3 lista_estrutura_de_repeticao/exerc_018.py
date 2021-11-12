"""
18. Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Pode implementar com o comando while ou for. Foram obtidos/lidos os seguintes dados:
    * nome da cidade;
    * número de veículos de passeio;
    * número de acidentes de trânsito com vítimas.

**Deseja-se saber:**
    * o maior índice de acidentes de trânsito e a qual cidade pertence;
    * o menor índice de acidentes de trânsito e a qual cidade pertence;
    * qual é a média de veículos nas cinco cidades juntas;
    * qual é a média de acidentes de trânsito nas cidades com mais de 2.000 veículos de passeio.
"""

total_cidades_pesquisadas = 2
somatoria_veiculos_cidades = 0
soma_acidentes_acima_2000_veiculos = 0
numero_cidades_mais_2000_veiculos = 0
numero_acidentes = 0

for cidade in range(0,total_cidades_pesquisadas):
    nome_cidade = str(input('Informe o nome da cidade: '))
    numero_veiculos = int(input('Informe o número de veículos: ')) 
    numero_acidentes = int(input('Informe o número de acidentes: '))
    if cidade == 0:
        maior_casos_acidentes = numero_acidentes
        cidade_maior_casos_acidentes = nome_cidade
        menor_casos_acidentes = numero_acidentes
        cidade_menor_casos_acidentes = nome_cidade
    else:
        if numero_acidentes > maior_casos_acidentes:
             maior_casos_acidentes = numero_acidentes
             cidade_maior_casos_acidentes = nome_cidade
        if numero_acidentes < menor_casos_acidentes:
            menor_casos_acidentes = numero_acidentes
            cidade_menor_casos_acidentes = nome_cidade
    somatoria_veiculos_cidades += numero_veiculos
    if numero_veiculos > 2000:
        soma_acidentes_acima_2000_veiculos += numero_acidentes
        numero_cidades_mais_2000_veiculos += 1
media_carros_cidades = somatoria_veiculos_cidades / total_cidades_pesquisadas
if numero_cidades_mais_2000_veiculos == 0:
    print('Não foi informada nenhuma cidade com mais de 2000 veículos')
else:
    media_acidentes_cidade_mais_2000_veiculos = soma_acidentes_acima_2000_veiculos / numero_cidades_mais_2000_veiculos
    print(cidade_maior_casos_acidentes, maior_casos_acidentes)
    print(cidade_menor_casos_acidentes, menor_casos_acidentes) 
    print(media_carros_cidades)
    print(media_acidentes_cidade_mais_2000_veiculos)