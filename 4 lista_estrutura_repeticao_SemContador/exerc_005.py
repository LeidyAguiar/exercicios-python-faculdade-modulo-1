"""
5. No final do ano muitas pessoas compram presentes. Faça um programa que registre alguns dados das pessoas, usando como critério de parada a letra ‘n’, 
para a pergunta “Deseja cadastrar outro (‘s’/’n’)?”, para identificar o perfil dos compradores numa loja de roupas e apresente como resultado a:
    * Quantidade de mulheres e de homens;
    * Quantidade de mulheres e de homens abaixo e acima de 18 anos.
"""
resp = 'S'
mulheres = 0
homens = 0
h_maior_18 = 0
m_maior_18 = 0
m_abaixo_18 = 0
h_abaixo_18 = 0
while resp != 'n' and resp != 'N':
    sexo = str(input('Qual o seu sexo?[M/H] '))
    idade = int(input('Qual a sua idade? '))
    if sexo == 'M' or sexo == 'm':
        mulheres += 1 
        if idade >= 18:
            m_maior_18 += 1     
    elif sexo == 'H' or sexo == 'h':
        homens += 1
        if idade >= 18:
            h_maior_18 += 1
            
    m_abaixo_18 = mulheres - m_maior_18
    h_abaixo_18 = homens - h_maior_18
    resp = str(input('Deseja cadastrar outro[S/N]? '))
print('Quantidade de mulheres: ',mulheres)
print('Quantidade de homens: ',homens)
print('Quantidade de mulheres acima de 18 anos: ',m_maior_18)
print('Quantidade de homens acima de 18 anos: ',h_maior_18)
print('Quantidade de mulheres abaixo de 18 anos: ',m_abaixo_18)
print('Quantidade de homens abaixo de 18 anos: ',h_abaixo_18)
