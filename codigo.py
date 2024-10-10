# Atividade proposta: Você foi contratado por uma empresa com mais de 800 mil clientes para um projeto de Dados. Recentemente a empresa percebeu que da sua base total de clientes, a maioria são clientes inativos, ou seja, que já cancelaram o serviço. Precisando melhorar seus resultados ela quer conseguir entender os principais motivos desses cancelamentos e quais as ações mais eficientes para reduzir esse número.

#Bibliotecas usadas no projeto: pandas | numpy | openpyxl | nbformat | ipykernel | plotly.

#!pip install pandas numpy openpyxl nbformat ipykernel plotly

#Importando bibliotecas.

import pandas as pd
import plotly.express as px

tabela = pd.read_csv("projetos-python/python-insights/tabela_cancelamentos.csv") #(CASO NÃO FUNCIONAR, TENTE ALTERAR O DIRETÓRIO!!)

tabela = tabela.drop(columns="CustomerID") #Retiro a coluna CustumerID (Coluna inútil para a análise em questão).
tabela = tabela.dropna() #Retiro os valores nulos da tabela. (NaN = Not a Number).
tabela = tabela.drop_duplicates() #Retiro as informações duplicadas.

#print(tabela.info()) #Display para projetos ipynb (Melhor visualização da base de dados).

(tabela["cancelou"].value_counts()) #Contar quantas pessoas cancelaram.

(tabela["cancelou"].value_counts(normalize=True)) #Exibir em %.

print(tabela["cancelou"].value_counts(normalize=True).map("{:.1%}".format)) # Formatação numérica (Conta os valores e converte para porcentagens com uma casa decimal)

#Análise das causas dos cancelamentos

#Passo 1 - Criar o gráfico.
#Passo 2 - Exibir o gráfico na tela.

# 1,0 = Cancelou.
# 0,0 = Não cancelou.

for coluna in tabela.columns: #Para cada coluna na tabela, mostre um gráfico para cada uma das colunas.
    grafico = px.histogram(tabela, x=coluna, color="cancelou", text_auto=True)
    grafico.show()

# Clientes do contrato mensal - TODOS cancelaram.
    # Solução proposta - Oferecer desconto nos planos anuais e trimestrais.

# Clientes que ligam mais do que 4 vezes para o call center, cancelam.
    # Solução proposta - Criar um processo para resolver o problema do cliente em no máximo 3 ligações.

# Clientes que atrasaram mais de 20 dias, cancelaram.
    # Solução proposta - Política de resolver atrasos em até 10 dias (equipe financeira).

# Se eu resolver as 3 principais causas do cancelamento, quanto cai a % de cancelamento?

tabela = tabela[tabela["duracao_contrato"]!="Monthly"]
tabela = tabela[tabela["ligacoes_callcenter"]<=4]
tabela = tabela[tabela["dias_atraso"]<=20]

print(tabela["cancelou"].value_counts(normalize=True).map("{:.1%}".format)) # Formatação numérica (Conta os valores e converte para porcentagens com uma casa decimal)

# De 56.7% de cancelamento, cai para 18.4%.
