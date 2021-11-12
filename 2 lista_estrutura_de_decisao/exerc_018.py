"""
18. Faça um programa que receba o código correspondente ao cargo de um funcionário e seu salário atual e mostre o cargo, o valor do aumento e seu novo salário. 
Os cargos estão na tabela a seguir.

  CÓDIGO | CARGO        | PERCENTUAL
  1      | Escriturário |  50%
  2      | Secretário   |  35%
  3      | Caixa        |  20%
  4      | Gerente      |  10%
  5      | Diretor      |  Não tem aumento
"""
cargo = float(input('Informe o seu código correspondente ao cargo: '))
salario = float(input('Informe seu salário atual: '))

if cargo == 1:
    print('O seu cargo é o de Escriturário')
    aumento = salario * 50 / 100
    print('O valor do aumento é de:',aumento)
    novo_sal = salario + aumento
    print('O seu novo salário é:', novo_sal)
elif cargo == 2:
    print('O seu cargo é o de Secretário')
    aumento = salario * 35 / 100
    print('O valor do aumento é de:', aumento)
    novo_sal = salario + aumento
    print('O seu novo salário é:', novo_sal)
elif cargo == 3:
    print('O seu cargo é o de Caixa')
    aumento = salario * 20 / 100
    print('O valor do aumento é de:', aumento)
    novo_sal = salario + aumento
    print('O seu novo salário é:', novo_sal)
elif cargo == 4:
    print('O seu cargo é o de Gerente')
    aumento = salario * 10 / 100
    print('O valor do aumento é de:', aumento)
    novo_sal = salario + aumento
    print('O seu novo salário é:', novo_sal)
elif cargo == 5:
    print('O seu cargo é o de Diretor')
    aumento = salario * 0 / 100
    print('O valor do aumento é de:', aumento)
    novo_sal = salario + aumento
    print('O seu novo salário é:', novo_sal)