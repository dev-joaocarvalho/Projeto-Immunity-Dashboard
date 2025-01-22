import stremlit as st
import pandas as pd

# Criando o DataFrame com os dados simulados
data = {
    "Data": [
        "2023-01-01", "2023-01-01", "2023-01-01", "2023-02-01", "2023-02-01", "2023-02-01", "2023-03-01", "2023-03-01", "2023-03-01",
        "2023-04-01", "2023-04-01", "2023-04-01", "2023-05-01", "2023-05-01", "2023-05-01", "2023-06-01", "2023-06-01", "2023-06-01",
        "2023-07-01", "2023-07-01", "2023-07-01", "2023-08-01", "2023-08-01", "2023-08-01", "2023-09-01", "2023-09-01", "2023-09-01",
        "2023-10-01", "2023-10-01", "2023-10-01", "2023-11-01", "2023-11-01", "2023-11-01", "2023-12-01", "2023-12-01", "2023-12-01"
    ],
    "Estado": [
        "São Paulo", "Minas Gerais", "Rio de Janeiro", "Bahia", "Pernambuco", "Paraná", "Ceará", "Goiás", "Santa Catarina",
        "São Paulo", "Maranhão", "Rio de Janeiro", "Minas Gerais", "Bahia", "Paraná", "Amazonas", "Espírito Santo", "Rio Grande do Sul",
        "Pernambuco", "Rio de Janeiro", "Mato Grosso", "São Paulo", "Goiás", "Ceará", "Minas Gerais", "Paraná", "Santa Catarina",
        "Rio de Janeiro", "Bahia", "Pernambuco", "Espírito Santo", "Amazonas", "Mato Grosso", "São Paulo", "Goiás", "Rio Grande do Sul"
    ],
    "Tipo de Vacina": [
        "CoronaVac", "AstraZeneca", "Pfizer", "CoronaVac", "AstraZeneca", "Pfizer", "CoronaVac", "AstraZeneca", "Pfizer",
        "Pfizer", "CoronaVac", "AstraZeneca", "Pfizer", "AstraZeneca", "CoronaVac", "CoronaVac", "Pfizer", "AstraZeneca",
        "CoronaVac", "Pfizer", "AstraZeneca", "AstraZeneca", "Pfizer", "CoronaVac", "Pfizer", "CoronaVac", "CoronaVac",
        "Pfizer", "AstraZeneca", "CoronaVac", "Pfizer", "AstraZeneca", "Pfizer", "CoronaVac", "CoronaVac", "AstraZeneca"
    ],
    "Vacinas Administradas": [
        150000, 120000, 80000, 100000, 75000, 60000, 90000, 110000, 70000,
        140000, 95000, 130000, 80000, 120000, 110000, 60000, 50000, 85000,
        75000, 90000, 70000, 110000, 95000, 100000, 115000, 105000, 80000,
        85000, 90000, 65000, 70000, 40000, 55000, 120000, 105000, 95000
    ]
}

# Criando o DataFrame
df = pd.DataFrame(data)

# Salvando como CSV
df.to_csv('dados_vacinacao.csv', index=False)

# Exibindo os primeiros registros do DataFrame para verificação
print(df.head())

