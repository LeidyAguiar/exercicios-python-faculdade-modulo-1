"""
19. Faça um programa que monte os oito primeiros termos da sequência de Fibonacci. Pode implementar com o comando while ou for.
"""
numero_elementos_sequencia = 8
elementoN = 0
elementoNmais1 = 1
 
print(elementoN)
print(elementoNmais1)
 
for elemento in range(3,numero_elementos_sequencia):
    valor_fibonacci_atual = elementoN + elementoNmais1
 
    print(valor_fibonacci_atual)
 
    elementoN = elementoNmais1
    elementoNmais1 = valor_fibonacci_atual