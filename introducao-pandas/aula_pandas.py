import pandas as pd

# lendo arquivos
df01 = pd.read_excel("introducao-pandas/Aracaju.xlsx")
df02 = pd.read_excel("introducao-pandas/Fortaleza.xlsx")
df03 = pd.read_excel("introducao-pandas/Natal.xlsx")
df04 = pd.read_excel("introducao-pandas/Recife.xlsx")
df05 = pd.read_excel("introducao-pandas/Salvador.xlsx")

# Juntando todos os arquivos
df = pd.concat([df01, df02, df03, df04, df05])

# Verifica o tipos das colunas
# df.dtypes

# Altera tipo da Colna LojaID para Object
df['LojaID'] = df['LojaID'].astype('object')

# Encontra valor nulos 
df.isnull().sum()

# Seleciona a Caoluna com Valores Nulos e subistiui pela Média
#df['Vendas'].fillna(df['Vendas'].mean(), inplace=True)

# Selecionando a coluna com Valores Nulos e substituindo por zero
# df['Vendas'].fillna(0, inplace=True)

# Apagando todos as linhas com Valores Nulos.
# df['Vendas'].dropna(inplace=True)

# Criando novas Colunas

df['Receita']= df['Vendas'].mul(df['Qtde'])

# realiza o agrupamento por ano
Agrupamento_ano = df.groupby(df['Data'].dt.year)['Receita'].sum()

df['ano_venda'] = df['Data'].dt.year

print(df['ano_venda'].max())