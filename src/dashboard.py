import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

def grafico_casos_dengue(data: pd.DataFrame):
    """
    Gráfico de barras que mostra a quantidade de pessoas com e sem dengue.
    """
    data['DengueTexto'] = data['Dengue'].map({0: "Sem Dengue", 1: "Com Dengue"})
    contagem = data['DengueTexto'].value_counts().reset_index()
    contagem.columns = ['Resultado', 'Quantidade']
    fig = px.bar(contagem, x='Resultado', y='Quantidade', color='Resultado',
                 title="Casos de Dengue",
                 labels={'Resultado': 'Resultado', 'Quantidade': 'Quantidade de Pessoas'})
    return fig

def grafico_sintomas_comb(data: pd.DataFrame):
    """
    Gráfico de barras para exibir a combinação: Dor de Cabeça + Dor nas Articulações versus dengue.
    """
    # Cria a coluna que indica a presença dos dois sintomas
    data['Headache_JointPain'] = ((data['Headache'] == 1) & (data['JointPain'] == 1)).astype(int)
    grupo = data.groupby(['Headache_JointPain', 'Dengue']).size().reset_index(name='Count')
    grupo['Sintomas'] = grupo['Headache_JointPain'].map({
        0: "Não possui dor de cabeça e dor nas articulações",
        1: "Possui dor de cabeça e dor nas articulações"
    })
    grupo['DengueTexto'] = grupo['Dengue'].map({0: "Sem Dengue", 1: "Com Dengue"})
    fig = px.bar(grupo, x='Sintomas', y='Count', color='DengueTexto', barmode='group',
                 title="Combinação: Dor de Cabeça + Dor nas Articulações vs Dengue")
    return fig

def grafico_sem_sintomas(data: pd.DataFrame):
    """
    Gráfico de barras para exibir pacientes sem nenhum sintoma versus resultado de dengue.
    """
    data['NenhumSintoma'] = ((data['Fever'] == 0) & (data['Headache'] == 0) &
                             (data['JointPain'] == 0) & (data['Bleeding'] == 0)).astype(int)
    grupo = data.groupby(['NenhumSintoma', 'Dengue']).size().reset_index(name='Count')
    grupo['Sintomas'] = grupo['NenhumSintoma'].map({
        0: "Possui algum sintoma",
        1: "Nenhum sintoma"
    })
    grupo['DengueTexto'] = grupo['Dengue'].map({0: "Sem Dengue", 1: "Com Dengue"})
    fig = px.bar(grupo, x='Sintomas', y='Count', color='DengueTexto', barmode='group',
                 title="Pacientes sem Sintomas vs Dengue")
    return fig

def grafico_pie_dengue(data: pd.DataFrame):
    """
    Gráfico de pizza para mostrar a distribuição percentual de casos de dengue.
    """
    data['DengueTexto'] = data['Dengue'].map({0: "Sem Dengue", 1: "Com Dengue"})
    fig = px.pie(data, names='DengueTexto', title="Distribuição Percentual de Casos de Dengue")
    return fig

def heatmap_fever_headache(data: pd.DataFrame):
    """
    Heatmap para visualizar a relação entre Febre e Dor de Cabeça com o resultado de dengue.
    """
    data['DengueTexto'] = data['Dengue'].map({0: "Sem Dengue", 1: "Com Dengue"})
    tabela = pd.crosstab(index=[data['Fever'], data['Headache']], columns=data['DengueTexto'])
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(tabela, annot=True, fmt="d", cmap="YlGnBu", ax=ax)
    ax.set_title("Heatmap: Febre e Dor de Cabeça vs Dengue")
    return fig