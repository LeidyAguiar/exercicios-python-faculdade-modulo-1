"""
20. Em uma fábrica trabalham homens e mulheres divididos em três classes:
    * trabalhadores que fazem até 30 peças por mês — classe 1;
    * trabalhadores que fazem de 31 a 50 peças por mês — classe 2;
    * trabalhadores que fazem mais de 50 peças por mês — classe 3.

**Os salários são compostos da sequinte maneira:**
    * A classe 1 recebe salário mínimo.
    * A classe 2 recebe salário mínimo mais 3% deste salário por peça, acima das 30 peças iniciais.
    * A classe 3 recebe salário mínimo mais 5% desse salário por peça, acima das 30 peças iniciais.

Pode implementar com o comando while ou for.

**Faça um programa que receba:**
    * o número do operário,
    * o número de peças fabricadas no mês,
    * o sexo do operário,

**Calcule e mostre:**
    * o número do operário e seu salário;
    * o total da folha de pagamento da fábrica;
    * o número total de peças fabricadas no mês;
    * a média de peças fabricadas pelos homens;
    * a média de peças fabricadas pelas mulheres; e
    * o número do operário ou operária de maior salário.

**A fábrica possui 15 operários.**
"""
total_de_operarios = 4
valor_do_salario_minimo = 954
 
total_da_folha_de_pagamento_no_mes = 0
total_de_pecas_fabricadas_no_mes = 0

total_de_pecas_do_operario = 0

media_das_pecas_fabricada_por_homens = 0
media_das_pecas_fabricada_por_mulheres = 0

total_de_homens = 0
total_de_mulheres = 0
 
meta_minima = 30
meta_classe3 = 50
 
porcentagem_de_bonus_da_classe1 = 0
porcentagem_de_bonus_da_classe2 = 2 / 100
porcentagem_de_bonus_da_classe3 = 3 / 100

total_de_operarios_homens = 0
total_de_operarios_mulheres = 0
 
somatorio_das_pecas_fabricadas_por_homens = 0
somatorio_das_pecas_fabricadas_por_mulheres = 0
 
maior_salario_entre_os_operarios = -1
 

for operario in range(1,total_de_operarios):
    numero_do_operario = int(input('Digite o número do operário: '))
    print(numero_do_operario)
    sexo_do_operario = str(input('Digite o sexo do operário (M ou H): '))
    print(sexo_do_operario)
    total_de_pecas_fabricadas_pelo_operario = int(input('Digite o total de peças fabricadas pelo operário: '))
    print(total_de_pecas_fabricadas_pelo_operario)
    if total_de_pecas_fabricadas_pelo_operario <= meta_minima:
        porcentagem_da_classe_do_operario = porcentagem_de_bonus_da_classe1
    elif total_de_pecas_do_operario >= meta_classe3:
        porcentagem_da_classe_do_operario = porcentagem_de_bonus_da_classe3
    else:
          porcentagem_da_classe_do_operario = porcentagem_de_bonus_da_classe2
 
    if total_de_pecas_fabricadas_pelo_operario > meta_minima:
        producao_acima_da_meta = total_de_pecas_fabricadas_pelo_operario - meta_minima
    else:
        producao_acima_da_meta = 0
    bonus_de_producao = valor_do_salario_minimo * porcentagem_da_classe_do_operario * producao_acima_da_meta
    salario_do_operario = valor_do_salario_minimo + bonus_de_producao
    print('O número do operário e seu salário é respectivamente:',numero_do_operario,',',salario_do_operario)
    total_da_folha_de_pagamento_no_mes += salario_do_operario 
    total_de_pecas_fabricadas_no_mes += total_de_pecas_fabricadas_pelo_operario
 
    if sexo_do_operario == 'H':
        total_de_homens += 1
        somatorio_das_pecas_fabricadas_por_homens += total_de_pecas_fabricadas_pelo_operario
    if sexo_do_operario == 'M':
        total_de_mulheres += 1
        somatorio_das_pecas_fabricadas_por_mulheres += total_de_pecas_fabricadas_pelo_operario
    if salario_do_operario > maior_salario_entre_os_operarios:
        numero_do_operario_com_o_maior_salario = numero_do_operario
        maior_salario_entre_os_operarios = salario_do_operario
media_das_pecas_fabricada_por_homens = somatorio_das_pecas_fabricadas_por_homens / total_de_homens
media_das_pecas_fabricada_por_mulheres = somatorio_das_pecas_fabricadas_por_mulheres / total_de_mulheres
print(f'O total da folha de pagamento no mês é de: {total_da_folha_de_pagamento_no_mes:.2f}')
print('O total de peças fabricadas:',total_de_pecas_fabricadas_no_mes)
print('Média de peças feitas por homens:',media_das_pecas_fabricada_por_homens)
print('Média de peças feitas por mulheres:',media_das_pecas_fabricada_por_mulheres)
print('Número de operário com maior salário:',numero_do_operario_com_o_maior_salario)