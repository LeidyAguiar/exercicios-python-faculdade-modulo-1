"""
16. Um funcionário de uma empresa recebe, anualmente, aumento salarial. Pode implementar com o comando while ou for.

**Sabe-se que:**
    * Esse funcionário foi contratado em 2005, com salário inicial de R$ 1.000,00.
    * Em 2006, ele recebeu aumento de 1,5% sobre seu salário inicial.
    * A partir de 2007, os aumentos salariais sempre corresponderam ao dobro do percentual do ano anterior.

**Faça um programa que determine o salário atual desse funcionário.**
"""
salario_inicial = 1000
ano_atual = 2007

percentual_aumento_ano = 1.5 / 100
aumento_ano = salario_inicial * percentual_aumento_ano
salario_ano = salario_inicial + aumento_ano

for salario in range(2007,ano_atual + 1):
    percentual_aumento_ano = percentual_aumento_ano * 2
    aumento_ano = salario_ano * percentual_aumento_ano
    salario_ano = salario_ano + aumento_ano

print(ano_atual,'=',salario_ano)