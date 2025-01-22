import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

# Carregar os dados
df = pd.read_csv('simulação_dados_vacinacao.csv')

# Título do dashboard
st.title("Dashboard de Vacinação")

# Descrição
st.write("""
    Este dashboard apresenta dados sobre as vacinas administradas em diferentes estados do Brasil.
    Ele inclui gráficos interativos para visualizar a quantidade de vacinas aplicadas ao longo do tempo,
    e a distribuição por estado e tipo de vacina.
""")

# Gráfico de Pizza - Distribuição de vacinas por estado
st.subheader("Distribuição de Vacinas por Estado")
estado_vacinas = df.groupby('Estado')['Vacinas Administradas'].sum().reset_index()
fig_pizza = px.pie(estado_vacinas, names='Estado', values='Vacinas Administradas', title='Distribuição das Vacinas por Estado')
st.plotly_chart(fig_pizza)

# Gráfico de Barras - Quantidade de Vacinas Administradas por Tipo
st.subheader("Quantidade de Vacinas por Tipo")
tipo_vacinas = df.groupby('Tipo de Vacina')['Vacinas Administradas'].sum().reset_index()
fig_bar = px.bar(tipo_vacinas, x='Tipo de Vacina', y='Vacinas Administradas', color='Tipo de Vacina',
                 title="Quantidade de Vacinas por Tipo", color_discrete_map={'CoronaVac': 'blue', 'AstraZeneca': 'green', 'Pfizer': 'red'})
st.plotly_chart(fig_bar)

# Gráfico de Linhas - Vacinas Administradas ao longo dos meses# Convertendo a coluna de data para o tipo datetime
df['data_vacinacao'] = pd.to_datetime(df['data_vacinacao'], errors='coerce')
# Agrupando os dados por mês e somando as vacinas aplicadas
df['mes'] = df['data_vacinacao'].dt.to_period('M')
df_mensal = df.groupby('mes')['vacinas_aplicadas'].sum().reset_index()
# Criando o gráfico
fig = px.line(df_mensal, x='mes', y='vacinas_aplicadas', title='Vacinas Aplicadas por Mês')


# Filtro interativo para visualizar dados de um estado específico
estado_selecionado = st.selectbox('Selecione um Estado para Detalhes', df['Estado'].unique())
df_estado = df[df['Estado'] == estado_selecionado]
st.write(f"Detalhes para o estado de {estado_selecionado}:")
st.write(df_estado)


