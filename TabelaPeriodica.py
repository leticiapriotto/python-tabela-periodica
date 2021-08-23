import csv
from os import system

#adicionar outros elementos
#adicionar estados a temperatura ambiente
#corrigir NameError
#adicionar opcao de filtrar elementos por grupo (gases nobres etc)
#opcao exibir somente um dado de todos os elementos

tabela_periodica = {}

arq = csv.reader(open('tabela.csv'), delimiter=';') #le o arquivo que contem os elementos
for i,dado_linha in enumerate(arq):
    if i == 0: #pula a primeira linha do arquivo na hora da leitura
        continue

    dados = {}
    dados['simbolo'] = dado_linha[0] 
    dados['nome'] = dado_linha[1]
    dados['numero atomico'] = dado_linha[2]
    dados['massa atomica'] = dado_linha[3]
    dados['configuracao eletronica'] = dado_linha[4]
    dados['linha'] = dado_linha[5]
    dados['coluna'] = dado_linha[6]

    tabela_periodica[dados['simbolo']] = dados #insere os dados 

system('cls')

print('='*50)
print('Tabela Periódica'.center(50))
print('='*50)

busca1 = True #para criar o loop
while busca1:
    print('\nEscolha uma opção:\n[1] Mostrar todos os dados de todos os elementos\n[2] Mostrar os dados de um só elemento\n[3] Sair do programa')
    opcao = int(input('\nSua opção: '))
    print('')

    #exibe todos os dados de todos os elementos
    if opcao == 1:
        for item in tabela_periodica:
            elemento = tabela_periodica[item]
            print(f'Dados do Elemento {elemento["simbolo"]}')
            print(f'Simbolo: {elemento["simbolo"]}')
            print(f'Nome: {elemento["nome"]}')
            print(f'Número Atômico: {elemento["numero atomico"]}')
            print(f'Massa Atômica: {elemento["massa atomica"]}')
            print(f'Configuração Eletrônica: {elemento["configuracao eletronica"]}')
            print(f'Linha da Tabela: {elemento["linha"]}')
            print(f'Coluna da Tabela: {elemento["coluna"]}')
            print('-'*50)

    #exibe os dados de somente um elemento
    elif opcao == 2:
        system('cls')
        print('='*50)
        print('Elementos disponíveis para pesquisa:'.center(50))
        print('='*50)
        print('')
        for item in tabela_periodica:
            elemento = tabela_periodica[item]
            print(f'Simbolo: {elemento["simbolo"]}')
        
        print('')

        elementoEscolhido = str(input('Digite o simbolo do elemento que você deseja ver: '))
        print(f'[1] Ver todas as informações do elemento {elementoEscolhido} \n[2] Escolher uma informação específica\n')
        opcao = int(input('Sua opção: '))
        soma = 0

        #mostra todas as informacoes do elemento digitado
        if opcao == 1:
            for item in tabela_periodica:
                elemento = tabela_periodica[elementoEscolhido]
                print(f'Dados do Elemento {elemento["simbolo"]}')
                print(f'Simbolo: {elemento["simbolo"]}')
                print(f'Nome: {elemento["nome"]}')
                print(f'Número Atômico: {elemento["numero atomico"]}')
                print(f'Massa Atômica: {elemento["massa atomica"]}')
                print(f'Configuração Eletrônica: {elemento["configuracao eletronica"]}')
                print(f'Linha da Tabela: {elemento["linha"]}')
                print(f'Coluna da Tabela: {elemento["coluna"]}')
                print('')
                soma = 1
                if soma == 1:
                    break 
        
        #exibe quais as informacoes disponiveis e mostra ao usuario a que ele escolher
        elif opcao == 2:
            print(f'\nElemento Escolhido: {elementoEscolhido}')
            print('Digite a informação que deseja ver:\n\n- nome\n- numero atomico\n- massa atomica\n- configuracao eletronica\n- linha \n- coluna')
            opcaoInfo = input('Dado desejado: ')

            print(f'{opcaoInfo}: {tabela_periodica[elementoEscolhido][opcaoInfo.lower()]}')
        
        #caso opcao seja invalida
        else:
            print('Digite uma opção válida')

    
    #encerra o programa
    elif opcao == 3:
        pesquisando = False   

    #caso opcao seja invalida
    else:
        print('Digite uma opção válida')

