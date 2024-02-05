import pandas as pd
import matplotlib.pyplot as plt



# criando nosso DataFrame
df = pd.read_excel('Analise-Exploratoria/AdventureWorks.xlsx')

# visualizando as 5 primeiras Linhas
# df.head()

# quantidades de Linhas do arquivo
# df.shape()

# verificando os tipos de dados das colunas
# df.dtypes

receita_total = round(df['Valor Venda'].sum(), 2)

# Criando Coluna Custo   Custo Unitario * Quantidade
df['Custo'] = df['Custo Unitário'].mul(df['Quantidade'])

# Criando Coluna Lucro  Valor venda - Custo
df['Lucro'] = df['Valor Venda'] - df['Custo']

lucro_total = round(df['Lucro'].sum(), 2)
# print(lucro_total)
# print(df.head(1))


# Criando coluna do Tempo de envio do Produto 
df['Tempo Envio'] = (df['Data Envio'] - df['Data Venda']).dt.days

# pegando a Média do tempo de Envio por Marca
media_marca = df.groupby('Marca')['Tempo Envio'].mean()

lucro_ano_marca = df.groupby([df['Data Venda'].dt.year, 'Marca'])['Lucro'].sum()

# Grafico Total de Produto Vendido
plt.style.use('seaborn-v0_8-dark')
total_produto_vendido = df.groupby('Produto')['Quantidade'].sum().sort_values(ascending=True)
total_produto_vendido.plot.barh(title='Total Produtos Vendidos')
plt.xlabel('Total')
plt.ylabel('Produtos')
plt.show()

lucro_ano = df.groupby(df['Data Venda'].dt.year)['Lucro'].sum()
lucro_ano.plot.bar(title='Lucro x Ano')
plt.xlabel('Ano')
plt.ylabel('Receita')
plt.show()

df_2009 = df[df['Data Venda'].dt.year == 2009]
lucro_ano_2009 = df_2009.groupby(df['Data Venda'].dt.month)['Lucro'].sum()
lucro_ano_2009.plot(title='Lucro x Mês')
plt.xlabel('Mês')
plt.ylabel('Receita')
plt.show()

lucro_marca = df.groupby('Marca')['Lucro'].sum()
lucro_marca.plot.barh(title='Lucros x Marca')
plt.xlabel('Marca')
plt.ylabel('Lucro')
plt.xticks(rotation='horizontal')
plt.show()


lucro_classe = df.groupby('Classe')['Lucro'].sum()
lucro_classe.plot.barh(title='Lucros x Classe')
plt.xlabel('Classe')
plt.ylabel('Lucro')
plt.xticks(rotation='horizontal')
plt.show()


df.to_excel('Analise-Exploratoria/Nova_Analise.xlsx')