"""
6. Faça um programa para o curso de ADS (6 módulos) que calcule e apresente os seguintes itens:
    * Quantidade de homens e mulheres de cada módulo;
    * Média de idades de cada módulo;
    * Quantidade de homens e mulheres do curso todo;
    * Média de idades do curso todo.
"""
mulheres_curso_todo = 0
homens_curso_todo = 0
media_idade_cursTodo = 0
soma_idade_cursTodo = 0


for i in range(1,7):
    qnte_mulheres = 0
    qnte_homens = 0
    media_idades = 0
    soma_idade = 0
    
    resp = 'S'
    print(f'------------------------Cadastro Módulo {i}--------------------------')
    while resp != 'n' and resp != 'N':
        sexo = str(input('Qual o sexo do aluno[M/H]? '))
        idade = int(input('Qual a idade do aluno? '))
        soma_idade += idade


        if sexo == 'M':
            qnte_mulheres += 1   
        elif sexo == 'H':
            qnte_homens += 1
                    
        
        resp = str(input('Deseja cadastrar outro[S/N]? ')) 

    media_idades = soma_idade / (qnte_mulheres + qnte_homens)
    print('-----------------------------------------------------------')
    print(f'A quantidade de mulheres módulo {i} é: {qnte_mulheres}')
    print(f'A quantidade de homens módulo {i} é: {qnte_homens}')
    print(f'A média de idades módulo {i} é: {media_idades:.2f}')
    mulheres_curso_todo += qnte_mulheres
    homens_curso_todo += qnte_homens
    soma_idade_cursTodo += soma_idade

print('---------------------------TOTAIS----------------------------')
media_idade_cursTodo = soma_idade_cursTodo / (mulheres_curso_todo + homens_curso_todo)
print('A quantidade de mulheres do curso todo é: ',mulheres_curso_todo)
print('A quantidade de homens do curso todo é: ',homens_curso_todo)
print('A média de idades do curso todo é: ',media_idade_cursTodo)
