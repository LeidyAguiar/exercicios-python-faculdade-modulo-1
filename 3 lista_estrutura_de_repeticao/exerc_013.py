"""
13. Faça um algoritmo que leia de dez alunos altura e nome. Mostre o aluno mais alto e mais baixo e seus respectivos nomes. Pode implementar com o comando while ou for.
"""
print('Exemplo com o while')
contador = 0 # inicialização
while contador < 4: # condição
    nome = input('Digite o nome: ') # é texto (srt ou só input)
    altura = float(input('Informe a altura: '))
    # Dica de programação para encontrar maiores ou menores valores
    if contador == 0: # somente será executado este if uma única vez
        alto = altura # para inicializar as variáveis com valores
        baixo = altura # reais que vieram da digitação
        nome_alto = nome
        nome_baixo = nome
    if altura >= alto:
        alto = altura
        nome_alto = nome
    if altura <= baixo:
        baixo = altura
        nome_baixo = nome
    contador = contador + 1 # incremento
print('Nome do aluno alto',nome_alto,'com altura',alto)
print('Nome do aluno baixo',nome_baixo,'com altura',baixo)