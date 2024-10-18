import os

os.system('cls')

import pandas as pd


produtos = ['Notebook', 'Smartphone', 'Tablet', 'Smartwatch', 'Camera']
quantidade_estoque = [15, 30, 20, 10, 25]

estoque = pd.Series(quantidade_estoque, index=produtos)


# print('Séries Estoque e Produtos: ')
# print(estoque)


# SELECIONANDO UM VALOR ESPECÍFICO PELO ÍNDICE
print('\n Quantidade de notebooks em estoque')
print(estoque['Notebook'])

# SELECIONANDO MÚLTIPLOS VALORES
print('\n Estoque de notebooks e cameras')
print(estoque[['Notebook', 'Camera']].values)

# FILTRANDO PRODUTOS COM ESTOQUE ABAIXO DE 20
print('\nProdutos com estoque abaixo de 20 unidades:')
print(estoque[estoque > 20])

# OPERAÇÃO ARITMÉTICA: AUMENTAR ESTOQUE EM 5 UNIDADES
print('\nAumentando o estoque em 5 unidades para todos os produtos:')
print(estoque + 5)