# Previsão de Dengue com KNN + Dashboard Interativo

Este projeto realiza **análise exploratória de dados** e **classificação com KNN** utilizando um dataset de sintomas relacionados à **dengue** que foram tiradas da plataforma **Kaggle**. Além disso, disponibiliza **dashboards interativos com Streamlit** para visualizar padrões entre sintomas e casos positivos de dengue.

## Integrantes do Projeto
>[Erick Cirico](https://github.com/erickom8)

>[Iago Kater](https://github.com/iagokater),

>[Daniel Barbante](https://github.com/DanielLucas2305),

>[Vinícius la Serra](https://github.com/vinirls).

## Funcionalidades
- Previsão de possíveis pacientes com dengue com base nos sintomas: febre, dor de cabeça, dor nas articulações e sangramento.
- Visualização de dados e gráficos.
- Estrutura do código modular com separação entre modelo, gráficos e interface.

---

## Como rodar o projeto localmente

### 1. Clone o repositório

```bash
git clone https://github.com/erickom8/dengue_knn_app.git
cd dengue_knn_app
```

### 2. Crie e ative um ambiente virtual (recomendado)

```bash
# Linux/macOS
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

---

## Download do Dataset

O dataset original **não foi incluído no repositório** por questões de tamanho.

Para utilizá-lo:

1. Acesse o link:  
   **[Dengue Dataset - Kaggle](https://www.kaggle.com/datasets/dipayancodes/dengue)**  
2. Baixe o arquivo `dengue.csv` (ou como estiver nomeado).
3. Renomeie para `dados_dengue.csv` (se necessário).
4. Crie e coloque dentro da pasta `data/` do projeto.

---

## Rodando o app Streamlit

Depois de instalar tudo e baixar o dataset, execute o comando:

```bash
streamlit run app.py
```

---

## Estrutura do Projeto

```
.
├── app.py                     # Interface principal do Streamlit
├── model/
│   └── modelo_knn.pkl         # Modelo KNN treinado
│   └── treinar_modelo.py      # Arquivo para gerar o modelo KNN treinado
├── src/
│   ├── dashboards.py          # Código que possuem as funções de criação dos dashboards
│   ├── test.py  
├── data/
│   └── dados_dengue.csv       # Dataset (adicionado manualmente)
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Pré-requisitos

- Python 3.8+
- Pacotes: Streamlit, Scikit-learn, Pandas, Seaborn, Plotly, etc. (listados no `requirements.txt`)

---

## Obrigado pela atenção!
