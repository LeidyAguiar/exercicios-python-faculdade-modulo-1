"""
23. Faça um programa para resolver equações do 2 o grau.

ax² + bx + c = 0

A variável a deve ser diferente de zero

  * delta = b ** 2 - 4 * a * c
  * delta < 0. Não existe raiz real
  * delta = 0. Existe uma raiz real
    * x = (-b) / (2 * a)

  * delta > 0. Existem duas raízes reais
    * x1 = (-b + delta )/ (2 * a)
    * x2 = (-b - delta )/ (2 * a)
"""
import math
a = int(input('Informe um número para a: '))
b = int(input('Informe um número para b: '))
c = int(input('Informe um número para c: '))

if a == 0:
    print('Estes valores não formam uma equação de segundo grau')
else:
    delta = (b ** 2) - ( 4 * a * c)
    if delta < 0:
        print('Não existe raiz real')
    if delta == 0:
        print('Existe uma raiz real')
        x1 = (- b) / (2 * a)
        print(x1)
    if delta > 0:
        print('Existem duas raízes reais')
        x1 = ((- b) + math.sqrt(delta)) / (2 * a)
        x2 = ((- b) - math.sqrt(delta)) / (2 * a)
        print(f'x1= {x1:.2f}',';',f'x2= {x2:.2f}')