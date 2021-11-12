"""
2. Faça um algoritmo que mostre o cumprimento 'Olá' para o nome de alguém (4 pessoas). Exemplo ‘Olá Mariana’. Pode implementar com o comando while ou for.
"""
print('Exemplo com o while')
cumprimento = 1 # inicialização
while cumprimento <= 4: # condição
    nome = str(input('Informe seu nome: '))
    print(cumprimento, 'Olá,',nome, )
    cumprimento = cumprimento + 1
print('Término da execução')