import pandas as pd
import pickle
import os

from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Caminho do dataset e do modelo
DATA_PATH = os.path.join("data", "dados_dengue.csv")
MODEL_PATH = os.path.join("model", "modelo_knn.pkl")

# Carregar os dados
data = pd.read_csv(DATA_PATH)

# Seleciona as colunas que serão usadas como entrada (features)
X = data[['Fever', 'Headache', 'JointPain', 'Bleeding']]

# Coluna alvo (target) — 1 para dengue, 0 para não dengue
y = data['Dengue']

# Divide em treino e teste (80% treino, 20% teste)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Verifica se o modelo já foi treinado e salvo
if os.path.exists(MODEL_PATH):
    # Carrega o modelo treinado
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
    print("Modelo carregado de 'model/modelo_knn.pkl'")
else:
    # Cria e treina o modelo KNN
    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(X_train, y_train)
    
    # Cria a pasta model se não existir
    os.makedirs("model", exist_ok=True)
    
    # Salva o modelo treinado no formato pickle
    with open(MODEL_PATH, "wb") as f:
        pickle.dump(model, f)
    print("Modelo treinado e salvo em 'model/modelo_knn.pkl'")

# Função para calcular as métricas
def calcular_metricas():
    y_pred = model.predict(X_test)
    matriz_confusao = confusion_matrix(y_test, y_pred)
    relatorio_classificacao = classification_report(y_test, y_pred)
    acuracia = accuracy_score(y_test, y_pred)
    
    return matriz_confusao, relatorio_classificacao, acuracia