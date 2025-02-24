import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Immunity",
    page_icon="😷",
    layout="wide",
    initial_sidebar_state="auto"
)

# Carregar os dados
df = pd.read_csv('simulação_dados_vacinacao.csv')

# Título do dashboard
st.title("😷Immunity Dashboard")

# Descrição
st.write("""
    Este dashboard apresenta dados simulados sobre as vacinas administradas em diferentes estados do Brasil.
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

# Gráfico de Linhas - Vacinas Administradas ao longo dos meses
st.subheader("Vacinas Administradas ao Longo do Tempo")
df['Data'] = pd.to_datetime(df['Data'])
df_monthly = df.groupby(df['Data'].dt.to_period('M'))['Vacinas Administradas'].sum().reset_index()
df_monthly['Data'] = df_monthly['Data'].dt.strftime('%Y-%m')

fig_line = plt.figure(figsize=(10,6))
plt.plot(df_monthly['Data'], df_monthly['Vacinas Administradas'], marker='o', color='orange')
plt.title('Vacinas Administradas ao Longo dos Meses')
plt.xlabel('Mês')
plt.ylabel('Vacinas Administradas')
plt.xticks(rotation=45)
st.pyplot(fig_line)

# Filtro interativo para visualizar dados de um estado específico
estado_selecionado = st.selectbox('Selecione um Estado para Detalhes', df['Estado'].unique())
df_estado = df[df['Estado'] == estado_selecionado]
st.write(f"Detalhes para o estado de {estado_selecionado}:")
st.write(df_estado)

st.markdown(
    """
    Desenvolvido por **João Marcos Santos e Carvalho**  
    🌐 [GitHub](https://github.com/dev-joaocarvalho) | 🔗 [LinkedIn](https://www.linkedin.com/in/joaom-s-carvalho)
    """
)





