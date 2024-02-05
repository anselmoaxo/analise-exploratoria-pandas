import pandas as pd
import matplotlib.pyplot as plt

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


df['Cidade'].value_counts().plot.bar(title='Total de Vendas por Cidades', color='red')
plt.xlabel('Cidades')
plt.ylabel('Total de Vendas')
plt.style.use('ggplot')
plt.show()