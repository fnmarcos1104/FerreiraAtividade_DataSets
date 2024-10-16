import os 

os.system('cls')

import pandas as pd

try:
    df = pd.read_csv('Gamepass_Games_v1.csv', sep=',', encoding='utf-8')

    print(df.to_string())


    # FILTRO EM COLUNA ESPECÍFICA
    # jogos = df ['GAME'] 
    # print(jogos.to_string())

    df.to_csv('Base_modificada.cvs', index=False, sep=',', encoding='utf-8')
    df.to_excel('classic_disco_modificado.xls', index=False, engine='openpyxl')



except Exception as e:
    print(f'Erro {e}')
    exit()