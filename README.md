Este projeto foi desenvolvido para uma empresa com uma base de mais de 800 mil clientes. O objetivo principal é identificar os principais motivos pelos quais os clientes cancelam o serviço e propor soluções eficientes para reduzir o número de cancelamentos.
Objetivo do Projeto

Analisar a base de dados de clientes da empresa, composta principalmente por clientes inativos (aqueles que já cancelaram o serviço), para identificar padrões nos cancelamentos. Com base nos insights obtidos, foram sugeridas ações específicas que podem ajudar a reduzir a taxa de cancelamento.
Principais Soluções Propostas

    Clientes com contrato mensal:
        Todos os clientes com contratos mensais cancelaram.
        Solução: Oferecer descontos para migrar clientes para contratos anuais ou trimestrais.

    Clientes que ligam para o call center mais de 4 vezes:
        Esses clientes tendem a cancelar o serviço.
        Solução: Melhorar os processos de atendimento, com o objetivo de resolver os problemas dos clientes em, no máximo, 3 ligações.

    Clientes que atrasaram mais de 20 dias no pagamento:
        Atrasos superiores a 20 dias estão fortemente associados ao cancelamento.
        Solução: Implementar uma política de regularização de atrasos em até 10 dias, contando com o apoio da equipe financeira.

Ferramentas e Bibliotecas Utilizadas

    pandas: Para a manipulação de dados.
    numpy: Suporte para operações numéricas e arrays.
    openpyxl: Leitura e gravação de arquivos Excel.
    nbformat e ipykernel: Integração e execução em notebooks.
    plotly: Visualização de dados interativa, para gerar gráficos e histogramas das análises.

Etapas do Projeto

    Carregamento dos Dados: A base de dados de cancelamentos foi carregada e processada com a remoção de valores duplicados e nulos, além da exclusão de colunas irrelevantes como CustomerID.

    Análise Exploratória dos Dados: Foram gerados gráficos e histogramas para cada uma das variáveis da base de dados, com o objetivo de entender quais fatores mais influenciam o cancelamento.

    Propostas de Ação: Com base na análise, foram identificados três fatores principais que influenciam os cancelamentos. Para cada um, foi proposta uma ação corretiva visando reduzir a taxa de cancelamento.

    Simulação Pós-Ajustes: Após simular a aplicação das ações sugeridas, a taxa de cancelamento foi reduzida de 56.7% para 18.4%.

Como Executar o Projeto

    Instale as bibliotecas necessárias:

    bash

pip install pandas numpy openpyxl nbformat ipykernel plotly

Execute o arquivo principal do projeto para carregar e analisar os dados.

Modifique ou aplique novos filtros e analise as mudanças nos resultados com base nas ações sugeridas.
