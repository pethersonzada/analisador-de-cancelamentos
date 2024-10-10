Análise de Cancelamentos de Clientes

Este projeto visa identificar os principais motivos de cancelamento de clientes em uma empresa com mais de 800 mil clientes. A partir dessa análise, são propostas ações para reduzir a taxa de cancelamentos.

Bibliotecas usadas:

    pandas: Manipulação de dados.
    numpy: Suporte para operações matemáticas.
    openpyxl: Leitura de arquivos Excel.
    nbformat e ipykernel: Suporte para notebooks Jupyter.
    plotly: Criação de gráficos interativos.

Como usar:

    Instale as dependências necessárias:

    pip install pandas numpy openpyxl nbformat ipykernel plotly

    Certifique-se de que o arquivo tabela_cancelamentos.csv está no diretório correto.
    Execute o script para analisar as causas dos cancelamentos e gerar gráficos.

Etapas do Processo:

    Limpeza dos dados:
        Colunas irrelevantes e valores nulos/duplicados são removidos.

    Análise de cancelamentos:
        A quantidade e a porcentagem de clientes que cancelaram são calculadas.

    Visualização de dados:
        Gráficos interativos são gerados para cada coluna, destacando a relação entre variáveis como duracao_contrato, ligacoes_callcenter e dias_atraso com o cancelamento.

    Soluções propostas:
        Contrato mensal: Todos os clientes com contrato mensal cancelaram. Solução: oferecer descontos para planos anuais e trimestrais.
        Ligações ao call center: Clientes que ligaram mais de 4 vezes cancelaram. Solução: resolver problemas em no máximo 3 ligações.
        Atraso de pagamento: Clientes que atrasaram mais de 20 dias cancelaram. Solução: política para resolver atrasos em até 10 dias.

    Impacto das ações:
        Após aplicar as soluções propostas, a taxa de cancelamento foi reduzida de 56,7% para 18,4%.
