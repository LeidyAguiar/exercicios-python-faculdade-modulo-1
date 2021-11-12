"""
22. Faça um programa que receba:
    * o preço unitário,
    * a refrigeração (S para os produtos que necessitem de refrigeração e N para os que não necessitem)
    * a categoria (A — alimentação; L — limpeza; e V — vestuário)

**Calcule e mostre:**
    * O custo de estocagem, calculado de acordo com a tabela a seguir.

                                    Preço unitário              | Refrigeração          | Categoria      |      Custo de estocagem
                                    Até 20                      |       -               |   A            |          2,00
                                    Até 20                      |       -               |   L            |          3,00
                                    Até 20                      |       -               |   V            |          4,00
                                --------------------------------|-----------------------|----------------|---------------------------
                                    Entre 20 e 50 (inclusive)   |       S               |   -            |          6,00
                                    Entre 20 e 50 (inclusive)   |       N               |   -            |          0,00 
                                --------------------------------|-----------------------|----------------|---------------------------
                                    Maior que 50                |       S               |    A           |          5,00
                                    Maior que 50                |       S               |    L           |          2,00
                                    Maior que 50                |       S               |    V           |          4,00
                                    Maior que 50                |       N               |    A ou V      |          0,00  
                                    Maior que 50                |       N               |    L           |          1,00 


* O imposto calculado de acordo com as regras a seguir:
  * Se o produto possuir **categoria A** e **refrigeração S**, seu imposto será de 2% sobre o preço unitário; caso contrário, será de 4%.
  * O preço final, ou seja, preço unitário mais custo de estocagem mais imposto.
  * A classificação calculada usando a tabela a seguir.

                                Preço final                         |   Classificação
                                Até 20,00                           |       Barato
                                Entre 20,00 e 100,00 (inclusive)    |       Normal
                                Acima de R$ 100,00                  |       Caro

* A média dos valores adicionais, ou seja, a média dos custos de estocagem e dos impostos dos doze produtos.
* O maior preço final.
* O menor preço final.
* O total dos impostos.
* A quantidade e a classificação de produtos com classificação barato.
* A quantidade e a classificação de produtos com classificação caro.
* A quantidade e a classificação de produtos com classificação normal.
"""
total_de_produtos = 4
 
total_de_produtos_baratos = 0
total_de_produtos_normais = 0
total_de_produtos_caros = 0
total_de_custo_adicionais_de_todos_produtos = 0
total_de_custos_adicionais = 0
custo_adicional_do_produto = 0
custo_de_estocagem = 0
imposto_sobre_o_produto = 0
preco_final_do_produto = 0
preco_final_sobre_produto = 0
 
for produto in range(total_de_produtos):
    preco_do_produto = float(input('Qual o preço do produto: '))
    produto_necessita_de_refrigeracao = str(input('O produto necessita de refrigeração (S ou N): '))
    categoria_do_produto = str(input('Qual a categoria do produto (A, L ou V): '))
    
    if preco_do_produto <= 20:
        if categoria_do_produto == 'A':
            custo_de_estocagem = 2
        if categoria_do_produto == 'L':
            custo_de_estocagem = 3
        if categoria_do_produto == 'V':
            custo_de_estocagem = 4
 
    if preco_do_produto > 20 and preco_do_produto <= 50:
        if produto_necessita_de_refrigeracao == 'S':
            custo_de_estocagem = 6
        else:
            custo_de_estocagem = 0
 
    if preco_do_produto > 50:
        if produto_necessita_de_refrigeracao == 'S':
            if categoria_do_produto == 'A':
                custo_de_estocagem = 5
            if categoria_do_produto == 'L':
                custo_de_estocagem = 2
            if categoria_do_produto == 'V':
                custo_de_estocagem = 4
        else:
            if categoria_do_produto == 'A' or categoria_do_produto == 'V':
                custo_de_estocagem = 0
            if categoria_do_produto == 'L':
                custo_de_estocagem = 1
 
    if categoria_do_produto == 'A' and produto_necessita_de_refrigeracao == 'S':
        imposto_do_produto = 2 / 100
    else:
        imposto_do_produto = 4 / 100
 
    preco_final_do_produto = preco_do_produto + custo_de_estocagem + imposto_sobre_o_produto
 
    print('Custo de estocagem, imposto do produto e preço final é respctivamente:',custo_de_estocagem,'-',imposto_do_produto,'-',preco_final_do_produto)
    if preco_final_do_produto <= 20:
        total_de_produtos_baratos += 1
        classificacao_do_produto = 'PRODUTO BARATO'
    
    if preco_final_do_produto > 20 and preco_final_sobre_produto <=  20:
        total_de_produtos_normais += 1
        classificacao_do_produto = 'PRODUTO NORMAL'
    
    if preco_final_do_produto > 100:
        total_de_produtos_caros += 1
        classificacao_do_produto = 'PRODUTO CARO'
        custo_adicional_do_produto = custo_de_estocagem + imposto_sobre_o_produto
        total_de_custo_adicionais_de_todos_produtos += custo_adicional_do_produto
        total_de_produtos_caros += imposto_sobre_o_produto
    
    if produto == 0:
        preco_do_produto_mais_caro = preco_final_do_produto
        preco_do_produto_mais_barato = preco_final_do_produto
    else:
        if preco_do_produto_mais_caro < preco_final_do_produto:
            preco_do_produto_mais_caro = preco_final_do_produto
        if preco_do_produto_mais_barato > preco_final_do_produto:
            preco_do_produto_mais_barato = preco_final_do_produto
 
media_dos_valores_adicionais = total_de_custo_adicionais_de_todos_produtos / total_de_produtos
 
print('A média dos valores adicionais é:',media_dos_valores_adicionais)
print('Preço do produto mais caro:',preco_do_produto_mais_caro)
print('Preço do produto mais barato:',preco_do_produto_mais_barato)
print('Total de produtos baratos:',total_de_produtos_baratos)
print('Total de produtos normais:',total_de_produtos_normais)
print('Total de produtos caros:',total_de_produtos_caros)