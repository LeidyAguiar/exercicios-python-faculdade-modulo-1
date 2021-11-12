"""
2. Foi realizada uma pesquisa sobre algumas características físicas de ALGUNS habitantes de uma região, NÃO FOI INFORMADA A QUANTIDADE TOTAL, então use como critério de parada, 
idade igual a zero para encerrar a repetição. Preste atenção nesse detalhe, pois somente poderá usar a função append, quando for digitado uma idade válida. 

- Foram coletados os seguintes dados de cada habitante: idade, sexo (M/F), cor dos olhos (A - azuis ou C - castanhos). Escolha se quer armazenar uma letra ou a palavra, para cor dos olhos. 

- Em Python crie um programa que leia esses dados, armazenando-os em vetores, uma para idade, outro para sexo (apenas uma letra) e outro para cor dos olhos.

- Calcule e apresente:
    * Média de idades das pessoas com olhos castanhos;
    * Quantidade de pessoas que foram entrevistadas
    * Quantidade de pessoas do sexo feminino com idade entre 18 e 35 anos(inclusive) e que tenham olhos azuis.

* Observação: pode usar o operador ***in*** e a função ***len***() apenas. Outras funções prontas da linguagem Python, não serão aceitas.
"""
vet_idade = []
vet_sexo = []
vet_olhos = []
idade = 1
cor_olhos = ''
sexo = ''
soma_idade_c = 0
media = 0
qntd_c = 0
sexo_feminino = 0

while idade > 0:
    idade = int(input('Informe a idade: '))
    if idade > 0:
        vet_idade.append(idade)
        sexo = str(input('Digite o sexo(M/F): '))
        vet_sexo.append(sexo)
        cor_olhos = str(input('Informe a cor dos olhos(A/C): '))
        vet_olhos.append(cor_olhos)
        if cor_olhos == 'C':
            soma_idade_c += idade
            qntd_c += 1
        if sexo == 'F' and idade >= 18 and idade <= 35 and cor_olhos == 'A':
            sexo_feminino += 1
if qntd_c > 0:
    media = soma_idade_c / qntd_c

print(f'Média de pessoas com olhos castanhos: {media:.2f}')
print('Quantidade de pessoas entrevistadas: ',len(vet_idade))
print('Quantidade de pessoas do sexo feminino entre 18 e 35 anos e que tenham olhos azuis: ',sexo_feminino)


