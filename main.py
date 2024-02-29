import pandas as pd

## lendo o arquivo csv como um dataframe do pandas
df = pd.read_csv("desafio analise de dados\gapminder.csv")

## Printando o nome das colunas
print(df.columns)

## renomeando as colunas do nosso dataframe
df.rename(columns={
    'country':'pais',
    'continent':'continente',
    'year':'ano',
    'lifeExp':'expectativa de vida',
    'pop':'população total',
    'gdpPercap':'PIB percap'}, inplace= True)

## Printando o nome das colunas
print(df.columns)

## Total de linhas e colunas
print(df.shape)

## printando os tipos de dados das nossas colunas
print(df.dtypes)

## print as utimas linhas das nossa colunas
print(df.tail())

## retornando informações estatisticas para nossas tabela
print(df.describe())

## valor maximo da coluna ano
print(df.ano.max())

## retornando apenas os valores unicos de uma coluna
print(df.continente.unique())

## retornando apenas as 5 primeiras linhas de um unico continente
print(df.loc[df.continente == 'Asia'].head())

## agrupamento de dados, nesse caso está printando a quantidade de paises para cada continente
print(df.groupby("continente")['pais'].nunique())

## agrupamento de dados, nesse caso está printando a espectativa média para cada ano da coluna ano
print(df.groupby('ano')['expectativa de vida'].mean())

## agrupamento de dados, nesse caso está printando a média do pib para cada ano
print(df.groupby('ano')['PIB percap'].mean())


