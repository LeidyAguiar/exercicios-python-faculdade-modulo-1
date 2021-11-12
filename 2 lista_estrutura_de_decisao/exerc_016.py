"""
16. Faça um programa que determine a data cronologicamente maior entre duas datas fornecidas pelo usuário. 
Cada data deve ser composta por três valores inteiros, em que o primeiro representa o dia, o segundo, o mês e o terceiro, o ano.
"""
dia1 = int(input('Informe o dia da data 1: '))
mes1 = int(input('Informe o mês da data 1: '))
ano1 = int(input('Informe o ano da data 1: '))
dia2 = int(input('Informe o dia da data 2: '))
mes2 = int(input('Informe o mês da data 2: '))
ano2 = int(input('Informe o ano da data 2: '))

if ano1 > ano2:
    print('A maior data é:',dia1,'-',mes1,'-',ano1)
elif ano2 > ano1:
    print('A maior data é:',dia2,'-',mes2,'-',ano2)
elif mes1 > mes2:
    print('A maior data é:',dia1,'-',mes1,'-',ano1)
elif mes2 > mes1:
    print('A maior data é:',dia2,'-',mes2,'-',ano2)
elif dia1 > dia2:
    print('A maior data é:',dia1,'-',mes1,'-',ano1)
elif dia2 > dia1:
    print('A maior data é:',dia2,'-',mes2,'-',ano2)
else:
    print('As datas são iguais!')

