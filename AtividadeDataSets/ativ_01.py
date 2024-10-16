import os 

os.system('cls')

import pandas as pd

try:
    df = pd.read_csv('Gamepass_Games_v1.csv', sep=',', encoding='utf-8')

    print(df.to_string())
    print(150* '=')



    # FILTRO EM COLUNA ESPECÍFICA
    # print('Listagem da coluna Games:')
    # print(150* '=')
    # jogos = df ['GAME'] 
    # print(jogos.to_string())
    # print(150* '=')


    # FILTRO POR PRODUTO SELECIONADO
    jg = input('Qual jogo deseja filtrar: ')
    filtro_jg = df[df['GAME'] == jg]
    print(filtro_jg[['GAME', 'GAMERS', 'TIME', 'ADDED', 'Game_Score']])
    print(150* '=')


    # FILTRAGEM DE DADOS DE COLUNA
    print('Filtragem de dados em coluna: ')
    filtro_pontuacao = int(input('Filtrar por Game Score acima de: '))
    pontuacao = df[df['Game_Score'] > filtro_pontuacao] 
    print(pontuacao[['GAME', 'Game_Score']])
    print(150* '=')



    # INFORMAÇÕES SOBRE O TIPO DE CADA COLUNA
    print(f'\n Tipo específico de cada coluna:')
    print(150* '=')
    print(df.info())


    # df.to_csv('Base_modificada.cvs', index=False, sep=',', encoding='utf-8')
    # df.to_excel('Gamepass_Base_Modificada.xls', index=False, engine='openpyxl')



except Exception as e:
    print(f'Erro {e}')
    exit()