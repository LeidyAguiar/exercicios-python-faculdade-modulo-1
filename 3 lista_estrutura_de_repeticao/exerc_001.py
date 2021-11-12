"""
1. Faça um algoritmo que mostre 10 vezes a frase “Bem vindo a Fatec!”. Pode implementar com o comando while ou for.
"""
print('Exemplo com o while')
qalunos = 1 # inicialização
while qalunos <= 10: # condição
    print(qalunos, "Bem vindo a Fatec")
    qalunos = qalunos + 1 #incremento

print('\nExemplo com o for')
for contador in range(1,11):
    print(contador, "Bem vindo a Fatec")