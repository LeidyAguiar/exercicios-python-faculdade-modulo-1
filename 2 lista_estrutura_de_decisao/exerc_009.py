"""
9. Faça um programa que receba três notas de um aluno, calcule e mostre a média aritmética e a mensagem constante 
na tabela a seguir. Aos alunos que ficaram para exame, calcule e mostre a nota que deverão tirar para serem aprovados, 
considerando que a média exigida é 6,0.

                        MÉDIA ARITMÉTICA | MENSAGEM
                        0 <= média < 3   | Reprovado
                        3 <= média < 6   | Exame
                        6 <= média <= 10 | Aprovado

SE media >= 3 E media < 6
    ESCREVA “Exame”
    nota_exame = 12 - media
    ESCREVA “Você deve tirar a nota”, nota_exame, “para ser aprovado.”
"""

primeira_nota = float(input('Diga a sua primeira nota: '))
segunda_nota = float(input('Diga a sua segunda nota: '))
terceira_nota = float(input('Diga a sua terceira nota: '))
media = (primeira_nota + segunda_nota + terceira_nota) / 3
print(f'Sua média foi de = {media:.2f}')
if media >= 0 and media < 3:
    print('Reprovado')
elif media >= 3 and media < 6:
    nota_exame = 12 - media
    print('Exame')
    print('Você deve tirar a nota', nota_exame, 'para ser aprovado')
else:
    print('Aprovado')