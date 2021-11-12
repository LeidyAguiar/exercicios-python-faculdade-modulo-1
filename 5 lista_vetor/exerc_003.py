"""
3. Faça um programa que carregue um vetor de dez elementos que contenha o nome de pessoas e outro que contenha o peso, encontre qual a 
pessoa mais gorda e mais magra e apresente o nome o peso das mesmas.​ Use dois vetores, um para peso e outro para nome. Não use nenhuma função pronta da linguagem Python.
"""
vet_peso = [] # declarar a variável vetor vazia, dever ser antes do laço de repetição
vet_nome = []

for i in range(5):
    vet_nome.append(input('Digite o nome: '))
    vet_peso.append(float(input('Digite o peso: ')))
    if i == 0: # inicialização das variáveis de maior e menor valor apenas quando for igual a ZERO
        gordo = vet_peso[i]
        magro = vet_peso[i]
        nome_gordo = vet_nome[i]
        nome_magro = vet_nome[i]
    if vet_peso[i] > gordo:
        gordo = vet_peso[i]
        nome_gordo = vet_nome[i]
    elif vet_peso[i] < magro:
        magro = vet_peso[i]
        nome_magro = vet_nome[i]
print(nome_gordo, 'possui ',gordo,' kg +')
print(nome_magro, 'possui ',magro,' kg -')

for i in range(5): # este trecho é opcional para este exercício
    print('Nome: ',vet_nome[i],'\tpeso: ',vet_peso[i],' kg')
