"""
15. Faça um programa que mostre a data e a hora do sistema nos seguintes formatos: dia/mês/ano – mês por extenso e hora:minuto.

* Observação: from carrega um módulo/biblioteca da linguagem Python e o import é usado para informar qual objeto desta biblioteca queremos importar/carregar no nosso programa.
"""
from datetime import datetime
hoje = datetime.now()

if hoje.month == 1:
    mes = 'Janeiro'
elif hoje.month == 2:
    mes = 'Fevereiro'
elif hoje.month == 3:
    mes = 'Março'
elif hoje.month == 4:
    mes = 'Abril'
elif hoje.month == 5:
    mes = 'Maio'
elif hoje.month == 6:
    mes = 'Junho'
elif hoje.month == 7:
    mes = 'Julho'
elif hoje.month == 8:
    mes = 'Agosto'
elif hoje.month == 9:
    mes = 'Setembro'
elif hoje.month == 10:
    mes = 'Outubro'
elif hoje.month == 11:
    mes = 'Novembro'
else:
    mes = 'Dezembro'
print(f'{hoje.day}/{hoje.month}/{hoje.year} - {mes} - {hoje.hour}:{hoje.minute}')
