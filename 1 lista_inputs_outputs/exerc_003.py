"""
3. Faça um programa que receba três notas, calcule e mostre a média aritmética.

  LEIA nota1, nota2, nota3
  media = (nota1 + nota2 + nota3) / 3
  ESCREVA media
"""
# entrada
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))

# processamento
media = (nota1 + nota2 + nota3) / 3

# saída
print('A média é =', media)