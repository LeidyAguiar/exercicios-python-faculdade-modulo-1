"""
15. Faça um programa que receba duas notas de seis alunos. Esta tabela não representa o cálculo efetuado pela faculdade. Pode implementar com o comando while ou for. Calcule e mostre:
    * a média aritmética das duas notas de cada aluno; e
    * a mensagem que está na tabela a seguir:


                            Média aritimética       |   Mesagem
                                Até 3               |   Reprovado
                                Entre 3 e 7         |   Exame
                                De 7 para cima      |   Aprovado

    * o total de alunos aprovados;
    * o total de alunos de exame;
    * o total de alunos reprovados;
    * a média da classe.
"""

contador_reprovados = 0
contador_aprovados = 0
contador_exame = 0
media_sala = 0 # variável acumuladora
for contador in range(1,7):
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    media = (nota1 + nota2) / 2
    if media <= 3:
        print('Reprovados')
        contador_reprovados = contador_reprovados + 1 # incremento
        contador_reprovados += 1
    elif media > 3 and media < 7:
        print('Exame')
        contador_exame += 1 # incremento de forma compacta
    elif media >= 7 and media <= 10:
        print('Aprovados')
        contador_aprovados += 1
        print('A média das notas da sala é de:',media)
        media_sala = media_sala + media # está somando a média de cada aluno
print('Número de alunos aprovados:',contador_aprovados)
print('Número de alunos que ficaram de exame:', contador_exame)
print('Número de alunos reprovados:',contador_reprovados)
print(f'A média foi de: {media_sala/3:.2}')
