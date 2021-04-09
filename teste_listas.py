import pandas as pd
script_ini = pd.read_csv('C:\\Users\\vinis\\Desktop\\listas_paneas\\lista_1833.csv', sep=';')
script_hj = pd.read_csv('C:\\Users\\vinis\\Desktop\\listas_paneas\\lista_1834.csv', sep=';')
#Transformo ambos os DatasFrames em listas e ordeno por ondem crescente.
df = sorted(script_ini['TELEFONE'].unique())
df2 = sorted(script_hj['Telefone'].unique())

# #lista vazia na qual os valores que não tiverem sido discados vão ser inseridos
l = []
# # Para cada item no DataFrame primário, se o item não estiver no DataFrame secundário, insere na lista vazia.
for i in df:
    if i not in df2:
        l.append(i)
df3 = pd.DataFrame(l)
df3.to_csv('C:\\Users\\vinis\\Desktop\\Programação\\ligacoes.csv')
print(l)