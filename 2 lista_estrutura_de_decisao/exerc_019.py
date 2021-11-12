"""
19. Faça um programa que apresente o menu a seguir, permita ao usuário escolher a opção desejada, receba os dados necessários para executar a operação e mostre o resultado. 
Verifique a possibilidade de opção inválida e não se preocupe com restrições, como salário negativo.

Menu de opções
1. Imposto
2. Novo salário
3. Classificação
Digite a opção desejada:

* Na opção 1: receber o salário de um funcionário, calcular e mostrar o valor do imposto usando as regras a seguir.

                                SALÁRIO                                        | PERCENTUAL DO IMPOSTO
                                Menor que  500,00                              | 5%
                                De 500,00 (inclusive) a 850,00 (inclusive)     | 10%
                                Acima de  850,00                               | 15%

* Na opção 2: receber o salário de um funcionário, calcular e mostrar o valor do novo salário, usando as regras a seguir.

                                SALÁRIO                                        | AUMENTO
                                Maior que  1.500,00                            | 25,00
                                De 750,00 (inclusive) a 1.500,00 (inclusive)   | 50,00
                                De 450,00 (inclusive) a 750,00                 | 75,00
                                Menor que  450,00                              | 100,00

* Na opção 3: receber o salário de um funcionário e mostrar sua classificação usando a tabela a seguir.

                                    SALÁRIO                   |  CLASSIFICAÇÃO
                                    Até 700,00 (inclusive)    |  Mal remunerado
                                    Maiores que 700,00        |  Bem remunerado
"""
print('Menu de Opções:')
print('1. Imposto')
print('2. Novo Salário')
print('3. Classificação')
opcao = int(input('Digite a opção desejada: '))
salario = float(input('Informe seu salário: '))
if opcao == 1:
    if salario < 500:
        imposto = salario * 5 / 100
    elif salario >= 500 and salario <= 850:
        imposto = salario * 10 / 100
    elif salario > 850:
        imposto = salario * 15 / 100
    print('O valor do imposto é de:', imposto)
elif opcao == 2:
    if salario > 1500:
        aumento = salario + 25
    elif salario >= 750 and salario <= 1500:
        aumento = salario + 50
    elif salario >= 450 and salario < 750:
        aumento = salario + 75
    elif salario < 450:
        aumento = salario + 100
    print('O valor do novo salário é:', aumento)
elif opcao == 3:
    if salario <= 700:
        print('Mal remunerado')
    else:
        print('Bem remunerado')


