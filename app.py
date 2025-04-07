import streamlit as st
import numpy as np
import pickle
import pandas as pd
from src.dashboard import (
    grafico_casos_dengue,
    grafico_sintomas_comb,
    grafico_sem_sintomas,
    grafico_pie_dengue,
    heatmap_fever_headache
)

# Configuração da página
st.set_page_config(page_title="Dashboard de Análise de Dengue", layout="wide")
st.title("Dashboard Interativo de Análise de Dados de Dengue")

st.sidebar.header("Informações Adicionais")
st.sidebar.image("assets/logo.jpg", use_container_width =True)
st.sidebar.markdown("""
### Sobre o Projeto
Este projeto é um dashboard interativo para análise de dados de dengue, utilizando Streamlit. Ele inclui visualizações de dados e um modelo de previsão de dengue baseado em KNN.
""")
st.sidebar.markdown("""
### Links Úteis
- [Github do Projeto](https://github.com/erickom8/dengue_knn_app.git)
""")


# Carrega o dataset
data = pd.read_csv("data/dados_dengue.csv")

# Exibe os gráficos usando as funções importadas
st.header("Casos de Dengue")
fig1 = grafico_casos_dengue(data)
st.plotly_chart(fig1, use_container_width=True)

st.header("Dor de Cabeça + Dor nas Articulações vs Dengue")
fig2 = grafico_sintomas_comb(data)
st.plotly_chart(fig2, use_container_width=True)

st.header("Pacientes sem Sintomas vs Dengue")
fig3 = grafico_sem_sintomas(data)
st.plotly_chart(fig3, use_container_width=True)

st.header("Distribuição Percentual de Dengue")
fig4 = grafico_pie_dengue(data)
st.plotly_chart(fig4, use_container_width=True)

st.header("Heatmap: Febre e Dor de Cabeça vs Dengue")
fig5 = heatmap_fever_headache(data)
st.pyplot(fig5)


# Título
st.title("Previsão de Dengue com KNN")

# Carrega o modelo
with open("model/modelo_knn.pkl", "rb") as f:
    model = pickle.load(f)

# Parâmetros de entrada para previsão
st.subheader("Sintomas do paciente:")
fever = st.selectbox("Febre", [0, 1])
headache = st.selectbox("Dor de cabeça", [0, 1])
joint_pain = st.selectbox("Dor nas articulações", [0, 1])
bleeding = st.selectbox("Sangramento", [0, 1])

# Botão de previsão
if st.button("Prever"):
    entrada = np.array([[fever, headache, joint_pain, bleeding]])
    pred = model.predict(entrada)[0]

    if pred == 1:
        st.error("Resultado: *Com Dengue*")
    else:
        st.success("Resultado: *Sem Dengue*")

