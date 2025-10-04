#Análise de dados exploratória

#importando bibliotecas
import pandas as pd
import seaborn as srn
import statistics as sts

#importando os dados e criando a variável dataset para armzana-los
dataset = pd.read_csv('tempo.csv', sep=';')

#visualizar os dados
dataset.head()

#explorar dados categóricos, Aparencia, Jogar, Vento
#Aparencia
agrupado_aparencia = dataset.groupby('Aparencia').size()
print(agrupado_aparencia)

#grafico
agrupado_aparencia.plor.bar('Aparencia', color='grey')

#Vento
agrupado_vento = dataset.groupby('Vento').size()
print(agrupado_vento)

#grafico
agrupado_vento.plot.bar('Vento', color='grey')

#Jogar
agrupado_jogar = dataset.groupby('Jogar').size()
print(agrupado_jogar)

#grafico
agrupado_aparencia.plor.bar('jogar', color='grey')

#explorando dados numéricos, Temperatura e Humidade
#Temperatura
dataset['Temperatura'].describe()
srn.boxplot(dataset['Temperatura']).set_title('Temperatura')
srn.histplot(dataset['Temperatura']).set_title('Temperatura')

#Umidade
dataset['Umidade'].describe()
srn.boxplot(dataset['Umidade']).set_title('Umidade')
srn.histplot(dataset['Umidade']).set_title('Umidade')

#tratamento de dados 
#tratando dados faltantes
dataset.isnull().sum()

#Aparencia, valores inválidos
dataset.loc[dataset('Aparencia') == 'menos', 'Aparencia'] = 'sol'

#visualizar resultado do filtro
agrupado_aparencia = dataset.groupby('Aparencia').size()
print(agrupado_aparencia)

#Resolvendo temperatura fora do domínio
dataset.loc[dataset('Temperatura')<-130 | dataset('Temperatura')>130]

#calcular mediana
mediana_temperatura = sts.median(dataset['Temperatura'])

#visualizar mediana
print(mediana_temperatura)

#substituir os valores pela mediana
dataset.loc[dataset('Temperatura')<-130 | dataset('Temperatura')>130] = mediana_temperatura

#verificamos se ainda temoeraturas fora do domínio
dataset.loc [dataset('Temperatura')<-130 | dataser('Temperatura')>130]
#nenhum resultado

#resolvendo umidade fora do domínio e corrigindo NAs (Not available)

agrupado_umidade = dataset.groupby('Umidade').size()
print(agrupado_umidade)

#total de NAs
dataset['Umidade'].isnull().sum()

#calcular mediana
mediana_umidade = sts.median(dataset['Umidade'])
print(mediana_umidade)

#preencher NAs com a mediana
dataset['Umidade'].fillna(mediana_umidade, inplace=True)

#verificar se ainda existem NAs
dataset['Umidade'].isnull().sum()
#nenhum resultado

#corrigindo valores fora do domínio
dataset.loc[dataset('Umidade')<0 | dataset('Umidade')>100] = mediana_umidade

#verificando se ainda existem valores fora do padrão
agrupado_umidade - dataset.groupby('Umidade').size()
print(agrupado_umidade)

#corrigindo NAs em Vento
agrupado_vento = dataset.groupby('Vento').size()
print(agrupado_vento)

#total de NAs
dataset['Vento'].isnull().sum()

#preenchendo NAs

dataset['Vento'].fillna('Falso', inplace=True)

#verificando se ainda existem NAs
dataset['Vento'].isnull().sum()