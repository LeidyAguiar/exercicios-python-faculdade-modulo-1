"""
17. Foi feita uma pesquisa com as crianças de uma determinada localidade. Faça um programa que:
    * leia o número de crianças nascidas no período;
    * identifique o sexo (M ou F) e a idade da criança em meses.

**O programa deve calcular e mostrar:**
    * a percentagem de crianças do sexo marculino;
    * a percentagem de crianças do sexo feminino;
    * a percentagem de crianças menores que 24 meses.

**Observação:
porcentagem_de_meninos = total_de_meninos / total_de_criancas_nascidas * 100
porcentagem_de_meninas = total_de_meninas / total_de_criancas_nascidas * 100
porcentagem_de_criancas_menores_de_24_mese=criancas_menores_de_24_meses/total_de_criancas_nascidas*100
"""
numero_criancas = int(input('Informe a quantidade de crianças nascidas: '))
contador = 0
total_de_meninos = 0
total_de_meninas = 0
criancas_menores_24_meses = 0
while contador < numero_criancas:
    sexo = str(input('Digite o sexo da criança(M ou F): '))
    idade = int(input('Informe a idade da criança: '))
    if sexo == 'M':
            total_de_meninos = total_de_meninos + 1
    else:
            total_de_meninas = total_de_meninas + 1
    if idade < 24:
            criancas_menores_24_meses = criancas_menores_24_meses + 1
    contador = contador + 1

perc_meninos = total_de_meninos / numero_criancas * 100
perc_meninas = total_de_meninas / numero_criancas * 100
perc_menores_24_meses = criancas_menores_24_meses / numero_criancas * 100

print(f'A porcentagem de meninos é :{perc_meninos:.2f}')
print(f'A porcentagem de meninas é :{perc_meninas:.2f}')
print(f'A porcentagem de crianças menores que 24 meses é:{perc_menores_24_meses:.2f}')