import os

os.system('cls')

import pandas as pd

data = {
    'Nome' : ['Ana', 'João', 'Maria'],
    'Idade' : [23, 35, 29],
    'Gênero' : ['F', 'M', 'F'],
    'Altura' : [1.70, 1.80, 1.65]
}

df = pd.DataFrame(data)

print(f'\n {df}')

print('\nVARIÁVEIS QUANTITATIVAS')
print('\nExibindo idade')
print(df['Idade'])

print('\nExibindo altura')
print(df['Altura'])