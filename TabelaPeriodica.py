import csv

tabela_periodica = {}

arq = csv.reader(open('tabela.txt'), delimiter=';')
for i,dado_linha in enumerate(arq):
    if i == 0:
        continue

    dados = {}
    dados['simbolo'] = dado_linha[0] 
    dados['nome'] = dado_linha[1]
   
    tabela_periodica[dados['simbolo']] = dados
