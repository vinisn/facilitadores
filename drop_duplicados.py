import pandas as pd
#Importando o arquivo com numeros duplicados
dataset = pd.read_csv('C:\\Users\\vinis\\Desktop\\listas_paneas\\report_ligacao_20210409_143857_862.csv', sep=';')
#Transformando o dataset em um DataFrame
listatel = pd.DataFrame(dataset) 
#Alterando o nome da coluna principal para que seja possivel realizar o drop e ou a navegação
listatel.columns = ['Telefone']
#Dropando todos os duplicados e mantendo somente 1 numero de cada.
listatel.drop_duplicates(subset = ['Telefone'], inplace = True)
#Salvando o DataFrame em um arquivo Excel
#listatel.to_csv('C:\\Users\\vinis\\Desktop\\Programação\\tentativa.csv')
print(listatel)