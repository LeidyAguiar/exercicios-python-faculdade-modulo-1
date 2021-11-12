"""
6. Faça um programa que carregue um vetor com dez nomes e faça uma verificação se um determinado nome esta nesse vetor. 
Não use nenhuma função pronta da linguagem Python.
"""

vet_nome = []
strnome = ''
pesquisa = False
for i in range(5):
    vet_nome.append(str(input('Digite um nome: ')))
strnome = str(input('Digite o nome a ser pesquisado: '))
for i in range(5):
    if vet_nome[i] == strnome:
        pesquisa = True
if pesquisa == True:
        print('Encontrou')
else:
    print('Não encontrou')
    