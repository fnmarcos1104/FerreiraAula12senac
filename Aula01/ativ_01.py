import os

os.system('cls')

import pandas as pd


data = {
    'Código' : [1, 2, 3],
    'Produto' : ['Notebook', 'Smartphone', 'Tablet'],
    'Vendidos' : [120, 340, 210],
    'Cor' : ['Preto', 'Prata', 'Azul'],
    'Categoria' : ['Eletrônicos', 'Eletrônicos', 'Eletrônicos'],
    'Preço' : [3500, 2500, 1200],
    'Faturamento' : [420000, 850000, 252105],
    'Satisfação' : ['Alto', 'Muito Alto', 'Médio']

}

df = pd.DataFrame(data)

print(f'\n {df}')

print('\nVARIÁVEIS QUANTITATIVAS')
print('\nExibindo Códigos dos Produtos')
print(df['Código'])
print(30* '=')

print('\nExibindo Produtos Vendidos')
print(df['Vendidos'])
print(30* '=')

print('\nExibindo Preço dos Produtos')
print(df['Preço'])
print(30* '=')

print('\nExibindo Faturamento Total')
print(df['Faturamento'])
print(30* '=')


print('\nVARIÁVEIS QUALITATIVAS')
print('\nExibindo Produtos')
print(df['Produto'])
print(30* '=')

print('\nExibindo Cores dos Produtos')
print(df['Cor'])
print(30* '=')

print('\nExibindo Categoria dos Produtos')
print(df['Categoria'])
print(30* '=')

print('\nExibindo Satisfação dos Compradores')
print(df['Satisfação'])
print(30* '=')
