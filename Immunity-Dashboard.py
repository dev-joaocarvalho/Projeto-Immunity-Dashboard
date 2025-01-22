import streamlit as st
import pandas as pd
import plotly.express as px

# Configurações iniciais do Streamlit
st.set_page_config(page_title="Immunity Dashboard", layout="wide")
st.title("Immunity Dashboard")

# Carregar dados
def carregar_dados():
    # Substituir pelo caminho do dataset real
    dados = pd.read_csv("vacinacao_jan_2024.csv", sep=';')  # Dataset fornecido
    return dados

data = carregar_dados()

# Selecionar colunas relevantes
data = data[["dt_vacina", "ds_vacina", "ds_dose_vacina"]]
data["dt_vacina"] = pd.to_datetime(data["dt_vacina"], format="%Y-%m-%d")

# Filtros no sidebar
st.sidebar.title("Filtros")
vacinas = st.sidebar.multiselect(
    "Selecione as vacinas:", options=data['ds_vacina'].unique(), default=data['ds_vacina'].unique()
)
data_filtrada = data[data['ds_vacina'].isin(vacinas)]

# Gráfico: Quantidade de vacinas por dia
st.header("Quantidade de vacinas aplicadas por dia")
quantidade_por_dia = data_filtrada.groupby("dt_vacina").size().reset_index(name="quantidade")
grafico_dia = px.bar(
    quantidade_por_dia,
    x="dt_vacina",
    y="quantidade",
    title="Vacinas aplicadas por dia",
    labels={"dt_vacina": "Data", "quantidade": "Quantidade"}
)
st.plotly_chart(grafico_dia, use_container_width=True)

# Gráfico: Vacinas mais aplicadas
st.header("Vacinas mais aplicadas")
quantidade_por_vacina = data_filtrada.groupby("ds_vacina").size().reset_index(name="quantidade")
grafico_vacinas = px.pie(
    quantidade_por_vacina,
    names="ds_vacina",
    values="quantidade",
    title="Distribuição de vacinas aplicadas",
    labels={"ds_vacina": "Vacina", "quantidade": "Quantidade"}
)
st.plotly_chart(grafico_vacinas, use_container_width=True)

# Exibir tabela com dados filtrados
st.header("Dados detalhados")
st.dataframe(data_filtrada)
